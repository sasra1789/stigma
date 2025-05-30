label day22:

    scene bg_cell_dark with slow_dissolve
    show screen hud

    "…피곤하다."

    "아니, 이상하게 맥이 풀린다. 몸이 붕 뜬다."

    "지금이 아침인가? 밤인가? 감각이 조용히 녹아들고 있다."

    play sound "sfx/needle_inject.ogg"

    "팔에 미세한 자극. 순간, 눈이 번쩍 뜨인다."

    d "조금만 더 들춰보자. 네가 꼭꼭 숨긴 것들."

    d "이걸로, 넌 조금 더… 너 자신을 마주하게 될 거야."

    $ anxiety += 8
    $ stress += 10

    scene black with fade

    "숨이 막힌다. 아니, 가슴이 조인다."

    "어딘가 익숙한 어둠 속에서, 누군가의 숨결이 느껴진다."

    "『넌, 나를… 믿었었지.』"

    "그 목소리는 어릴 적, 작고 미성숙했던 디오스의 목소리와 닮아 있다."

    scene bg_flashback_chapel with dissolve

    "향이 짙은 성당. 무릎 꿇은 아이들."

    "기도보다 숨죽여 울던 시절. 그리고— 그가 있었다."

    show young_d at right with dissolve

    young_d "기억나?"

    young_d "내 손, 네가 자주 잡았었지."

    "아이였던 당신은 말없이 끄덕인다. 그 손은 지금과 달리… 따뜻했다."

    young_d "나는, 그런 네가 불편했어."

    young_d "왜냐면—"

    hide young_d with dissolve
    scene bg_cell_dark with flash

    show d_neutral at left with dissolve

    d "그 감정이 진짜였거든. 그때도 지금도."

    d "하지만 넌 항상 도망쳤어. 기도와 침묵 뒤로 숨었지."

    "몸이 천천히 일어난다. 결박은 풀려있지만… 스스로 일어설 힘이 없다."

    menu:
        "“그 손을, 믿었었어.”":
            d "그래. 그래서 더 끊기 힘들겠지."

            $ dios_trust += 5
            $ holiness += 2

        "“그 손이, 무서웠어.”":
            d "맞아. 그래서 날 더 지켜보게 됐겠지."

            $ stress += 3
            $ anxiety += 5

        "“…내가 착각한 거야.”":
            d "그런 생각을 할 줄 알았어. 그래서 회상을 유도한 거고."

            $ dios_trust -= 3
            $ anxiety += 3

    d "잘 생각해봐. 네가 봤던 그 순간들— 네가 만든 환상일까, 내가 남긴 진실일까."

    d "내일도, 계속 묻고 또 묻자. 언제까지든."

    play sound "sfx/door_close.ogg"
    hide d_neutral with moveoutright

    "그가 떠난다. 이번엔 아무 말도, 아무 행동도 하지 않는다."

    "그러나 그 침묵이, 가장 크고 무거운 대답처럼 느껴졌다."

    jump day23
