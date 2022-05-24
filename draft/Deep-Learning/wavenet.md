
# WaveNet
기본적으로 waveform x = {x_1, ..., x_T}의 joint probability를 구하기 위해 조건부확률의 곱을 사용하게 된다. 즉,

$$
p(x) = \Pi^T_{t=1}p(x_t | x_1, ..., x_{t-1})
$$

## Causal Convolution

기본적으로 causal convolution에서 왔다.
prediction을 할 때, timestep t는 t 이후의 timestep을 이용하지 못하는 구조이다.
1D data를 다룰 때에 간단하게 input을 shift하여 마지막 구간의 input에 output을 삽입하면 된다.

(causal convolution 그림)

## Causal Convolution의 단점과 Dilated Causal convolution

좋은 구조이고, recurrent connection이 없기 때문에 RNN보다 학습이 빠르지만, 많은 양의 convolution layer가 필요하다.
따라서 computational cost 높음

이를 해결하기 위해 dilated convolution사용
dilated convolution?: input을 받아들이고, dilate 크기만큼 skip하는, 그래서 filter 자체의 크기보다 더 넓은 영역을 다루는 convolution을 말한다.

(대충 dilate convolution 그림)

## Softmax distribution
conditional distribution을 ($p(x_t | x_1, ..., x_{t-1})$) 모델링 하기 위해 사용됨.
mixture model (mixture density model 이나 mixture of convolutional Gaussian scale mixture)를 사용할 수도 있지만, softmax distribution이 더 성능 좋다고 한다. (심지어 input값이 audio sample 같이 continuous한 값으로서 나타날 때에도 성능이 더 좋았다) 왜냐하면 categorical distribution이 분포의 모양에 대한 가정이 없기 때문에 임의의 분포를 더 잘 모델링 한다고 한다.

raw audio는 보통 16bit integer value로서 저장되기 때문에, softmax layer는 65536개의 확률을 매 timestep마다 만들게 된다. 이는 $\mu$-law companding transformation을 통해 256개의 값으로써 quantize할 수 있게 된다.

$$
f(x_t) = sign(x_t)\cfrac{ln(1 + \mu|x_t|)}{ln(1 + \mu)}
$$

여기서 -1 < $x_t$ <1 이고, $\mu$ = 255이다.

## Gated Activation Units
PixelCNN과 같은 gated activation unit을 사용한다고 함

$$
z = tanh(W_{f, k} * x) \cdot \sigma (W_{g, k} * x)
$$

여기서 *는 convolution을 의미하고, $\cdot$은 element-wise multiplication을 의미한다. k는 layer index, f와 g는 filter와 gate를 의미한다. W는 학습가능한 convolution filter를 의미함.

## Residual and skip connections

(residual block 그림)

수렴 속도를 높이고 더욱 layer를 쌓을 수 있게끔 만든 block이다.

## Conditional Wavenet

(Conditinal wavenet 그림)

추가적인 조건으로서 주어지는 input h가 있을 때, conditonal distribution은 p(x | h)를 모델링 하기 위해선 식이 약간 바뀐다.

$$
p(x | h) = \Pi^T_{t=1}p(x_t | x_1, ..., x_{t-1}, h)
$$

조건을 줌으로써 WaveNet이 원하는 특성을 가지는 audio를 학습할 수 있게 한다. 예를들어, 다화자 setting에서는 h값에 speaker identity를 추가적인 input으로 줌으로써 합성하고자 하는 speaker를 설정해줄 수 있다.

조건을 주는 방식을 두가지로 분류할 수 있다. 1) global conditioning, 2) local conditioning

### global conditioning

global conditioning은 하나의 잠재표현인 h만으로 모든 timestep의 output distribution에 영향을 주는 형태의 조건을 말한다. TTS를 합성할 때의 speaker embedding과 같은 값이 여기에 해당할 것이다.

그렇게 된다면 앞서 소개했던 activation function의 수식이 살짝 변형되게 된다.

$$
z = tanh(W_{f, k} * x + V^T_{f, k} h) \cdot \sigma (W_{g, k} * x + V^T_{g, k} h)
$$

여기서 $V_{*, k}$ 는 학습가능한 linear projection이고, $V^T_{*, k} h$ 는 시간축에 대해 적용이 되게 된다.

### local conditioning

local conditioning은 audio signal보다 더 작은 sampling frequency로서 만들어지게된 시계열이 $h_t$로서 주어지게 된다. 그 후 시계열 data를 upsampling하여 새로운 시계열인 y=f(h)로서 만들어 audio signal과 같은 resolution을 가지게 맞춘 후, activation unit을 다음과 같이 적용한다.

$$
z = tanh(W_{f, k} * x + V_{f, k} y) \cdot \sigma (W_{g, k} * x + V_{g, k} y)
$$

여기서 $V_{f, k} * y$ 는