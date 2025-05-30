label day26:

    scene bg_cell_light with slow_dissolve
    show screen hud

    "그날 이후, 매일 같은 시간."

    "그 손은 구멍 너머로 다가왔다."

    "어떤 날은 온기를 전했고, 어떤 날은 손글씨가 담긴 종이 조각을 건넸다."

    "무의미한 낙서. 꽃의 그림. 종교 문장. 때로는 이름 없는 위로."

    menu:
        "그 손을 기다린다":
            "어느새 시간이 다가오면 가슴이 뛴다. 말은 없지만, 이건 기도다."
            $ holiness += 2
            $ anxiety -= 3

        "이름을 물어본다":
            "문 너머에 대고 속삭인다. '당신은 누구죠?'"
            "하지만 돌아오는 건… 더 조용한 침묵뿐이다."
            $ dios_trust -= 1

        "더 이상 받지 않는다":
            "이건 d의 조작일지도 모른다. 일종의 실험. 신뢰는 약점이다."
            $ anxiety += 5
            $ stress += 3

    "그리고 오늘—"

    play sound "sfx/door_open.ogg"
    show d_suspicious at left with moveinleft

    d "재밌는 걸 보고 있더군."

    d "네가 받던 그 종이. 꽤… 감상적이던데?"

    "그는 구멍을 들여다보며 조용히 웃는다. 차갑고, 천천히."

    d "이 감방에서 시詩를 주고받는 건 처음 보네."

    d "그 손, 오늘은 잘랐어."

    pause(1.5)

    "……."

    d "너도 이제 알겠지. 구멍은 출구가 아니야."

    d "넌 다시, 여기 있어."

    hide d_suspicious with moveoutleft
    play sound "sfx/door_close.ogg"

    "어딘가서 핏물이 번진 종이 조각 하나가 구멍을 통해 밀려왔다."

    "이젠, 아무것도 오지 않겠지."

    $ stress += 5
    $ anxiety += 5

    jump day27
