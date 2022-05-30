


# mel-spectrogram

# Spectral

http://recherche.ircam.fr/anasyn/schwarz/da/specenv/3_3Spectral_Envelopes.html#:~:text=A%20spectral%20envelope%20is%20a,Envelope%20fit

Spectral Envelop은 frequency-magnitude plane에 그려지는 곡선이며, Fourier magnitude spectrum에 의해 유도된다. 한 window마다 하나의 값을 가지게 된다. 다음과 같은 특성을 가져야 한다.

1. Envelope fit
   이 곡선은 스팩트럼의 envelope를 그리게 된다. 즉, magnitude spectrum을 잘 연결하는 peak를 연결하는 곡선이 된다. 

2. Regularity
   곡선의 smoothness나 regularity가 필요하다. 즉, 곡선은 너무 많이 진동하면 안되지만 신호의 에너지/진동수 의 분포를 잘 표현해야 한다.

3. Steadyness
   곡선이 완만해야 한다. (수학적 의미의 완만함) 
   

# Cepstral

Ceptrum($c(m)$)은 spectrum의 log형태를 IFT (inverse fourier transform)을 취한 형태를 Ceptral이라고 명명한다.

generalized ceptrum ($c_{\alpha, \gamma}(m)$)은 warped frequency scale $\beta_\alpha(\omega)$ 로 계산된 generalized logarithmic spectrum의 IFT이다.

# Mel-Generalized Cepstral (MGC)


# Mel-Ceptral distortion (MCD)
http://www.cs.columbia.edu/~ecooper/tts/mcd.html


# F0

https://en.wikipedia.org/wiki/Fundamental_frequency


fundamental frequency라고도 부른다. 

periodic waveform의 가장 낮은 주파수를 의미한다.

음악에서는 note의 pitch를 의미한다.