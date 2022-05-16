---
title: "[Deep Learning] 트렌스포머"
category:
    - "Deep Learning"
tags:
    - "NLP", "Transformer"
toc: true
use_math: true
---
# 서론

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

이와 더불어 RNN 모델이 가지고 있는 고질적인 문제인 장기 의존성 문제점(long term dependency problem)으로 인해 encoder에 초반에 입력된 단어일수록 최종 결과물에 반영이 되기 힘들다는 단점도 존재했다. 이는 후반에 발생한 결과값의 loss가 RNN을 통과하면서 초반의 RNN 가중치에는 영향을 많이 주지 않게 되는 기울기 소실 (gradient vanishing) 문제때문이었다.

|![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbiIVTW%2Fbtq6lmQLYc8%2FPL3jSLYvejvJWbp2eCoRF1%2Fimg.jpg)|
|:---:|
|https://www.slideshare.net/albahnsen/classifying-phishing-urls-using-recurrent-neural-networks-75314663|

위 그림을 보면 이해가 더욱 쉽다. $h_{t+1}$ 의 loss를 계산하여 RNN 모델인 A를 통과시키다보면 가중치를 수정시켜주는 기울기의 값이 점점 완만해져서 결국 $x_1, x_2$까지 도달하게 되는 기울기가 없게 된다는 것이다.

이러한 RNN based seq2seq문제를 해결하기 위해서 연구자들은 많은 고민을 하게 된다. 많은 연구들이 소개되었고, 그 중 하나로 input sequence가 길어져도 output의 정확도를 개선해줄 수 있는 방법인 attention 기법이 소개되었다.


## RNN seq2seq의 단점을 보완하기 위해 등장한 attention
attention의 아이디어는 (각 시점마다 생성되는 decoder의 hidden state)를 (모든 시점에서의 encoder의 hidden state)와 비교한다는 것이다. 각 encoder의 hidden state는 번역하고자 하는 각각의 단어의 정보를 가지게 된다. 그렇다면 decoder가 해당 시점에서 예측하고자 하는 단어의 정보는 encoder의 hidden state를 들여다보면 알 수 있지 않을까? 특히, 그 시점에서 예측해야하는 단어의 정보를 가진 encoder의 hidden state는 더욱 집중해서(attention) 본다면 번역의 질이 훨씬 높아질 것이라는게 이 기법의 핵심 아이디어가 되는 것이다.

### attention의 작동 기작


<br>


# 'Attention' is all you need
트렌스포머을 본격적으로 파헤치기에 앞서 어텐션(Attention)에 대해 짚고 넘어갈 필요가 있다. 트렌스포머를 소개하는 논문 제목에서도 알 수 있듯이, 본 모델을 이해하기 위해선 기존 seq2seq 모델의 단점을 보완하기 위한 어텐션의 이해가 필수적인 것이다. 

<br>

# Attention is 'all you need'
그런데 트렌스포머에선 '어텐션만 있으면 된다!'라고 말하고 있는 것이다. 

<br>

## attention-based RNN을 넘어서


---
참고문헌

https://bkshin.tistory.com/entry/NLP-14-%EC%96%B4%ED%85%90%EC%85%98Attention#:~:text=%ED%95%9C%EA%B5%AD%EC%96%B4%EB%A5%BC%20%EC%98%81%EC%96%B4%EB%A1%9C%20%EB%B2%88%EC%97%AD,%EB%AC%B8%EC%9E%A5%20%EB%B3%80%ED%99%98%ED%95%98%EB%8A%94%20%EA%B2%83%EC%9E%85%EB%8B%88%EB%8B%A4.

https://machinelearningmastery.com/a-gentle-introduction-to-positional-encoding-in-transformer-models-part-1/#:~:text=Transformers%20use%20a%20smart%20positional,summed%20with%20its%20positional%20information.

https://github.com/bentrevett/pytorch-seq2seq
