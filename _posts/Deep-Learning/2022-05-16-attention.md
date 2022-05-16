---
title: "[Deep Learning] 어텐션"
category:
    - "Deep Learning"
tags:
    - "NLP"
    - "seq2seq"
toc: true
use_math: true
---

# 서론
트렌스포머에 대해 정리를 해보아야 할 것 같아서 트렌스포머의 기반 기술이 되는 attention의 기초를 단단히 하고 가고 싶어서 블로그 글을 작성하게 되었다.

## 기존 seq2seq 모델의 단점

### 기존 seq2seq 모델: RNN based seq2seq
attention 기법이 소개되기 전, 번역 task를 수행하는 딥러닝 모델 중 가장 좋은 성능을 달성했던 것은 RNN 기반의 encoder, decoder를 가진 seq2seq 모델이었다. (seq2seq 모델이란, 입력 데이터를 시퀀스(sequence)로 받고 출력 데이터를 시퀀스(sequence)로 내놓는 모델을 뜻한다.) 
> "I am a student" -> [Seq2Seq model] -> "je suis étudiant"


좀 더 구체적으로 설명하자면 번역하고자 하는 문장의 단어들을 encoder RNN에 하나씩 input으로 주고, 이를 바탕으로 encoder는 문장이 마무리 되었을 때 fixed-length의 vector를 decoder에 넘겨주게 된다. 이 fixed-length vector에는 이전에 encoder에 입력으로 주었던 문장에 대한 함축적인 정보가 들어있는 것이다. 

