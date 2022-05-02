---
title: "[Dev] Visual studio에서 namespace를 인식하지 않을 때"
category:
    - "Dev"
tags:
    - "Visual Studio"
toc: true
---
* JUCE라는 프레임워크로 큐베이스와 같은 DAW에서 사용할 수 있는 vst의 ui를 개발하는 업무를 맡게 된 우리 인턴씨
* 프레임워크를 다운도 받고, 솔루션 빌드 후 프로젝트를 하나 새로 파서 시작해보려고 하는 찰나..
* Visual studio의 프로젝트 안에 존재하는 namespace(juce)를 인식을 못하는 우리 코드...
* 이것은 실제상황..
* 한번 해결해보자구

솔루션과 프로젝트의 차이에 대해 언급을 해야할 거 같네
나중에 봐보자

c++
    'using' keyword
    'auto' keyword
    'make_unique'
    static cast

JUCE
    ProcessContextReplacing
    ProcessorChain
    IIR filter를 만들 때 사용할 order: 2, 4, 6, 8

Signal Processing
    IIR filter