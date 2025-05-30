label day18:

    scene bg_cell_dark with fade
    show screen hud

    "불이 꺼진 감방. 문이 열리지 않았다."

    "그는 오늘 오지 않았다."

    "대신 당신은 처음으로— 그를 불렀다."

    narrator "“d…”"

    "목소리는 작았고, 떨렸고, 그러나 분명히 그 이름이었다."

    play sound "sfx/door_open.ogg"
    show d_neutral at left with dissolve

    d "……부른 거냐, 나를?"

    d "네가 먼저 날 찾은 건… 처음이네."

    menu:
        "“당신은 날 사랑했어?”":
            d "……"

            d "그 질문, 정말 야만적이다. 하지만…"

            d "응. 그랬을지도 몰라. 아니면 지금이라도 그래야 할지도."

            $ dios_trust += 5
            $ anxiety -= 5

        "“왜 날 이렇게 가뒀어?”":
            d "도망갈까 봐. 나에게서."

            d "네 신앙은 나를 부정하니까. 그래서 가뒀지."

            $ stress += 3

        "“…미워.”":
            d "좋아. 미움도 감정이니까."

            d "널 무감각하게 만들고 싶진 않았어."

            $ dios_trust -= 2
            $ anxiety += 2

    "당신은 더 이상 아무 말도 하지 않았다."

    "그의 손이 아주 조금, 당신 쪽으로 움직였지만… 이내 멈췄다."

    jump day19