|![](https://wikidocs.net/images/page/24996/seq2seq%EB%AA%A8%EB%8D%B811.PNG)|
|:---:|
|딥 러닝을 이용한 자연어 처리 입문: 시퀀스 투 시퀀스 (Wikidocs)|

decoder는 이 fixed-length vector를 입력받은 후에 문장 시작 패딩을 받아 첫 단어를 출력하게 된다. 이후 출력된 첫 단어를 다시 decoder에게 입력시켜 두번째 단어를 출력하고, 두번째 단어를 입력시켜 세번째 단어를 출력하고. 이 과정을 반복해서 결국 문장 종료 패딩이 decoder로부터 출력될 때까지 출력 단어를 입력 단어로써 되먹이게 된다. 이 모델은 짧은 문장에 대해서 높은 정확도의 번역 완성을 보였다.


### fixed-length vector의 함정
그렇다면 이 모델의 단점이 무엇이길레 개선을 하게 된 것일까? 가장 큰 단점은 encoder에 입력값으로 줄 수 있는 input sequence의 길이는 정해져 있지 않은데, encoder의 결과값으로 나온 context vector가 고정된 길이를 가지고 있다는 것이다. input sequence의 길이가 짧다면 문제가 되지 않을 수 있지만, 만약 input sequence의 길이가 길게 주어진다면 모든 단어를 표현하기엔 context vector의 길이가 부족할 수 있다는 것이다.

> "I am a student" -> [encoder] -> [모든 input이 충분히 표현된 context vector]
>
> "The Renaissance kitchen had a definite hierarchy of help who worked together to produce ...." -> [encoder] -> [모든 input이 충분히 표현된 context vector]

이는 당연히 성능저하로 이루어질 수 밖에 없었다. 특히 sequence의 길이가 길 수록 encoder가 출력하는 context vector는 많은 정보를 함축하려 할 것이고, 이는 번역의 질을 떨어뜨리는 결과를 낳게 되었다.

이와 더불어 RNN 모델이 가지고 있는 고질적인 문제인 장기 의존성 문제점(long term dependency problem)으로 인해 encoder에 초반에 입력된 단어일수록 최종 결과물에 반영이 되기 힘들다는 단점도 존재했다. 이는 후반에 발생한 결과값의 loss가 RNN을 통과하면서 초반의 RNN 가중치에는 영향을 많이 주지 않게 되는 기울기 소실 (gradient vanishing) 문제 때문이었다.

|![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbiIVTW%2Fbtq6lmQLYc8%2FPL3jSLYvejvJWbp2eCoRF1%2Fimg.jpg)|
|:---:|
|https://www.slideshare.net/albahnsen/classifying-phishing-urls-using-recurrent-neural-networks-75314663|

$h_{t+1}$ 의 loss를 계산하여 RNN 모델인 A를 통과시키다보면 가중치를 수정시켜주는 기울기의 값이 점점 완만해져서 결국 $x_1, x_2$까지 도달하게 되는 기울기가 없게 된다는 것이다.

이러한 RNN based seq2seq문제를 해결하기 위해서 연구자들은 많은 고민을 하게 된다. 많은 연구들이 소개되었고, 그 중 하나로 input sequence가 길어져도 output의 정확도를 개선해줄 수 있는 방법인 attention 기법이 소개되었다.


## RNN seq2seq의 단점을 보완하기 위해 등장한 attention
attention의 아이디어는 (각 시점마다 생성되는 decoder의 hidden state)를 (모든 시점에서의 encoder의 hidden state)와 비교한다는 것이다. 각 encoder의 hidden state는 번역하고자 하는 각각의 단어의 정보를 가지게 된다. 그렇다면 decoder가 해당 시점에서 예측하고자 하는 단어의 정보는 encoder의 hidden state를 들여다보면 알 수 있지 않을까? 특히, 그 시점에서 예측해야하는 단어의 정보를 가진 encoder의 hidden state는 더욱 집중해서(attention) 본다면 번역의 질이 훨씬 높아질 것이라는게 이 기법의 핵심 아이디어가 되는 것이다.

### attention의 작동 기작

|![](https://wikidocs.net/images/page/22893/dotproductattention1_final.PNG)|
|:---:|
|https://wikidocs.net/22893|

attention의 작동 기작을 이미지로 표현하자면 위와 같이 나타나게 된다. 위 상황은 encoder에 입력으로 [I, am, a, student]를 차례로 입력하였으며, 이 정보를 바탕으로 decoder가 차례로 단어들을 예측하고 있는 상황이다. 

#### attention score
|![](https://wikidocs.net/images/page/22893/dotproductattention2_final.PNG)|
|:---:|
|https://wikidocs.net/22893|

decoder에 suis라는 프랑스어 단어를 집어넣게 되었을 때, (이는 je 단어를 decoder에 넣었을 때 출력되는 output이다) decoder는 이 단어를 해석하는 hidden state를 출력하게 된다. attention 기법은 이렇게 나타난 '특정 시점의' decoder hidden state를 '모든 시점의' encoder hidden state와 비교하고, 유사한 정도를 점수로써 환산하게 되는데 이를 attention score라고 한다. attention score를 구하는 방법은 다양하게 제시되었지만, 가장 대표적인 attention score function은 dot product를 구하는 것이다. 즉, 다음과 같은 수식을 통해 attention score를 구하게 된다.

$$
score(s_t, h_i) = s_t^Th_i
$$

위 그림에서 attention score는 각 encoder의 hidden state마다 하나의 scalar값으로 나타나지게 된다.

#### attention distribution
|![](https://wikidocs.net/images/page/22893/dotproductattention3_final.PNG)|
|:---:|
|https://wikidocs.net/22893|

위의 과정으로 구해진 모든 attention score에 softmax 함수를 적용하여 모든 값들의 합이 1이 되게 되는 분포로써 나타낼 수 있게 된다. 이렇게 만들어지게된 값들은 통틀어서 attention distribution이라고 부르게 된다. 각각의 attention distribution의 값들은 'decoder의 hidden state가 encoder의 hidden state들 중에 어떤 state를 많이 참고하는가'를 정량화했다고 보아도 될 것 같다. 즉, attention distribution에서의 값이 클 수록 decoder의 hidden state는 해당 encoder의 hidden state와 강하게 연관되어 있다는 것이다.


#### attention value
|![](https://wikidocs.net/images/page/22893/dotproductattention4_final.PNG)|
|:---:|
|https://wikidocs.net/22893|

위 과정을 통해 만들어진 attention distribution을 해당 encoder의 hidden state와 곱해서 사용하게 된다. attention distribution의 각 값은 스칼라이기 때문에 encoder의 hidden state와 곱해지게 됨으로써 가중치의 역할을 하게 된다. 이렇게 곱해져서 만들어진 weighted encoder hidden state들을 모두 더해서 만들어지게 된 vector를 attention value라고 표현한다. 이 vector는 encoder의 문맥을 표현하기 때문에 context vector라고도 표현을 한다.

-----
참고문헌

https://wikidocs.net/22893

https://glee1228.tistory.com/3

https://bkshin.tistory.com/entry/NLP-14-%EC%96%B4%ED%85%90%EC%85%98Attention#:~:text=%ED%95%9C%EA%B5%AD%EC%96%B4%EB%A5%BC%20%EC%98%81%EC%96%B4%EB%A1%9C%20%EB%B2%88%EC%97%AD,%EB%AC%B8%EC%9E%A5%20%EB%B3%80%ED%99%98%ED%95%98%EB%8A%94%20%EA%B2%83%EC%9E%85%EB%8B%88%EB%8B%A4