label day30:

    scene bg_cell_dark with slow_dissolve
    show screen hud

    "30일째 아침. 이곳의 공기는 어제와 다르다."

    "당신도 안다. 오늘이 마지막이라는 것을."

    play sound "sfx/heartbeat.ogg" loop
    pause(2.0)

    "마음은 고요하지만, 몸은 떨린다.  이 문이 오늘은 열린다는 걸, 본능이 알고 있다."

    show d_neutral at center with dissolve

    d "아직도 안 부서졌네. 대단한 끈질김이야."

    d "…그러니까 말이지, 애송이.  이젠 진심으로 너만 보면 웃음이 나와."

    d "넌 도망도 못 치고, 부서지지도 않아.  내 손에만 남아버렸단 소리잖아?"


    d "자, 선택의 시간이다. 나탈리아."

    menu:
        "나는 신을 선택한다":
            "그것만이 유일하게 남은 길이다."

            if holiness >= 70:
                jump ending_holiness
            else:
                jump ending_half_faith

        "나는 너를 믿는다":
            "도무지 믿고 싶지 않은데… 그래도 네가 남는다."

            if dios_trust >= 70:
                jump ending_dios
            else:
                jump ending_broken_trust

        "나는 내 안의 불안을 따른다":
            "이 모든 것이 끝나길 원한다. 어떤 방식이든."

            if anxiety >= 70:
                jump ending_fall
            else:
                jump ending_survive

 # 안전망
jump ending_neutral
