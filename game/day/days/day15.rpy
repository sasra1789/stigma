label day15:

    scene bg_cell_dark with slow_dissolve

    show screen hud

    "오늘은 그가 먼저 도착해 있었다."

    show d_somber at left with dissolve

    d "오늘은 너보다 내가 먼저 기다렸네."

    d "기억나? 처음 울던 날."

    "……처음?"

    d "내가 널 발로 차고, 네가 피투성이가 됐을 때 말이야."

    d "근데 넌 그 와중에도… 날 걱정했어."

    menu:
        "“거짓말.”":
            "그럴 리 없다. 그런 기억은 없다."

            d "그래. 넌 기억 못 하지."

            d "아니, 기억 안 하려는 거겠지."

            $ stress += 5
            $ dios_trust -= 3

        "“…그게 진짜야?”":
            "낯익은 감정. 이상하게… 슬프다."

            d "그 눈빛, 봐. 아직도 날 이해하려고 하네."

            d "그래서 내가 널 아끼지."

            $ holiness += 2
            $ dios_trust += 3

        "침묵한다":
            "무언가 떠오를 듯 말 듯. 그 장면을 받아들이고 싶지 않다."

            d "그래, 침묵. 이건 네 방식이니까."

            d "그래도 괜찮아. 난 기억하니까."

            $ anxiety += 3
            $ dios_trust += 1

    "……무언가가 머릿속을 긁는다. 그가 말한 ‘처음’."

    scene bg_flashback with fade

    "짧은 회상—  "
    "피비린내, 낮은 조명, 그리고 …어린 목소리."

    d "넌, 날 처음으로 사람처럼 불렀어."

    scene bg_cell_dark with fade

    "회상이 끝났다. 하지만 남은 감정은 쉽게 지워지지 않는다."

    play sound "sfx/door_close.ogg"
    hide d_somber with dissolve

    "그가 떠났고, 당신은 아직도 그 순간 속에 있다."

    jump day16
