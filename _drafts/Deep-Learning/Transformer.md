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

트렌스포머을 본격적으로 파헤치기에 앞서 어텐션(Attention)에 대해 짚고 넘어갈 필요가 있다. 트렌스포머를 소개하는 논문 제목에서도 알 수 있듯이 (Attention is all you need), 본 모델을 이해하기 위해선 기존 seq2seq 모델의 단점을 보완하기 위한 어텐션의 이해가 필수적인 것이다.

[어텐션]({{ site.baseurl }}{% link _posts/Deep-Learning/2022-05-16-attention.md %})에 대해 공부해보았으니 이제 본격적으로 트렌스포머 그 자체에 대해서 공부를 해보고자 한다.


# Attention is all you need

간단히 요약하자면 어텐션(attention) 기법은 fixed length context vector 및 Gradient vanishing의 문제를 구조적으로 가지고 있는 RNN based seq2seq의 단점을 보완할 수 있도록 도입된 모델 구성 방법이었다. encoder가 학습을 통해 가지게 된 각 단어의 hiddens state와 이에 대응되는 같은 뜻, 다른 언어의 단어가 decoder를 통과해 산출된 hidden state를 비교하여 decoder가 현재의 단어를 표현하기에 가장 적합한 encoder의 hidden state를 집중해서 나타낸다는 뜻이었다. 이를 통해 RNN을 통한 기계번역 task 성능은 다시 한번 진보를 이루었으며, 업계 표준을 이루어내고 있었다.

## attention-based RNN을 넘어서

하지만 여전히 RNN 기반의 모델이 문제가 없는 것은 아니었다. RNN은 그 특성상 시계열(time series) 데이터를 차례로 입력받으며 학습이 진행되게 된다. RNN이 input을 받고, 그 안에서 연산과정을 거쳐 output이 출력된 후에야 다음 input을 넣어줄 수 있는 것이다.(Sequential computation) 이러한 구조적 특징 때문에 RNN은 병렬적인 연산이 어려운 구조였으며 이는 모델의 학습, 예측을 느리게 하는 주요 원인으로 지목되었다. 이 문제는 attention이 도입된 새로운 RNN구조에서도 똑같이 적용되는 문제였었다.

그런데 트렌스포머에선 '어텐션만 있으면 된다!'라고 주장하였다. 어텐션을 RNN기반의 모델을 보조해주는 기법에서 그 자체만을 사용하여 seq2seq 모델을 만들 수 있다고 말하는 것이다. RNN을 사용하지 않고 그 이상의 성능을 보여주면서, RNN을 사용하지 않았기에 병렬적인 연산으로 학습, 예측을 빠르게 수행할 수 있는 이 모델은 시간이 지날 수록 딥러닝 분야에 많은 영향을 끼치게 되었다. 요새는 단순한 자연어 관련 task를 넘어서 generative model 만들 때에도, vision 관련 task를 할 때에도 사용되는 중인, 이 분야에 있어서 game-changer의 역할을 제대로 하고 있다.

# Transformer 모델

