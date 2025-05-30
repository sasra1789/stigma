label day12:

    scene bg_cell_static with dissolve

    show screen hud

    "기억은 아직도 남아 있다. 꿈에서 본 그 장면."

    "하지만 오늘은—"

    play sound "sfx/door_open.ogg"
    show d_stern at left with dissolve

    "그가 들어왔다. 아무 말도 하지 않고."

    "눈빛도, 표정도, 말투도. 아무것도 없다. 그냥, 보고만 있다."

    if dios_trust >= 90:
        "그의 침묵이 낯설었다. 늘 말이 많았던 사람이었는데. 뭔가 이상했다."
    elif anxiety >= 90:
        "침묵은 더 무서웠다. 차라리 비웃어주지. 이건… 예고 없는 폭력 같았다."
    elif holiness >= 90:
        "그 침묵 속에서 신의 음성을 찾으려 했다. 어쩌면 이것도 신의 시련일까?"
    else:
        "무표정한 얼굴. 나를 본다. 마치 내가 숨도 쉬지 않기를 바라는 듯."

    "그래서 당신은 선택한다."

    menu:
        "혼잣말을 꺼낸다":
            "‘오늘은 왜 말 안 해?’"
            "그는 반응하지 않았다. 하지만, 눈빛이 살짝 흔들렸다."
            $ dios_trust += 2

        "그를 응시한다. 아무 말도 하지 않은 채.":
            "어느 쪽이 먼저 피할까? 이건 침묵 속의 대결이었다."
            $ stress += 3

        "속으로 기도한다":
            "‘이 사람의 침묵조차 내게 해답이 되게 하소서.’"
            $ holiness += 5

    "결국, 그는 아무 말 없이 돌아섰다."

    play sound "sfx/door_close.ogg"
    hide d_stern with dissolve

    "그의 침묵은 말보다 더 많은 것을 남겼다."

    jump day13
