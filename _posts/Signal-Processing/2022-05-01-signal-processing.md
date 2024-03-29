---
title: "[Signal Processing] 신호처리란?"
category:
    - "Signal Processing"
tags:
    - "Speech"
toc: true
---

# 1. 서론

오늘날 우리는 **신호**의 시대에 살고 있다. 우리가 보고(Vision), 듣는(Sound) 느낄 수 있는 신호 뿐만 아니라, 전자기기들이 연산, 정보 저장, 정보 전송 등을 위해 사용하는 전자기적 신호까지. 

사람들의 생활속에서 사용되는 여러 제품들은 신호처리가 필수적으로 사용되고 있다고 하여도 무방하다. 신호 처리는 이전부터 많은 분야에서 사용되고 있었다. 또한 이 분야는 비정형 데이터를 더욱 유연하게 다루어 원하는 결과를 달성하는 딥러닝의 등장으로 한층 더 필요성이 대두되었다. 딥러닝은 정제되지 않은 noisy한 정보(신호)를 받아들여 사람들이 놀랄만한 결과물을 만들어내고 있는 중이니 이 분야에 있는 사람들에겐 관련분야로써 관심을 가져야 한다.

향후의 ML Researcher의 길을 걷고자 하는 나로선, 딥러닝이 우리 생활에 실질적인 도움을 줄 수 있기 위해 사람에게 필요한 결과를 산출해야 한다고 생각한다. 이를 위해선 딥러닝이 학습에 이용하는 데이터(신호) 그 자체를 들여다보고 이에 맞는 모델을 구축해야 효율적인 학습을 할 수 있다 생각한다. 이를 위해 신호처리분야를 공부하고 앞으로 모델 연구에 적용시킬 수 있으면 연구자로서의 역량이 훨씬 높아질 것이다.

부족하지만 차근차근 하나씩 관련 내용들을 공부하고 블로그에 정리해보고자 한다. 

서론이 길었다. 신호처리의 기초부터 정리해보자.

# 2. 신호처리란?
신호처리는 다양한 신호를 가공(처리)하여 이를 활용하는 학문을 의미한다. 크게 아날로그 신호처리와 디지털 신호처리로 나뉘어지지만, 오늘날의 신호처리는 디지털 신호처리를 의미한다. [^1] 

아날로그 신호는 데이터가 연속적인 값으로 나타나는 신호를 뜻하게 된다. 수학적으론 정의역이 실수인 함수로써 나타낼 수 있다. 우리가 실생활에서 접하는 많은 신호는 대부분 아날로그 신호다. 

그렇다면 디지털 신호는 뭘까? 디지털 신호의 사전적 정의는 데이터를 일련의 이산 값으로 나타낸 신호이다.[^2] 즉, 신호의 형태가 비연속적이라는 뜻이다.

<p align="middle">
  <img src="https://dbscthumb-phinf.pstatic.net/2906_000_1/20140403184104493_EKR6TPZA5.jpg/z7_term31_i3.jpg?type=w300_fst&wm=N" /> 
  <em>디지털신호</em>
</p>


# 3. 아날로그 신호를 디지털 신호로
아날로그 신호는 정의역이 실수로서 나타낼 수 있다고 설명하였다. 그런데 실수는 무한하며, 이는 전자회로에서 다룰 수 없다. 따라서 신호 처리를 위해선 일상에서 사용되는 아날로그 신호를 디지털 신호로 변환하게 된다. 이 과정은 샘플링(Sampling)을 통해 이루어지게 된다. 

샘플링을 통해 정보손실이 일어나지 않게 하기 위해 사용하는 sampling theorem과 샘플링 이후에 사용하는 Fast Fourier Transformation는 추후 나 스스로 공부하여 정리한 후에 정리해야겠다.

![](https://en.wikipedia.org/wiki/File:Signal_Sampling.svg)

음성, 이미지, 영상 등의 사람이 받아들이는 아날로그 신호를 **전류 및 전압값과 같은 전자기적 신호로 변환**하여 나타낸 디지털 신호를 처리한다는 뜻이다. 변환된 디지털 신호는 소프트웨어로 쉽게 가공할 수 있게 된다.

우리 일상 생활에서 사용하고 있는 마이크가 대표적으로 아날로그 신호를 디지털 신호로 바꾸어주는 **변환기**이다. 마이크는 일련의 과정을 통해 물리적인 파형을 전류 및 전압의 파형으로 변환해준다. [^1] 

---
[^1]: [네이버 지식백과 - 신호처리](https://terms.naver.com/entry.naver?cid=44414&docId=2073329&categoryId=44414)

[^2]: [위키백과 - 디지털 신호](https://ko.wikipedia.org/wiki/%EB%94%94%EC%A7%80%ED%84%B8_%EC%8B%A0%ED%98%B8)

---