|![](https://pytorch.org/tutorials/_images/transformer_architecture.jpg)|
|:---:|
|Attention is all you need 논문에서 가져온 Transformer model|

우선 Transformer 구조의 기반이 된 것은 attention 기법이지만, transformer의 module 하나하나를 이해하기 위해선 몇가지 새로운 기법에 대한 이해가 있어야 한다. 초심자가 처음 봤을 때 가장 이해가 가지 않은 모듈은 **Multi-head attention**, **Positional Encoding** 일 것이다. 어쩌면 Position-wise Feed forward layer도 뭔 말인가 싶을 것 같다.~(트렌스포머를 처음 읽었을 때의 내 이야기이다!!)~ 우선 가장 아리송해보이는 두 layer에 대해 나름대로 설명해보고자 한다.

## Multi-head attention

### Query, key, value

Attention의 첫 concept은 단순히 설명하자면 현 시점의 decoder hidden state와 모든 시점에서의 encoder hidden state를 비교하여 유사도가 높은 
encoder의 hidden state들을 집중적으로 학습에 활용하겠다는 아이디어다. 

이 구조는 데이터 구조에서 쿼리(Query), 키(Key), 벨류(Value)의 관계와 매우 유사하다. 데이터구조 중에 { 키 : 벨류 }의 관계를 가지고 있는 구조인 dictionary와 큰 관련이 있다. dictionary에 { 키 : 벨류 } 매핑을 저장해놓고 있으면서 사용자는 자신이 찾고자 하는 value에 매핑되어 있는 key와 대응되는 query로 dictionary의 값들을 탐색하게 된다. 

|![](https://imgs.developpaper.com/imgs/915904713-83a8b6c7ba47d9cb_articlex.png)|
|:---:|
|https://developpaper.com/dismantling-transformer-series-2-detailed-explanation-of-multi-head-attention-mechanism/|

사용자의 입력에 해당하는 query가 dictionary가 가지고 있는 key를 하나씩 들여다보며 유사한 정도를 확인한다. 그리고 그 유사한 정도를 일종의 가중치로써 value에 곱해주고, 이를 더한 가중합을 attention value로써 사용자는 받아들이게 되는 것이다. 

나 같은 경우는 내가 알고 있는 개념에서의 dictionary는 가지고 있는 key와 사용자의 query가 완전히 일치해야만 value값을 반환할 것이라고만 생각했었다. 그래서 처음엔 위와 같은 attention을 query, key, value와 같은 용어로 설명하는 포스트들을 보았을 때 머릿속에 물음표를 지울 수 없었다. DB에서 query, key, value의 관계를 생각했을 때에도 query와 key는 무조건 같아야만 value값을 출력하고 있지 않은가. 여기에서의 query, key, value 관계는 그것 보단 훨씬 유연한 관계인 것이다. **사용자가 가지고 있는 Query값과 컴퓨터가 가지고 있는 Key의 유사도 값을 계산, 그 유사도의 값의 비율만큼 Key와 매핑되어 있는 Value에 가중치 곱 및 가중합을 통해 Attention Value를 계산**하는 일련의 과정이 query, key, value로 대응이 되었다. 이 관계가 머리속에서 정리가 되었을 때 딱딱하게 생각했던 내 머리속 개념이 조금 유연해진 기분이 들었다!

### Self-attention

그래서, 이런 개념이 우리가 배우는 attention에 굳이 대응하는 이유는 무엇일까? 단순히 현시점의 decoder의 hidden state를 가지고 encoder의 모든 hiddens state를 비교한다는 개념인데 굳이 한술 더 떠서 이런 개념을 도입하게 된 것인가? 물론 위 개념만 가지고 RNN기반 seq2seq를 바라보아도 큰 이해의 어려움은 없을 것 같다. 앞선 attention에선 별도의 처리과정 없이 encoder와 decoder의 hidden state들을 가져와서 서로의 값들을 비교한 후, 유사도의 값에 따라 encoder의 hidden state의 가중합으로써 attention value 값을 나타내게 된다. 

> Query : 현 시점의 Decoder의 hidden state
> Key : 모든 시점의 Encoder의 hidden states
> Value : 모든 시점의 Encoder의 hidden states

그런데 self-attention를 처음 접한다면, 위 관계를 정리하기 조금 어색할 수 있다. (적어도 난 그랬다.) 우선 

(대충 self-attention을 하기 위한 과정)

(self-attention과 query, key, value의 관계)


### Multi-head self-attention

()




## Positional Encoding

기존의 RNN 모델은 시계열 data를 차례로 input으로써 받아서 연산을 수행하기 때문에 input값들의 순서에 대한 걱정을 하지 않아도 괜찮았다. 즉, 시계열 data의 순서가 유지된 채로 훈련 및 학습을 시킬 수 있었던 것이다. 그러나 RNN을 사용하지 않는 transformer 모델은 학습 과정에서 이러한 input의 순서를 어떻게 부여할 것인지 생각할 수 밖에 없었다. 앞서 

## Position-wise Feed forward layer




|[](https://3.bp.blogspot.com/-aZ3zvPiCoXM/WaiKQO7KRnI/AAAAAAAAB_8/7a1CYjp40nUg4lKpW7covGZJQAySxlg8QCLcBGAs/s640/transform20fps.gif)|
|:---:|
|https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html|


---
참고문헌

https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html

https://machinelearningmastery.com/a-gentle-introduction-to-positional-encoding-in-transformer-models-part-1/#:~:text=Transformers%20use%20a%20smart%20positional,summed%20with%20its%20positional%20information.