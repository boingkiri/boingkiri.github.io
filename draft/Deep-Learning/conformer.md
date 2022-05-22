# 서론
이렇게 초안만 잔뜩 쌓이고 블로그 글을 못 올리는건 별로 안좋은거 같은데...
오늘은 트렌스포머를 이용하여 딥러닝 모델의 음성인식 성능을 높여준 구조인 컨포머(conformer)에 대해 알아보자.

이 구조는 음성인식을 위해 처음 도입되었지만, 현재 회사에서 개발중인 SVS 시스템에서 transformer 대신에 들어간 것을 보니, 다양한 분야에서 사용할 수 있을 것 같다. 해보자구!

# 

convolution과 self-attention을 결합하여 사용한 모델이 독립적으로 사용한 모델보다 더 좋은 성능을 보인다. 같이 학습하면 local 정보하고 global 정보 둘 다 학습할 수 있다는 것이다.

이 논문에선 convolution과 self attention을 유기적으로 결합하여 global과 local 정보를 효율적으로 학습할 수 있는 방법을 제시한다! self attention이 global interaction을 학습하고 convolution이 local한 corretlation을 학습할 수 있는 구조인 것이다.

어텐션 헤드 숫자, convolution 커널 크기, 활성화 함수 종류, feed forward layer의 종류를 비교해봄으로써 어떤 친구가 가장 정확도 향상이 있었는지 확인한다.

# Conformer Encoder

