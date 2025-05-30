label day7_holiness_route:

    scene bg_white_glow with fade
    play sound "sfx/angelic_voice.ogg"

    "빛은 점점 선명해졌다. 더는 환상이라 말할 수 없을 만큼."

    narrator "너는 두려움을 넘었다. 하지만 아직은, 절반이다."

    "낮은 음성이 다시 들린다. 마치 어릴 적 누군가의 품 같은 감각."

    narrator "그를 증오하지 마라. 그 또한 나의 도구였다."

    menu:
        "그를… 용서하라는 겁니까?":
            narrator "용서는 그를 위한 것이 아니다. 너를 위한 것이다."
            $ holiness += 5

        "전 아직… 용서할 수 없습니다.":
            narrator "그러면 더 오래 머물러야 하리라. 침묵 안에."
            $ stress += 5

    "그 말이 끝나자 방이 다시 어둠으로 접힌다."

    scene bg_cell_dim with dissolve
    "빛은 사라졌다. 하지만 마음속엔 그 흔적이 남았다."

    jump day8


label day7_dios_route:

    scene bg_cell_warm with dissolve
    show d_soft at left with dissolve

    d "내가 무슨 말을 해도 넌 나를 의심하지."

    d "그런데도, 내가 매일 너한테 오고 있다는 건… 뭘까?"

    "그의 눈빛이 흔들린다. 처음으로 그가 당신을 피한다."

    menu:
        "……내가 익숙해진 걸까. 네가 아니라 이 감옥에.":
            d "……그 말, 왜 이렇게 아프냐."
            $ dios_trust += 5
            $ stress -= 5

        "착각하지 마. 넌 여전히 나를 가두고 있어.":
            d "그래. 널 놓아줄 생각은 없어."
            $ dios_trust -= 3
            $ anxiety += 5

    d "다만, 너는… 내가 처음으로 두려워한 존재일지도 모르지."

    hide d_soft with fade
    "그의 말은 농담 같았지만, 농담처럼 들리지 않았다."

    jump day8

label day7_anxiety_route:

    scene bg_cell_distorted with hpunch
    play sound "sfx/mind_break.ogg"

    "현실이 끊긴다. 선과 선 사이, 말과 말 사이에서 목소리가 새어나온다."

    "『신은 널 버렸다』"

    "『너는 실패작이야』"

    "『그는 널 사랑한 적 없어』"

    menu:
        "귀를 막는다":
            "손가락 사이로 피가 흐른다. 그래도 멈출 수 없다."
            $ anxiety += 5

        "소리를 따라간다":
            "발소리. 없던 문. 하얀 복도. 눈부신 방."
            $ holiness += 5
            $ stress += 5

        "몸을 벽에 부딪힌다":
            "모서리의 냉기만이 현실감을 되살린다."
            $ stress += 10

    "그 모든 소음이 멈췄을 때, 당신은 바닥에 쓰러져 있었다."

    jump day8

label day7_neutral_route:

    scene bg_cell_dark with dissolve
    show d_neutral at left with moveinleft

    d "오늘은 아무 말도 하지 않네."

    d "근데 있잖아… 널 이렇게 지켜보는 것도 은근히 중독적이야."

    menu:
        "……그만 좀 해. 이건 고문이야.":
            d "그래, 고문 맞아. 네 감정이 나한테 전염되는 기분."
            $ anxiety += 5

        "네가 즐기고 있는 거 알아.":
            d "응. 인정. 네가 무너지는 걸 보는 게… 이상하게 끌려."
            $ dios_trust += 3

    "그는 무슨 말을 하든 감정이 없는 듯 보인다. 하지만 어쩌면… 너무 많아서 감추는 걸지도."

    jump day8