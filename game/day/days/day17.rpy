label day_17:

    scene bg_cell_evening with fade
    "D17. 창문은 닫혀 있었지만, 빛은 들어왔다."

    "그는 오늘, 고해성사보다 먼저 나를 불렀다."

    scene bg_private_room
    show dios_neutral at right with dissolve

    d "오늘은 특별한 날이니까. 너랑 단둘이 얘기하고 싶어서."

    "그는 웃고 있었지만, 눈은 웃지 않았다."

    d "너도 알잖아. 이런 생활, 오래 하다 보면 정드는 법이야."

    d "도망치겠다고 발버둥치는 거, 솔직히 좀 지겹지 않냐?"

    d "그만해. 그냥… 여기서 살아."

    $ flag_surrender_offer = True

    menu:
        "……고개를 끄덕인다":
            $ dios_trust += 3
            d "봐. 결국은 순해지더라."
            d "이 방, 네가 원하면 열쇠도 줄 수 있어. 물론… 내가 쥐고 있긴 하겠지만."

        "무표정으로 거절한다":
            $ dios_trust -= 2
            $ stress += 2
            d "거절? 지금도 그게 네 선택이라고 믿어?"
            d "넌 내가 얼마나 너를 잘 아는지, 아직 모르는구나."

        "아무 말 없이 뒤돌아 선다":
            $ dios_trust -= 1
            $ anxiety += 2
            d "도망은 못 가. 애초에 네가 갈 곳은, 여기 말곤 없거든."

    "그는 문을 잠그지 않았다. 대신, 내가 나가지 않았다."

    jump confession_17
