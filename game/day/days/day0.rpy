label day_0:

    scene black with fade
    pause 1.0

    "빛은 없었다."
    "공기는 정체되어 있었고, 시간은 얼어붙은 듯했다."

    scene bg_trunk_dark with slow_dissolve
    "정신을 차렸을 때, 나는… 차 트렁크 안이었다."

    "손발은 묶여 있지 않았다. 하지만 움직일 수 없었다."

    scene bg_cell_dark with fade
    "그리고 여기가, 지금의 감금실이다."

    "그가 말했다. 단 한 문장."

    show dios_neutral at right with dissolve
    d "30일을 줄게, 나탈리아."
    d "그 안에 날 이해하거나, 그 안에 무너지거나."

    hide dios_neutral with dissolve

    pause 0.5

    "이것은 감옥이다."
    "하지만 고해성사를 할 수 있는 교단의 형식을 띠고 있다."

    "내 하루는 기도, 노동, 정찰 중 하나로 시작된다."
    "그리고 매일 밤, 그는 신부의 얼굴로 나를 고해성사실로 부른다."

    scene black with fade
    pause 0.5

    "나는 거짓말을 할 수도 있다."
    "침묵할 수도 있고, 모든 것을 말할 수도 있다."

    "그러나 그가 보고 있다는 것을 잊어선 안 된다."

    pause 0.5

    show screen hud

    "이 게임에서 당신은 다음과 같은 수치를 관리하게 됩니다:"

    hide screen hud

    pause 0.5

    show text "🛐 신성력: 기도를 통해 축적되며, 신의 개입이나 특별한 능력을 해금합니다." with dissolve
    pause
    hide text
    show text "🧠 스트레스: 높을수록 고해성사에서 실수할 위험이 높아집니다." with dissolve
    pause
    hide text
    show text "😨 불안: 불안이 누적되면 정신이 붕괴되기 시작합니다." with dissolve
    pause
    hide text
    show text "🤍 디오스 신뢰: 높으면 그가 관대해지지만, 낮을수록 도망칠 기회가 생깁니다." with dissolve
    pause
    hide text

    "그리고, 이 30일의 끝에서 나는 하나의 결말을 맞게 된다."

    show dios_neutral at right with fade
    d "시작하자. 애송이."
    hide dios_neutral with dissolve

    pause 0.5

    jump day1
