---
title: "[Signal Processing] 디랙 델타 함수"
category:
    - "Signal Processing"
tags:
    - "Speech"
toc: true
---


# 1. 서론
앞선 포스팅에서 신호와 신호처리에 대해 정리해보았다. 아날로그 신호의 연속성을 컴퓨터는 다루기 힘들기 때문에 샘플링을 통해 디지털신호로 변환한다고 설명했었다. ~~(물론 샘플링 뿐 아니라 양자화 같은 다른 몇몇 과정을 거쳐 변환하긴 하지만..)~~

컴퓨터가 다룰 수 있는 디지털 신호로 변환하는 첫번째 관문인 샘플링, 그런데 과연 어떤 방식으로 샘플링 하는 것이 좋을까? 신호처리 관련 공부를 시작하기 전엔 '일정 간격으로 신호의 값을 하나씩 뽑아서 만드는 것 아니야?'정도로 생각하고 있었는데, 찾아보니 

$\large f(t)\ =\ \sum\limits_{n=-\infty}^{\infty} C_{n}e^{j\frac{2\pi n}{T} t}$

$C_{n}\ =\ \frac{1}{T}\int_{0}^{T}f(t)e^{-j\frac{2\pi n}{T} t}\ dt\quad for\ n\ =\ \ldots,-2,-1,0,1,2,\ldots$

<br><br><br>
# 2. 디랙 델타 함수 (Dirac delta function; $\delta(t)$)
디랙 델타 함수는 impulse function으로도 불린다. 디랙 델타 함수는 샘플링할 때 뿐만 아니라, 푸리에 변환할 때에도 중요한 키워드로써 사용되니 짚고 넘어가야 할 것 같다.



# 3. 아날로그 신호를 디지털 신호로

---
[^1]: [네이버 지식백과 - 신호처리](https://terms.naver.com/entry.naver?cid=44414&docId=2073329&categoryId=44414)

[^2]: [위키백과 - 디지털 신호](https://ko.wikipedia.org/wiki/%EB%94%94%EC%A7%80%ED%84%B8_%EC%8B%A0%ED%98%B8)

---
