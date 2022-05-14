---
title: "[Deep Learning] 왜 딥러닝 초기화가 중요할까?"
category:
    - "Deep Learning"
tags:
    - "Generative Model"
toc: true
use_math: true
---

# 서론

이상적인 딥러닝은 학습과정을 통해 시간이 지나면서 optimal한 한 점으로 수렴하려는 성질을 가지고 있다. 즉, 딥러닝의 가중치 하나하나의 초기값은 학습 초기엔 큰 변동이 일어날 수 있지만 시간이 지나면서 점점 그 변동값이 줄어들게 되며 최적화가 된다. 그렇다면 초기 가중치 값은 학습결과에 영향없을 것이라고 생각할 수도 있다. 학습이 진행되면 어짜피 다 똑같아 질 것
~~(사실 내가 그랬다.)~~ 

하지만 딥러닝 학습에 있어서 가중치 초기화는 생각보다 중요한 문제이다. 딥러닝의 최적화 방식인 GD 알고리즘은  

-------

참고문헌
[^1] https://blog.naver.com/PostView.naver?blogId=handuelly&logNo=221831940317&parentCategoryNo=&categoryNo=31&viewDate=&isShowPopularPosts=true&from=search
[^2] https://cs231n.github.io/neural-networks-2/#init
