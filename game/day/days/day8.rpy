label day8:

    scene bg_cell_dim with dissolve

    show screen hud

    "밤은 유난히 길었다."

    "창문도 없고, 시계도 없는 이곳에서 '밤'이라는 말은 어울리지 않지만…"

    "당신은 지금, '어두운' 상태에 있다는 사실만은 분명했다."

    if anxiety >= 80:
        "숨소리가 일정하지 않다. 손끝이 저릿하고, 벽의 무늬가 움직이는 것만 같다."
    elif holiness >= 80:
        "기도를 멈출 수 없다. 고요 속의 목소리가 이제는 확실히 들린다."
    elif dios_trust >= 80:
        "그가 오기 전부터, 그의 발소리를 상상한다. 어느새 익숙해진 습관."
    else:
        "침묵. 아무것도 바뀌지 않은 이 방. 그리고 당신의 호흡."

    pause(1.0)

    play sound "sfx/door_open.ogg"
    show d_neutral at left with moveinleft

    d "여기 있었구나."

    menu:
        "넌 늘 이렇게 찾아오지.":
            d "그래. 네가 나를 잊지 않도록 말이지."
            $ dios_trust += 3

        "오늘은 말하지 않을 거야.":
            d "그게 너답지. 하지만 재밌는 건, 그 침묵이 더 크게 들린다는 거지."
            $ stress += 3

        "…난 이제 지쳤어.":
            d "그래도 아직은 말할 수 있네. 그럼 넌 아직 무너지지 않았다는 뜻이야."
            $ anxiety -= 5
            $ dios_trust += 2

    "그는 오늘은 오래 머무르지 않았다."

    d "곧… 결정을 해야겠지. 신에게 기도할지, 나에게 기댈지, 아니면 그냥 무너질지."

    hide d_neutral with dissolve
    play sound "sfx/door_close.ogg"

    "그가 남긴 말이 벽처럼 남았다."

    if stress >= 80:
        "그 말이 끝나자마자, 당신은 조용히 눈을 감았다. 심장이 작게 떨렸다."
    elif holiness >= 85:
        "그의 말은 중요하지 않았다. 당신은 이미 결심했다. 신은 여기 있다."
    elif dios_trust >= 85:
        "그의 말은… 어딘가 다정했다. 무서웠다. 하지만… 따뜻했다."

    jump day9
