label day10:

    scene bg_cell_softlight with dissolve

    show screen hud

    "벽에 기댄 채, 창문도 없는 방 안에서 아침이라는 단어를 되뇌인다."

    "‘아침’이라는 이름조차 어울리지 않는 이곳."

    "그런데 문득, 누군가가 말한다."

    play sound "sfx/door_open.ogg"
    show d_soft at left with dissolve

    d "나탈리아."

    pause(0.5)

    "그가 처음으로 이름을 불렀다."

    if dios_trust >= 85:
        "그 목소리는 부드러웠다. 마치 오래된 기억 속의 누군가처럼."
    elif anxiety >= 85:
        "그가 내 이름을 부르는 순간, 온몸이 얼어붙었다. 그 이름은 족쇄였다."
    elif holiness >= 85:
        "그의 입에서 내 이름이 나왔을 때, 신의 이름이 더 선명해졌다."
    else:
        "낯설었다. 그는 항상 ‘너’ 혹은 ‘꼬맹이’라고 불렀다. 이상했다."

    d "그 이름을, 아직도 너 자신이라고 믿고 있어?"

    menu:
        "나는 나야. 아직은.":
            d "그래. 그건 꽤 끈질긴 말이지."
            $ stress -= 5

        "그 이름은, 누가 지은 거지?":
            d "네가 스스로 부여한 게 아니었단 걸 이제야 깨닫는 건가."
            $ anxiety += 5

        "그 이름, 이제는 낯설어.":
            d "그럼 네가 남은 건 뭐지? 기도? 침묵? 나?"
            $ holiness -= 2
            $ dios_trust += 2

    "그는 당신을 오래 보지 않았다. 단지… 이름을 부르고 떠났다."

    play sound "sfx/door_close.ogg"
    hide d_soft with dissolve

    "오늘, 당신은 다시 이름을 곱씹는다."

    "그 이름 속에 나라는 사람이 남아 있을까?"

    jump day11
