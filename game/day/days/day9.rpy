label day9:

    scene bg_cell_dark with dissolve

    show screen hud

    "물컵조차 없는 이 방에서, 당신은 ‘거울’을 떠올린다."

    "내가 지금 무슨 표정을 짓고 있을까?"

    if holiness >= 90:
        "기도 중의 얼굴은 평온했을 것이다. 적어도… 그들은 그렇게 말했다."
    elif dios_trust >= 90:
        "그는 가끔 당신을 쳐다보며 웃는다. 거기엔 무언가 묘한 애정이 섞여 있다."
    elif anxiety >= 90:
        "거울이 있다면, 보고 싶지 않았을 것이다. 무너져가는 얼굴, 터지기 직전의 껍질."
    else:
        "그저 무표정한 얼굴. 익숙해진 감정 없는 껍데기."

    "누군가의 눈에 나는 어떤 모습일까?"

    play sound "sfx/door_open.ogg"
    show d_neutral at left with moveinleft

    d "오늘은… 그냥 잠깐 들렀어."

    "그는 말을 아꼈다. 손도 주머니에 넣은 채, 눈을 피했다."

    d "사람이 거울을 보면… 원래보다 초라해 보인대. 왜 그런지 알아?"

    menu:
        "자신이 뭔지 아니까.":
            d "맞아. 넌 이제 스스로를 제대로 보기 시작했겠지."
            $ stress += 3

        "난 아직도 내가 누군지 모르겠어.":
            d "좋아. 그럼 네가 누군지 알려줄게. 천천히."
            $ dios_trust += 5

        "거울 따위 필요 없어. 난 끝까지 나야.":
            d "강하네. 그럼 부숴보자고, 네가 말하는 그 ‘나’라는 거."
            $ holiness += 3
            $ anxiety -= 2

    "그는 오늘도 오래 머무르지 않았다."

    d "조만간, 진짜 거울을 보여줄게. 거기 비친 널… 넌 견딜 수 있을까?"

    hide d_neutral with dissolve
    play sound "sfx/door_close.ogg"

    "그의 발소리는 작았다. 하지만 오늘따라 그 그림자가 길게 남았다."

    if stress >= 80 and anxiety >= 80:
        "당신은 무너지고 싶었다. 무너져서, 모든 걸 내려놓고 싶었다."
    elif holiness >= 90:
        "그러나 신은 무너지지 않는다 했다. 빛이 있는 한, 당신도 그 일부다."
    elif dios_trust >= 90:
        "…혹시. 그가 내게 진심이라면?"

    jump day10
