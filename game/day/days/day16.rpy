label day16:

    scene bg_cell_dark with dissolve
    show screen hud

    "머리가 계속 아프다."

    "어제 본 기억은 꿈이었을까? 하지만 감정은 선명하다."

    play sound "sfx/heartbeat.ogg"

    "『넌, 날 처음으로 사람처럼 불렀어.』"

    "그 말이 자꾸 되새겨진다. 왜 그랬을까. 내가 왜—"

    show d_silent at left with dissolve

    d "조용하네. …그 기억이 돌아온 건가."

    d "그래서 묻자. 내가 널 그때 죽였다면… 지금 너는 더 나았을까?"

    menu:
        "“죽었어야 했어.”":
            d "그럼… 다음에 기회가 오면 그래 줄까?"

            $ stress += 10
            $ dios_trust -= 5

        "“몰라.”":
            d "응, 그게 네 진심이겠지."

            $ anxiety += 3

        "“살고 싶었어.”":
            d "그래… 그 눈빛이 거짓이 아니었다면, 널 살게 한 게 맞을지도."

            $ dios_trust += 3

    hide d_silent with moveoutleft

    "그가 남긴 말은 흔적처럼 마음을 긁었다."

    jump day17
