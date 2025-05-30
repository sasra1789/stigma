label day5:

    scene bg_cell_dark with slow_dissolve

    show screen hud

    "숨이 가쁘다."

    "아무것도 하지 않았지만, 머릿속이 떠다니는 듯 어지럽다."

    "기억인가, 환상인가. 어제 d의 말이 계속 맴돈다."

    play sound "sfx/heartbeat.ogg" fadein 1.0

    "『넌 절대 자유로워질 수 없어, 나탈리아』"

    if stress >= 60 or anxiety >= 60:
        "그 문장이 뼛속을 긁는다. 무언가가 안에서 부서지고 있다."

    else:
        "그 말이 싫지는 않았다. 이상하리만큼… 현실적으로 들렸다."

    pause(1.0)

    play sound "sfx/door_open.ogg"
    show d_stern at left with moveinleft

    d "그래서? 오늘은 어떤 얼굴일까."

    d "신의 노예? 아니면 나한테 길들여진 강아지?"

    "그의 말이 너무도 가볍고, 가증스럽게 들린다."

    menu:
        "처음으로 소리친다":
            "목이 갈라질 듯 아픈 소리가 튀어나온다."
            nvl clear
            nvl window
            narrator "그만—"
            nvl hide
            d "……"

            d "드디어 목소리를 들었군. 이 얼마나 감동적인 날인가."

            $ stress -= 10
            $ anxiety += 5
            $ dios_trust += 3

        "신을 부른다":
            "조용히 속삭인다. 짧은 기도. 떨리는 손끝."
            d "하… 아직도? 대단해. 그 바닥에서 아직 신을 찾아?"
            $ holiness += 5
            $ dios_trust -= 1

        "아무 말도 하지 않는다":
            "그러나 침묵은 더 이상 방패가 아니다. 지금은… 도피에 가깝다."
            d "뭐야, 말할 줄도 모르는 인형이야?"

            if anxiety >= 70:
                d "……혹시 울고 있는 건 아니지?"
                $ stress += 5
                $ dios_trust -= 3
            else:
                d "그래, 언제나처럼. 고요하고 무의미하게."

    d "기억해. 말하는 순간, 너는 더 이상 침묵의 신앙 안에 있지 않아."

    d "하지만 난… 네 침묵조차 듣는 법을 배웠거든."

    play sound "sfx/door_close.ogg"
    hide d_stern with moveoutright

    "그가 떠났다. 이번엔 문을 꽝 닫지도 않았다."

    "당신의 심장만이 여전히 문 앞에서 맥을 놓지 못한 채 뛰고 있다."

    ## ✅ Day 6 분기 진입
    if holiness >= 80:
        jump day6_holiness_route
    elif dios_trust >= 70:
        jump day6_dios_trust_route
    elif anxiety >= 80:
        jump day6_anxiety_route
    else:
        jump day6_neutral_route
