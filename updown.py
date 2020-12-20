from random import *

try:
    print("------------업다운 게임------------")
    print("난이도를 선택하세요")
    print("1:쉬움(1~50) 2:보통(1~100) 3:어려움(1~200) 4:커스텀")
    c = int(input())
    if c==4:
        global e
        print("1부터 몇 까지?")
        e = int(input())

    b = randrange(1, 51) if c == 1 else randrange(1, 101) if c == 2 else randrange(1, 201) if c==3 else randrange(1, e)
    d = 50 if c==1 else 100 if c==2 else 200 if c==3 else e
    cnt = 0
    while True:
        cnt += 1
        print("1부터 {0}까지 숫자 중 하나를 입력하세요({1}번째 도전)".format(str(d), str(cnt)))
        a = int(input())
        print("Up" if a<b else "Down" if a>b else "정답!\n{0}번 만에 맞췄습니다".format(str(cnt)))
        if a == b:
            break
except ValueError:
    print("숫자만 입력해주세요!")
