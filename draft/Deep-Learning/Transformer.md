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

간단히 요약하자면 어텐션(attention) 기법은 fixed length context vector 및 Gradient vanishing의 문제를 구조적으로 가지고 있는 RNN based seq2seq의 단점을 보완할 수 있도록 도입된 모델 구성 방법이었다. 이를 통해 RNN을 통한 기계번역 task 성능은 다시 한번 진보를 이루었으며, 업계 표준을 이루어내고 있었다.

## attention-based RNN을 넘어서

하지만 여전히 RNN 기반의 모델이 문제가 없는 것은 아니었다. RNN은 그 특성상 시계열(time series) 데이터를 차례로 입력받으며 학습이 진행되게 된다. RNN이 input을 받고, 그 안에서 연산과정을 거쳐 output이 출력된 후에야 다음 input을 넣어줄 수 있는 것이다.(Sequential computation) 이러한 구조적 특징 때문에 RNN은 병렬적인 연산이 어려운 구조였으며 이는 모델의 학습, 예측을 느리게 하는 주요 원인으로 지목되었다. 이 문제는 attention이 도입된 새로운 RNN구조에서도 똑같이 적용되는 문제였었다.

그런데 트렌스포머에선 '어텐션만 있으면 된다!'라고 주장하였다. 어텐션을 RNN기반의 모델을 보조해주는 기법에서 그 자체만을 사용하여 seq2seq 모델을 만들 수 있다고 말하는 것이다. RNN을 사용하지 않고 그 이상의 성능을 보여주면서, RNN을 사용하지 않았기에 병렬적인 연산으로 학습, 예측을 빠르게 수행할 수 있는 이 모델은 시간이 지날 수록 딥러닝 분야에 많은 영향을 끼치게 되었다.

# Transformer 모델

|![](https://pytorch.org/tutorials/_images/transformer_architecture.jpg)|
|:---:|
|Attention is all you need 논문에서 가져온 Transformer model|

우선 Transformer 구조의 기반이 된 것은 attention 기법이지만, transformer의 module 하나하나를 이해하기 위해선 몇가지 새로운 기법에 대한 이해가 있어야 한다. 초심자가 처음 봤을 때 가장 이해가 가지 않은 모듈은 **Multi-head attention**, **Positional Encoding** 일 것이다. 이 둘에 대한 이해가 선행이 되야할 것 같다.

## Multi-head attention


## Positional Encoding

기존의 RNN 모델은 시계열 data를 차례로 input으로써 받아서 연산을 수행하기 때문에 input값들의 순서에 대한 걱정을 하지 않아도 괜찮았다. 즉, 시계열 data의 순서가 유지된 채로 훈련 및 학습을 시킬 수 있었던 것이다. 그러나 RNN을 사용하지 않는 transformer 모델은 학습 과정에서 이러한 input의 순서를 어떻게 부여할 것인지 생각할 수 밖에 없었다. 



|[](https://3.bp.blogspot.com/-aZ3zvPiCoXM/WaiKQO7KRnI/AAAAAAAAB_8/7a1CYjp40nUg4lKpW7covGZJQAySxlg8QCLcBGAs/s640/transform20fps.gif)|
|:---:|
|https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html|


---
참고문헌

https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html

https://machinelearningmastery.com/a-gentle-introduction-to-positional-encoding-in-transformer-models-part-1/#:~:text=Transformers%20use%20a%20smart%20positional,summed%20with%20its%20positional%20information.