#day6
"""
 감정수치에 따라 명확하게 분기되는 첫날 
이제까지의 Day 1~5는 "누가 주도권을 쥐고 있는가?"에 대한 시험이었다면,
Day 6부터는 d와 나탈리아의 관계가 갈라지는 분기점이 돼.
"""

label day6_holiness_route:

    scene bg_light_bloom with fade

    play sound "sfx/whisper_heaven.ogg"

    "눈을 감았을 뿐인데, 빛이 눈앞을 가른다."

    "어디선가 들려오는 목소리."

    narrator "…들리느냐, 나탈리아."

    "기도는 더 이상 혼잣말이 아니었다."

    narrator "네가 잊지 않았다면, 우리는 항상 함께였다."

    "그 순간, 손끝이 따뜻해진다. 방 안의 공기가 달라졌다."

    $ holiness += 10

    jump day7_holiness_route

label day6_dios_trust_route:

    scene bg_cell_dim with dissolve

    show d_soft at left with moveinleft

    d "오늘은, 그냥 보러 왔다."

    "그는 의자에 앉지 않는다. 그냥 그 자리에 선 채로, 당신을 바라본다."

    d "나는 네가 여기 있어줘서... 다행이라고 생각해."

    menu:
        "……왜 그런 말을 해?":
            d "글쎄. 나도 몰라. 그냥 네가 없으면 이 방이 너무 조용할 것 같아서."

        "아무 말도 하지 않는다":
            d "봐. 너랑 있는 시간이 편해지는 거 같기도 하고."

    $ dios_trust += 5

    "이 감정은… 착각일까, 아니면 유일한 온기일까?"

    jump day7_dios_route

label day6_anxiety_route:

    scene bg_cell_blur with vpunch

    play sound "sfx/heartbeat_fast.ogg" fadein 0.5

    "숨이 차다."

    "귀에서 울리는 맥박 소리가 모든 소리를 집어삼킨다."

    "세상이 뿌옇게 흔들리고, d의 말이 머릿속을 맴돈다."

    "『절대 자유로워질 수 없어』"

    menu:
        "제발 그만…!":
            "비명이 터져나온다. 아무도 없는데도."
            $ stress += 5

        "벽에 머리를 박는다":
            "통증조차 무의미하다."
            $ anxiety += 5

    "당신은 무너지고 있었다."

    jump day7_anxiety_route

label day6_neutral_route:

    scene bg_cell_dark with dissolve

    show d_neutral at left with moveinleft

    d "별일 없지?"

    "그의 말투는 어제와 다르지 않다. 하지만 당신의 침묵도 변함없다."

    d "좋아. 그게 너니까."

    "그는 더는 묻지 않는다. 더는 다그치지 않는다."

    "이 침묵 속에서, 서로는 서로를 조금씩 갉아먹는다."

    jump day7_neutral_route
