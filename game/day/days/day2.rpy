label day2:

    scene bg_cell_daylight with dissolve

    show screen hud

    "희미한 빛이 창문 틈으로 스며든다."

    "아침인지 오후인지 모른다. 단지... 어제와는 조금 다르다."

    "당신은 벽에 손을 대며, 스스로에게 묻는다."

    menu:
        "오늘도 살아야 하는 이유는...":
            "기도 속에서 작은 평온을 찾는다."
            $ holiness += 5
            $ stress -= 2

        "없다. 그저 견디는 것이다.":
            "차갑고 무감한 독백이 입에서 새어 나온다."
            $ anxiety += 5
            $ dios_trust -= 1

    "철문이 또다시 열리고, 그가 들어선다."
    
    play sound "sfx/door_open.ogg"
    show d_neutral at left with moveinleft

    d "이틀째다. 아직 버티고 있네?"

    d "혹시 어제보다 나은 하루라도 기대했나? …정말 귀엽군."

    "그의 말투엔 어딘가 장난스럽고, 무언가를 시험하는 조롱이 깃들어 있다."

    d "그래서, 꼬맹이. 아직도 위에 대고 기도나 하고 있나?"

    menu:
        "나는 신을 믿어.":
            "한 치의 흔들림 없는 목소리다."
            d "하, 그러니까 이런 데까지 와서 기도하고 앉았지. 유난스럽긴 해."
            $ holiness += 3
            $ dios_trust += 2

        "믿지 않아. 더 이상은.":
            d "오, 드디어 현실을 좀 보네? 눈 떴네? 축하해."
            $ holiness -= 5
            $ dios_trust += 1
            $ stress += 3

        "......":
            d "하아, 또 침묵인가. 네 고집은 수도벽보다 두껍군."
            $ anxiety += 5

    d "그 착각, 언제쯤 부서질까. 난 참을성이 많은 편이라 다행이지."

    play sound "sfx/door_close.ogg"
    hide d_neutral with moveoutright

    "그는 떠났다. 하지만 그의 목소리는 귓가에 머문다."

    jump day3
