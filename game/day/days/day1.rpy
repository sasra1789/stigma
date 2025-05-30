label day1:

    scene bg_cell_dark with slow_dissolve

    show screen hud

    "......"
    "당신은 어두운 방 안에서 깨어난다."

    "얼마나 지났을까. 시간이란 개념은 이곳에 없다."

    "손목엔 여전히 가죽 끈이 느슨하게 감겨 있다."
    "도망치려는 의지는 진즉 사라졌고, 이젠 기다리는 자의 자세만이 남아 있다."

    $ stress += 5
    $ anxiety += 10

    "철문 너머로 발소리가 들린다."

    play sound "sfx/door_open.ogg"
    show dios_neutral at left with moveinleft

    d "잘 잤나, 꼬마?"

    "그 목소리. 그 표정. 잊고 싶어도 잊히지 않는 사람."

    menu:
        "침묵한다":
            "그는 당신의 침묵에 익숙한 듯, 그저 웃는다."
            $ dios_trust += 2
            $ stress += 5

        "눈을 피한다":
            "시선을 피하자 그가 한 걸음 다가온다."
            $ anxiety += 5
            $ dios_trust -= 2

        "기도를 읊조린다":
            "속삭이는 기도가 방 안을 메운다."
            dios "아직도 신을 찾는군."
            $ holiness += 5
            $ dios_trust += 1

    d "첫날이군. 앞으로 30일. 네가 뭘 택할지 지켜보도록 하지."

    hide dios_neutral with moveoutright
    play sound "sfx/door_close.ogg"

    "그는 떠났다. 하지만 그의 그림자는 방 안에 남아 있다."

    "그리고 당신은 다시 혼자가 된다."

    jump day2
