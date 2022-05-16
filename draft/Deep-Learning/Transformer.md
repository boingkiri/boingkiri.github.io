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


# 'Attention' is all you need
트렌스포머을 본격적으로 파헤치기에 앞서 어텐션(Attention)에 대해 짚고 넘어갈 필요가 있다. 트렌스포머를 소개하는 논문 제목에서도 알 수 있듯이, 본 모델을 이해하기 위해선 기존 seq2seq 모델의 단점을 보완하기 위한 어텐션의 이해가 필수적인 것이다. 

<br>

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
그렇다면 이 모델의 단점이 무엇이길레 개선을 하게 된 것일까? 

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
