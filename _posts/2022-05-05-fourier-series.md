---
title: "[Signal Processing] 푸리에 계수"
category:
    - "Signal Processing"
tags:
    - "Math"
toc: true
use_math: true
---

# 서론
본격적으로 신호처리를 공부하기 전에 짚고 넘어가야하는 수학 개념을 짚고 넘어가야 할 것 같아서 몇 가지를 정리하고자 한다.

# Fourier Series
* 푸리에는 다음과 같은 가정을 한다.
    > **임의의 주기함수들은 단순한 주기함수의 조합으로 표현할 수 있다.**
    * *적절한 계수*를 가지고, *적절한 주기*를 가진 정현파의 조합으로 모든 주기함수를 근사할 수 있다는 아이디어를 생각한 것이다.

* 수식
    * $ f(t) = \sum_{n=-\infty}^{\infty} C_n e^{j \frac{2 \pi n}{T} t} $ ....(1)
    * $ C_n = \cfrac{1}{T} \int_0^T f(t) e^{j \frac{2 \pi n}{T} t} dt $
    * for n = ..., -2, -1, 0, 1, 2, ...

* 복잡한 수식이 소개가 되었지만, 이는 아래와 같은 의미를 가지고 있다.

## 모든 주기함수는 각기 다른 주파수를 가진 정현파 함수의 합이다.

* $w = \cfrac{2 \pi}{T}$ 로 가정한다면 (w: 주기함수의 주파수)
    * $ e^{j \frac{2 \pi n}{T} t} = e^{jnwt}$
    * $e^{jnwt} = cos(nwt) + jsin(nwt)$ -> 오일러법칙

* 이를 위의 (1)의 식에 대입을 한다면
    * $ f(t) = \sum_{n=-\infty}^{\infty} C_n e^{j \frac{2 \pi n}{T} t} $  = $ \sum_{n=-\infty}^{\infty} C_n (cos(nwt) + jsin(nwt)) $

* 위 특징을 통해 적절한 정현파의 조합으로 모든 주기함수를 표현할 수 있다!

|![](https://mathworld.wolfram.com/images/eps-svg/FourierSeriesExamples_1200.svg)|
|:--:|
| *출처 : 울프람알파*|

## 푸리에 계수
* 적절한 정현파의 조합으로 모든 주기함수를 표현할 수 있는데, 각각의 정현파의 계수의 식은 어떻게 나오게 된 것일까?

    | $ C_n = \cfrac{1}{T} \int_0^T f(t) e^{-j \frac{2 \pi n}{T} t} dt$|
    |:---:|
    |이 식이 어떻게 나오게 되는것인가?|

* 주기함수의 직교성을 이용하여 문제를 풀게 된다.
    * 푸리에 급수의 양 변에 켤레복소수를 곱해준다. ($e^{-j \frac{2 \pi q}{T} t}$)

    $$ e^{-j \frac{2 \pi q}{T} t} f(t) = \sum_{n=-\infty}^{\infty} C_n e^{j \frac{2 \pi n}{T} t} * e^{-j \frac{2 \pi q}{T} t} $$
    * 이후, f(t)의 시간주기인 [0, T]로 적분해준다.

    $$ 
    \int _0^T e^{-j \frac{2 \pi q}{T} t} f(t) dt 
    \\ = \int _0^T (\sum_{n=-\infty}^{\infty} C_n e^{j \frac{2 \pi n}{T} t} * e^{-j \frac{2 \pi q}{T} t}) dt 
    \\ = \sum_{n=-\infty}^{\infty} (C_n \int _0^T  e^{j \frac{2 \pi n}{T} t} * e^{-j \frac{2 \pi q}{T} t}) dt ... (2)
    $$

    * 시그마와 적분의 자리를 바꾼다 (시그마의 무한합과 적분의 자리를 바꾸는 과정은 엄밀한 정의가 필요할 것 같지만..)
    * t에 대한 적분이기 때문에 C_n은 관련 없기 때문에 밖으로 뺄 수 있다.

    * 여기서 n = q라면,
    $$ 
    C_n \int _0^T  (e^{j \frac{2 \pi n}{T} t} * e^{-j \frac{2 \pi n}{T} t}) dt
    \\ = C_n \int _0^T  1 dt = C_nT
    $$
    
    * 그리고 n $\neq$ q라면,
    $$
    \int _0^T exp(j\cfrac{2 \pi (n - q)}{T}t)dt
    \\ = \cfrac{T}{2j\pi(n-q)}[exp(j\cfrac{2 \pi (n - q)}{T}t)]_0^T
    \\ = \cfrac{T}{2j\pi(n-q)}[exp(j2 \pi (n - q)) - 1]
    $$
    * 여기서 n, q는 정수이기 때문에 $j2 \pi (n - q)$는 $2 \pi$의 정수배가 되고, $exp(2j\pi(n-q)))$는 1의 값을 가지게 된다.  따라서 위 적분식은 0의 값을 가지게 된다.

* 정리를 두서없이 했지만, (2)를 적분한다면 n = q일 때만 적분값이 $C_nT$의 값을 가지고 나머지 조건일 땐 (n $\neq$ q) 적분값이 0인 것을 확인할 수 있다.
* 따라서,
$$ 
\int_0^T e^{-j \frac{2 \pi q}{T} t} f(t) 
= \int_0^T \sum_{n=-\infty}^{\infty} C_n e^{j \frac{2 \pi n}{T} t} * e^{-j \frac{2 \pi q}{T} t}
= C_nT
\\
\therefore C_n = \cfrac{1}{T} \int_0^T e^{-j \frac{2 \pi q}{T} t} f(t) 
$$

가 되는 것이다.

----
참고문헌

[SuperMemi's Study : 푸리에 급수](https://supermemi.tistory.com/95?category=837542)