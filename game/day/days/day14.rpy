label day14:

    scene bg_cell_dark with slow_dissolve

    show screen hud

    "아직도 어제의 침묵이 남아 있다."

    "하지만 오늘은, 그냥 넘어가지 않기로 했다."

    play sound "sfx/door_open.ogg"
    show d_neutral at left with moveinleft

    d "또 같은 얼굴. 뭐, 특별히 바랄 것도 없지만."

    "그리고 그 순간—"

    "당신은 조용히, 그러나 분명하게 입을 연다."

    menu:
        "“…왜 나를 가뒀어?”":
            "목소리는 떨렸지만, 눈은 흔들리지 않았다."

            d "하… 드디어 질문을 던질 줄 아네?"

            d "왜긴. 재미있으니까."

            d "너 같은 건, 부서지기 직전이 제일 보기 좋거든."

            $ stress += 3
            $ dios_trust += 2

        "“날 시험하는 거야?”":
            "눈을 피하지 않는다. 단도직입적으로."

            d "시험? 흐흐. 그렇게 부르면 덜 잔인해지긴 하지."

            d "하지만 넌 생각보다 잘 버티더라. 신이 곁에 있어서 그런가?"

            $ holiness += 3
            $ anxiety += 3

        "“…날 지키는 거야?”":
            "속삭이는 질문. 마치 자신도 모르게 흘러나온 말."

            d "…지키는 거라고 생각했어?"

            d "그거 위험하다, 나탈리아. 그 착각, 진짜 독해."

            d "근데 말이지—"

            d "그게 꼭 틀린 말도 아닐 수도 있어."

            $ dios_trust += 5
            $ stress -= 2

    d "이제 질문도 하고, 꽤 사람이 다 됐네."

    d "그렇다고 진실에 가까워진 건 아니지만."

    play sound "sfx/door_close.ogg"
    hide d_neutral with dissolve

    "오늘은… 내가 질문을 했고, 그가 대답했다."

    "그 사소한 사실 하나가, 믿을 수 없을 정도로 중요하게 느껴졌다."

    jump day15
