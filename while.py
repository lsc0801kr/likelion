# num = 1
# while num < 11:
#     print(num, "번 손님 주문하신 음료나왔습니다!")
#     num = num+1


# mental = 50
# while True:
#     print("강의를 듣습니다")
#     mental = mental-10
#     print("현재 멘탈 게이지 :", mental)
#     if mental == 0:
#         print("제발 이제 그만")
#         break


num = 0
while num < 10:
    num = num+1
    if num % 2 == 0:
        continue
    # 반복문의 가장 처음으로 돌아감
    print("홀수 :", num)
