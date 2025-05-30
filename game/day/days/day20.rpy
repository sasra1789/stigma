label day20:

    scene bg_cell_dark with slow_dissolve
    show screen hud

    "밤은 조용하다."

    "하지만 오늘은 유독 잠들 수 없다."

    "눈을 감자, 오래된 장면이 떠오른다—"

    scene bg_flashback_chapel with fade
    play music "bgm/chapel_memories.ogg" fadein 1.0

    "—당신이 수도원으로 들어온 첫날."

    "신은 낯설고, 냉정했고… 그보다 사람들은 더 그랬다."

    "그 안에서 단 한 사람, 당신에게 말 걸어준 사람은—"

    show d_young at center with dissolve

    d "겁내지 마. 여긴 짖는 개도, 독 묻은 잔도 없어."

    "그의 말은 이상했다. 하지만 그것이 위로가 됐다."

    menu:
        "그때의 d를 떠올린다":
            "그의 눈은 지금보다 훨씬… 따뜻했다."

            $ dios_trust += 3

        "기억을 부정한다":
            "그 기억은 조작된 것이다. 감정은, 너의 적이다."

            $ anxiety += 5
            $ dios_trust -= 2

        "눈을 감는다":
            "과거는 과거일 뿐이다. 지금은 지금이다."

            $ holiness += 3
            $ stress -= 2

    scene bg_cell_dark with fade
    stop music fadeout 1.0

    "다시 감방."

    "그리고—"

    play sound "sfx/door_open.ogg"
    show d_silent at right with dissolve

    d "기도는 끝났어?"

    d "아니면 이제야 시작이려나."

    "그가 말을 걸어올 때, 당신의 입술은—"

    menu:
        "“왜 나를 구했어?”":
            d "…그러니까 네가 도망치지 못하게."

            d "살게 해야 지옥을 알지. 죽여선 아무것도 몰라."

            $ anxiety += 3
            $ dios_trust += 1

        "“다신 믿지 않아.”":
            d "누굴? 신을? 나를? 네 자신을?"

            d "그래. 그 중 하나라도 믿지 않으면, 덜 아프지."

            $ holiness -= 3
            $ dios_trust -= 2

        "“오늘은 그냥… 조용히 있어줘.”":
            "그는 말없이 곁에 앉았다."

            d "…드물게 이기적이네. 하지만 괜찮아."

            $ dios_trust += 4
            $ stress -= 3

    hide d_silent with dissolve

    "그는 그저 문을 열고, 닫고, 사라졌다."

    "그의 발소리조차 들리지 않는다."

    jump day21
