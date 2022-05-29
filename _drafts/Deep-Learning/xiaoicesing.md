---
title: "[Deep Learning] XiaoiceSing"
category:
    - "Deep Learning"
tags:
    - "Generative Model"
    - "SVS"
toc: true
use_math: true
---

# 서론

SVS 시스템은 음악 악보 정보를 바탕으로 singing voice를 만드는 시스템을 통칭한다. 여기서 singing voice는 보통 가사, 템포, 피치 등을 의미한다. SVS 시스템을 잘 만들기 위해선 다음과 같은 요소를 고려해야한다.

1. 명확한 발음, 좋은 음질, 자연스러움을 얻기 위한 spectral feature를 예측할 수 있는 강력한 spectrum model
2. singing의 복잡한 f0 contour를 잘 만들어내는 효과적인 F0 model
3. singing의 박자요소를 잘 배우는 duration model

기존 SVS 모델은 unit concatenation과 statistical parametric synthesis방식으로 SVS시스템을 만들었지만, 자연스로운 노래 소리와는 거리가 먼 방식이었다.

딥러닝모델이 (FFNN, LSTM 등등) SVS 성능을 향상시키는 방식으로 도입되었다. GAN이 FFNN의 over-smoothing effect를 완화시키는 역할을 하였다.

FFT를 이용한 timbre를 모델링 시 exposure bias issue를 해결하는 능력을 가지고 있었고, CNN을 이용해서 singing voice의 long-term dependency를 잘 모델링하는 모델 또한 나오게 되었다.

그런데 이런 모델들 대부분 spectral feature를 잘 모델링하는데 초점이 맞추어져 있고, F0와 duration으로부터 나오는 dynamic과 리듬적 요소에 대해선 잘 다루지 못하는 것 같다.

F0와 duration을 잘 모델링 하기 위한 몇몇 연구가 제안되었다. 
F0 모델링 부분에선, note에 대해 예측 F0의 weighted average를 계산하는 방식이 제시되었다. 이 방식의 문제점은 SVS에서의 out-of-tune 문제의 완화가 여전이 어렵다는 것이다. 그리고 후처리 방식은 F0 contour의 dynamic을 smooth할 것이라는 점이고, F0와 spectral feature의 잠재적인 상호관계를 무시한다는 단점이 있다. 

duration model에선 musical note의 길이와 predicted duration의 길이를 맞추는 과정이 들어가는데, 한 연구에선 phoneme duration의 합을 post-processing method를 통해 duration prediction의 정규화시킴으로써 total predicted duration을 note duration으로 heuristic하게 맞추었다. 이 연구 또한 모델 자체가 duration을 정확하게 예측하는 것이 중요했다. 게다가 위 연구에선 F0, duration, spectum model이 독립적으로 학습되었어서 singing voice의 일관성과 음악적 요소에 관한 정보가 무시된다는 단점이 있다.

이 연구에서 제시하는 xiaoicesing은 Fast-speech에서 영감을 따오고 약간의 수정을 통해 SVS 모델을 만들었다.
1. 가사의 phoneme sequence 뿐만 아니라 note ducation, note pitch와 같은 정보또한 encoding한 후 input으로 제공한다.
2. out-of-tune issue문제를 헤결하기 위해 note pitch와 predicted f0 사이에 residual connection을 붙인다.
3. phoneme duration loss와 더불어서 syllable duration loss이 학습 과정에서 고려되어서 리듬을 좀 더 살릴 수 있게 하였다.
4. Mel spectrogram 대신, Mel-generalized cepstrum (MGC)과 band aperiodicity(BAP)을 모델링하고 WORLD vocoder를 사용하여 singing voice를 합성함으로써 input F0 contour와 generated singing voice의 F0 contour가 일관성을 가질 수 있도록 한다.

Decoder와 duration predictor가 같은 encoder를 공유하는 Fastspeech의 구조를 이용해서 spectrum과 F0, duration model이 같이 학습되게 된다.

# Architecture



---------
