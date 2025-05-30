label day29:

    scene bg_cell_light with dissolve
    show screen hud

    "창문은 없지만, 빛은 들어온다."

    "몇 주째 반복되던 이 감옥 같은 생활. 그런데 오늘은… 미세한 균열이 느껴진다."

    menu:
        "침대를 옮겨 벽을 두드린다":
            "무의식 중에 반복된 행동. 탈출이 가능할지도 모른다는 착각."
            $ stress -= 2
            $ anxiety += 2

        "기도문에 이탈리아어를 섞어본다":
            "누가 들을 리 없지만, 언젠가 닿을지도 모른다는 미련."
            $ holiness += 3
            $ dios_trust -= 1

        "기록을 남긴다":
            "손톱으로 바닥에 선을 긋는다. 날짜도 아니고 말도 아니다. 단지 존재의 흔적."
            $ stress -= 1
            $ holiness += 1

    play sound "sfx/door_open.ogg"
    show d_cold at left with moveinleft

    d "그렇게 벽을 긁는 건 무슨 주술이야?"

    d "혹시 탈출구라도 찾았어?"

    "그는 웃고 있었지만, 눈동자는 경계하고 있었다."

    menu:
        "반격하듯 웃는다":
            "미소로 무장한다. 절망은 사치고, 비웃음은 방패다."
            d "좋아, 드디어 우리 대화가 좀 더 흥미로워졌군."

            $ dios_trust += 3
            $ anxiety -= 2

        "침묵한다":
            "그의 의심이 커지길 바란다. 거짓은 침묵보다 덜 효과적이니까."
            d "그래. 그런 눈빛이 나를 더 경계하게 만들어."

            $ dios_trust -= 1
            $ holiness += 2

        "탈출하겠다고 말한다":
            "순간, 나도 놀랐다. 그런 말을 내가 꺼낼 줄이야."
            d "하… 정말로? 그 입에서 '탈출'이라는 말이 나올 줄은."

            d "기대할게. 누가 더 오래 버티는지."

            $ dios_trust += 5
            $ anxiety += 3
            $ stress -= 5

    hide d_cold with moveoutright
    play sound "sfx/door_close.ogg"

    "남은 시간은 하루.  
    내일이면, 이곳에서의 유예도 끝이다."

    jump day30
