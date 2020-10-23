from random import *

print("업다운 게임")

b = randrange(1, 101)
cnt = 0
while True:
    a = int(input("1부터 100까지 숫자 중 하나를 입력하세요"))
    if a < b:
        print("Up")
        cnt += 1
    elif a > b:
        print("Down")
        cnt += 1
    else:
        cnt += 1
        break

print("정답!")
print("{0}번 만에 맞췄습니다.".format(str(cnt)))
