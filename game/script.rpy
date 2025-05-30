# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
# 스탯 정의
# 스탯 초기화
default day = 1
default holiness = 0
default stress = 0
default anxiety = 0
default dios_trust = 5

label start:

    scene black
    with fade

    "당신에게 주어진 유예는 단 30일..."

    jump day_loop



# 루프를 하지말고,, 이런 류의 게임은 D30일 을 모두 개별의 label 로 작성하여 각각 다르게 표현해도 좋을듯
label day_loop:

    scene bg_cell_day
    with fade

    "Day [day]. 오늘 하루, 어떤 활동을 하시겠습니까?"

    menu:
        "기도한다":
            $ holiness += 2
            $ stress = max(0, stress - 1)
            "나탈리아는 긴 시간 동안 침묵 속에서 기도에 집중했다."

        "정원 노동":
            $ stress += 1
            $ dios_trust += 1
            "디오스는 나탈리아의 성실함에 만족한 듯 보였다."

        "혼자 정찰한다":
            $ anxiety += 2
            $ dios_trust = max(0, dios_trust - 2)
            "수도원 뒤편은 감시가 심했다..."

    jump confession


label confession:

    scene bg_confession
    show dios_neutral at right
    with fade

    "밤이 되었다. 고해성사의 시간이다."

    "오늘 하루, 무엇을 했는지 말해보지."

    menu:
        "진실을 말한다":
            if dios_trust >= 5:
                "디오스는 조용히 고개를 끄덕였다."
                $ holiness += 1
            else:
                "디오스의 눈빛이 날카로워진다."
                $ stress += 2

        "거짓말을 한다":
            if holiness >= 3:
                "당신의 눈빛에 디오스는 속았다."
                $ stress = max(0, stress - 1)
            else:
                "거짓말이 들통 났다. 디오스는 조용히 미소 지었다."
                $ anxiety += 2
                $ dios_trust = max(0, dios_trust - 1)

        "침묵한다":
            "긴 침묵이 흘렀다. 디오스는 무언가를 메모했다."
            $ dios_trust = max(0, dios_trust - 1)
            $ anxiety += 1

    "그날 밤, 나탈리아는 기도하며 잠들었다..."

    # 날짜 증가 및 루프
    if day >= 30:
        jump ending_select
    else:
        $ day += 1
        jump day_loop


# 엔딩 분기

label ending_select:

    scene black
    with fade

    "30일이 지났다..."

    if holiness >= 10 and dios_trust <= 2:
        jump ending_escape

    elif anxiety >= 10:
        jump ending_mind_break

    elif dios_trust >= 10:
        jump ending_submission

    else:
        jump ending_normal


label ending_escape:

    scene bg_forest_night
    with slow_dissolve

    "당신은 끝내 자유를 되찾았다. 신의 은총이 함께했음을 믿으며."

    jump real_end


label ending_mind_break:

    scene bg_cell_dark
    with slow_dissolve

    "정신은 무너졌고, 당신은 그의 손 안에서 길들여졌다."

    jump real_end


label ending_submission:

    scene bg_chapel
    with slow_dissolve

    "당신은 더 이상 도망치지 않았다. 그와 함께 이곳에 남기로 했다."

    jump real_end


label ending_normal:

    scene bg_cell_evening
    with slow_dissolve

    "그 누구도 구원받지 못했다. 그러나 당신은 여전히 살아 있다."

    jump real_end

label real_end:
    return