---
title: "[Dev] c++"
category:
    - "Dev"
tags:
    - "C++"
toc: true
---

c++:
    * constexpr
        * 참고 문헌 : https://modoocode.com/293
        * 해당 객체나 함수의 리턴값을 컴파일 타임에 값을 알 수 있다
        * 컴파일러가 컴파일 타임에 어떤 식의 값을 결정할 수 있으면 해당 식을 상수식 (Constant expression) 이라 표현.
            이 중에서 값이 정수인 것을 정수상수식(Integral constant expression)
        * const와 헷갈릴 수 있다.
            * const로 정의된 상수들은 굳이 컴파일 타임에 그 값을 알 필요 없음.
            * 반면 constexpr변수는 반드시 오른쪽에 다른 상수식이 와야한다.
    * 리터럴
        * 참고문헌 : https://boycoding.tistory.com/155
        * c++에 2가지 상수가 존재
            * 리터럴 (literal)
            * 심볼릭 (Symbolic)
        * 리터럴 상수 : 코드에 직접 삽입된 값 -> 변경할 수 없으므로 상수이다.
        * 매직넘버
            ```C++
            int maxStudents = numClassrooms * 30;
            ```
            * 위 코드에서 30과 같은 숫자를 매직 넘버라고 한다.
            * 컨텍스트가 없는 코드 중간에 하드 코딩된 리터럴을 칭함.
            * 이를 사용하는 것 나쁜 습관: 매직 넘버가 무엇에 사용되는지에 대한 컨텍스트 없고, 나중에 값을 바꿔야 하면 문제 발생.
JUCE:
    * FIFO
        * 