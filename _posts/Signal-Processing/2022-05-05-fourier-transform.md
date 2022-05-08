---
title: "[Signal Processing] 푸리에 변환"
category:
    - "Signal Processing"
tags:
    - "Math"
toc: true
use_math: true
---

# 서론

신호처리에서 정말 많이 쓰이는 푸리에 변환에 대해서 공부해보고자 한다!

다음 포스트를 보고 온다면 이해에 도움이 될 것이다.

[푸리에 급수]({{ site.baseurl }}{% link _posts/Signal-Processing/2022-05-05-fourier-series.md %})

# 푸리에 급수의 확장

* 푸리에 급수를 통해 시간 주기 T를 가진 임의의 주기함수를 단순한 정현파들의 조합으로 표현할 수 있었다.

* 그런데 만약 주기함수의 주기가 무한히 크다는 가정($T \rightarrow \infty$)이 들어간다면, 우리는 이 함수의 주기를 실제로 볼 수 없을 것이다.

* 그렇다면, 주기를 가지고 있지 않은 함수 (비주기함수)를 *주기가 무한대인 주기함수*로 취급해도 되지 않을까?

## 주기가 무한대인 주기함수

* 이전에 다룬 푸리에 급수 식을 본다면,

$$
f(t) = \sum_{n=-\infty}^\infty C_n exp(j\frac{2 \pi n}{T}t) ... (1)
\\
C_n = \cfrac{1}{T}\int_{-T/2}^{T/2}f(t)exp(-j\frac{2 \pi n}{T}t)dt for n = ...,-2, -1, 0, 1, 2, ...
$$

* 위 식을 T에 대해 무한으로 극한을 취해보자

$$
\lim_{T->\infty}f(t) = \lim_{T->\infty}\cfrac{1}{T} \int_{-T/2}^{T/2}f(t)exp( -j \frac{2 \pi n}{T}t) \, dt \, exp(j\frac{2\pi n}{T}t)  ... (2)
$$

* 그 후, 1/T를 u(주파수: frequency) 로 치환하고 T를 포함한 변수들을 정리해준다.

$$
\lim_{T->\infty}T/2 = \infty, \lim_{T->\infty}-T/2 = -\infty, \lim_{T->\infty}1/T = du
$$

* 이를 바탕으로 (2)의 식을 다시 정리한다면 다음과 같다.
$$
\lim_{T->\infty}f(t) = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}
exp( -j 2 \pi u t) dt \,
exp( j2 \pi u t) du
\\
= \int_{-\infty}^{\infty}F(u)exp(j2\pi u t)du
$$

* 여기서 F(u)를 푸리에 급수에서 계수를 나타내는 것으로 볼 수 있다.

* 즉, 주기가 무한대인 주기함수 (= 비주기함수)를 푸리에 급수로서 나타낼 수 있는 것이다. 이를 **푸리에 변환**이라고 한다.

# 푸리에 변환 (Fourier Transform)

* 푸리에 변환은 입력 함수를 받아서 다양한 주파수를 가지는 정현파의 조합으로 표현하는 것을 말한다.

* 입력함수가 주기함수이던, 비주기함수 모두 가능하다는 것이 특징이다.

![](https://en.wikipedia.org/wiki/File:Fourier_transform_time_and_frequency_domains_(small).gif)

## 푸리에 변환 수식
* 위에서 전개한 식을 조금 정리한 것이 푸리에 변환 공식이 된다.
$$
f(t)= \int_{-\infty}^{\infty}F(u)exp(j2\pi u t)du ... (3)
\\
F\{f(t)\} = \int_{-\infty}^{\infty}f(t)exp(-j2 \pi u t) dt ... (4)
$$
* 여기서 $f(t)$는 피변환함수, 즉 푸리에 변환을 적용하기 전의 함수이다.

* $F(u)$는 푸리에변환 함수이다. 푸리에 변환이 적용된 $f(t)$는 $F\{f(t)\}$로 나타낼 수 있다.

* u는 주파수 (frequency)로서, 주기의 역수이다.

* 수식 (3)은 역 푸리에 변환 (Inverse Fourier Transform)이라 부른다. 입력 함수가 푸리에 급수 (즉, $e^{j12\pi ut}$의 조합)으로 표현된다는 의미이다.

* 수식 (4)는 푸리에변환(Fourier Transform)을 의미한다. 이 식은 주파수(u)에 관련된 식으로서, 주파수의 값에 따른 푸리에 급수의 계수 값을 구할 수 있다. 

* 이를 통해 주기함수만 표현할 수 있었던 푸리에 급수를 확장하여, **비주기함수도 간단한 주기함수의 합으로 표현할 수 있게 된 푸리에 변환이 소개 된 것이다.**

----

참고자료
[SuperMemi's Study : 푸리에 변환](https://supermemi.tistory.com/97?category=837542)