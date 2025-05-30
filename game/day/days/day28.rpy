label day28:

    scene bg_cell_dark with fade
    show screen hud

    "문이 열리지 않는다."

    "정해진 시간에 식사도, 감시도, d도 오지 않는다."

    "…처음이다."

    "『넌 아직도 날 기다리고 있었니?』"

    "『아님, 그가 네 모든 삶이 된 거야?』"

    "머릿속에서 무언가가 소용돌이친다."

    menu:
        "문을 두드린다":
            "거칠게 손이 움직인다. 더는 조용히 숨고 싶지 않다."
            $ stress -= 5
            $ dios_trust -= 2

        "기도문을 외운다":
            "짧게, 하지만 분명하게. 신은 멀지만 아직 닿는다."
            $ holiness += 3
            $ anxiety -= 2

        "가만히 앉아 생각한다":
            "내 안의 소리를 처음으로 정면으로 바라본다."
            $ dios_trust += 2
            $ anxiety += 1

    "몇 시간 후—"

    play sound "sfx/door_unlock.ogg"
    show d_tired at left with moveinleft

    d "그래. 넌 여전히 살아 있구나."

    d "나는 네가 며칠쯤은… 바닥에서 숨죽이고 있을 줄 알았는데."

    "그의 얼굴에는 약간의 피로, 그리고 미세한 당혹감이 섞여 있다."

    menu:
        "그를 노려본다":
            "입을 열지 않아도, 눈으로 충분히 전할 수 있다."
            $ dios_trust -= 2
            $ stress -= 1

        "그의 말에 대꾸한다":
            "지금껏 미뤄왔던 한 마디. 이제는 말할 수 있다."
            nvl clear
            window hide
            narrator "나는... 네가 싫어."
            nvl hide
            d "오, 드디어 혀를 움직였네."

            d "그 감정, 부디 더 키워줘. 사랑보다 이런 게 훨씬 자극적이니까."

            $ dios_trust += 3
            $ anxiety += 2

        "다시 침묵한다":
            "그러나 이번엔, 피하지 않기 위한 침묵이다."
            d "좋아. 그 침묵, 이제 네 방식으로 쓰고 있군."

            $ dios_trust += 1
            $ holiness += 1

    hide d_tired with moveoutright
    play sound "sfx/door_close.ogg"

    "오늘의 침묵은 다르다.  
    …내 것이었다."

    jump day29
