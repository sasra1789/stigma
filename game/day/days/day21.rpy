label day21:

    scene bg_cell_dark with slow_dissolve
    show screen hud

    "기이하다."

    "언제나와 같은 방. 같은 공기. 같은 천장인데—"

    "무언가가 달라졌다."

    play sound "sfx/electronic_buzz.ogg"
    "…삐———익."

    "벽 너머에서 짧은 전자음이 들린다."

    "누군가가… 무언가를 켰다?"

    menu:
        "소리를 따라 벽에 귀를 댄다":
            "희미하게, 중얼거림. 기계음. 그리고… 네 이름?"

            $ anxiety += 5

        "기도문을 읊는다":
            "침착함을 유지하려 노력한다. 하지만 손이 떨린다."

            $ holiness += 3

        "소리의 존재를 무시한다":
            "아무 일도 일어나지 않았다. 아니, 일어나지 않은 것으로 하자."

            $ stress += 2
            $ anxiety -= 2

    "잠시 후, 발소리가 들려온다."

    play sound "sfx/footsteps_metal.ogg"

    show d_cold at left with moveinleft

    d "…들을 수 있었겠지. 일부러 크게 틀었거든."

    d "예의 없는 손님들이야. 네 감방에 들어와선 네 얘기를 하다니."

    "손님?"

    d "그들의 관심은 네가 얼마나 미쳤는지가 아니라…"

    d "—네가 아직 말하지 않았다는 점이야."

    menu:
        "“누구야…?”":
            d "관찰자. 감시자. 너의 침묵에 흥미를 가진 자들."

            d "그리고… 나를 시험하는 자들."

            $ anxiety += 4

        "“말하지 않았으니까, 살아있는 거야.”":
            d "정확히 그거지."

            d "넌 아직 그들의 기대를 배신하지 않았어."

            $ holiness += 2
            $ dios_trust += 2

        "“…넌 내 편이야?”":
            d "내가?"

            d "그럼, 누굴 위해 여기 있겠어. 너를 위해일까… 나를 위해일까."

            d "아니면, 그들에게 보여줄 하나의 결과물로서일까?"

            $ dios_trust -= 2

    "그가 다가온다. 아주 가까이. 숨결이 닿을 만큼."

    d "이해해, 나탈리아. 이곳에선 진실이란—"

    d "목소리를 내지 않는 자만이 가질 수 있는 사치야."

    play sound "sfx/door_close_heavy.ogg"
    hide d_cold with moveoutright

    "그가 떠난다."

    "하지만 이번엔… 정말로 혼자가 아니다."

    "천장의 어딘가에서, 미세한 기계음이 다시 들려온다."

    play sound "sfx/surveillance_beep.ogg"

    "『기록 개시. 대상 상태 이상 없음.』"

    $ anxiety += 5
    $ stress += 3

    jump day22
