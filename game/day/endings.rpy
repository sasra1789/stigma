label ending_holiness:

scene bg_chapel_light with fade
stop music fadeout 2.0
play music "bgm/liberation.ogg"

"빛이 문 너머로 스며든다."

"당신은 천천히, 아주 천천히 그 안으로 걸어들어간다."

"누군가의 목소리도, 손길도 더는 필요하지 않다."

"이제, 자신을 용서할 수 있게 되었으니까."

"그리고… 신이 있다면, 그 앞에서도 고개를 들 수 있으니까."

"— 침묵 속에서 해방되다 —"

jump the_end

label ending_anxiety:

scene bg_cell_dark with fade
stop music fadeout 2.0
play music "bgm/despair.ogg"

"어둠은 더 짙어졌고, 숨소리는 그 안에서 질식한다."

"신도, 사랑도, 의미도 없다.  
남은 건 떨리는 손과, 부서진 신념뿐."

"그리고 그에게 조차—"

show d_stern at center with dissolve

d "……끝내 여기까지였네."

d "난 널 구해주고 싶었는데 말야. 아쉽군."

hide d_stern with moveoutright

"그의 발소리조차 멀어질 때— 당신은 아무 말도 할 수 없었다."

"— 침묵 속에서 파괴되다 —"

jump the_end

label ending_dependence:

scene bg_cell_warm with slow_dissolve
play music "bgm/ambiguous.ogg"

"이젠 아무것도 떠오르지 않는다. 오직 그만이 선명하다."

show d_smile at right with dissolve

d "봐, 역시 나 없인 안 되잖아."

d "신도 버렸고, 자존심도 내팽개쳤지."

d "근데 괜찮아. 난 네 그 비참한 얼굴이 좋거든."

"당신은 대답하지 않는다. 그저, 고개를 끄덕인다."

"그 순간, 방 안은 따뜻해졌지만— 해방은 아니었다."

"— 침묵 속에 길들여지다 —"

jump the_end


label ending_neutral:

scene bg_cell_neutral with fade
stop music fadeout 2.0
play music "bgm/neutrality.ogg"

"당신은 그를 받아들이지도, 거부하지도 않았다."

"신을 부르지도, 미치지도 않았다."

"그저, 오늘 하루를 또 버텼다."

show d at left with dissolve
d "……넌 여전히 재미있는 존재야."

hide d with dissolve

"그의 말도, 오늘의 공기처럼 흘러간다."

"그리고 내일이 오겠지. 또, 같은 하루가."

"— 침묵 속에서 버티다 —"

jump the_end


label the_end:
return
