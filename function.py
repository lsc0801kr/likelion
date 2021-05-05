# a = 2
# b = 3

# print("지금 입력된 수는", a, "와", b, "이다")
# print(a+b)

# c = 20
# d = 30

# print("지금 입력된 수는", c, "와", d, "이다")
# print(c+d)

# e = 10
# f = 100

# print("지금 입력된 수는", e, "와", f, "이다")
# print(e+f)


# a = 7
# b = 3


# def add(a, b):  # 함수 선언
#     return a+b


# sum = add(a, b)
# print(sum)


# # a가 5이하일때만 더하기를 해주는 함수
# def add2(a, b):
#     if a > 5:
#         return "a가 5보다 큼"
#     return a+b


# sum2 = add2(a, b)
# print(sum2)


# a = 7
# b = 3


# def add(a, b):
#     print("a + b =", a+b)


# sum = add(a, b)
# print(sum)


# def func():
#     print("입력값도 결과값도 없는 함수에요 ~")


# func()


num = int(input("숫자를 입력하세요"))


def func(num):
    if (num > 10):
        print("10보다 큽니다.")
    elif (num == 10):
        print("10과 같습니다.")
    else:
        print("10보다 작습니다.")


func(num)
