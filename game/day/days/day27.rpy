label day27:

    scene bg_cell_dark with dissolve
    show screen hud

    "아무것도 오지 않는다."

    "몇 시간째, 침묵만이 방을 채운다."

    "희망도, 절망도 고갈된 자리엔… 감각의 파편만이 남는다."

    play sound "sfx/static_noise.ogg"
    "귀가 멍하다. 무언가 들리는 것도 같고… 아닌 것도 같다."

    "『나탈리아』"

    pause(1.0)

    "『……』"

    "그 목소리는 익숙하면서 낯설다. d가 아니다. 하지만 이 공간과 너무 닮아 있다."

    menu:
        "눈을 감는다":
            "더는 보고 싶지 않다. 그가, 이 방이, 나 자신이."
            $ stress += 3
            $ anxiety += 5

        "기도를 올린다":
            "이럴 땐 신을… 아니, 아무 대상이라도 붙잡고 싶다."
            $ holiness += 5

        "그 목소리를 따라간다":
            "정신의 깊은 곳, 혼돈의 구멍을 들여다본다."
            $ dios_trust += 3
            $ anxiety += 7

    "『...넌 누구를 원하지?』"

    "『신이야? 아니면, d?』"

    show d_close at center with dissolve

    d "흠. 꽤 몰입했네. 혼잣말까지."

    d "그만 좀 깨어나. 나탈리아."

    d "신은 널 버렸고, 나는... 네가 더럽혀질 때까지 기다려줄 뿐이야."

    "그는 무릎을 꿇은 내 앞에 앉아, 고개를 기울인다."

    d "넌 점점 더 날 닮아가고 있어."

    d "축하해, 나탈리."

    hide d_close with moveoutbottom
    play sound "sfx/heartbeat.ogg"

    "심장이 다시 뛴다. 하지만 그것은 두려움이 아니라… 분노였다."

    $ stress += 3
    $ dios_trust -= 2

    jump day28
