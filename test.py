# input(money)
# if money >= 10000:
#     print("고기를 먹는다")
# elif (money >= 5000 || money < 10000):
#     print("국밥을 먹는다")
# else:
#     print("라면을 먹는다")


# li = [a, b, c, d, e]
# for i in range(5):
#     print(i+1, "번 과일을 입력하세요")
#     li[i] = input()

# for i in range(5):
#     print(i+1, "번째 과일은", li[i], "입니다.")


# cookies = {'탱커': '우유맛쿠키', '딜러': '칠리맛쿠키', '힐러': '천사막쿠키', '서포터': '석류맛쿠키'}
# print(cookies)
# if cookies['탱커']:
#     cookies['탱커'] = '다크초코맛쿠키'
# elif cookies['딜러']:
#     cookies['딜러'] = '라떼맛쿠키'
# elif cookies['힐러']:
#     cookies['힐러'] = '허브맛쿠키'
# print(cookies)


def add(a, b):
    print("a + b =", a+b)


def sub(a, b):
    print("a - b =", a-b)


def mul(a, b):
    print("a * b =", a*b)


def div(a, b):
    print("a / b =", a/b)


while a != 5 * b != 5:
    print('원하는 숫자를 입력하세요 1. 더하기 2. 빼기 3. 곱하기 4. 나누기 5. 종료')
    input(z)
    if z == 1:
        add(a, b):
    elif z == 2:
        sub(a, b)
    elif z == 3:
        mul(a, b)
    elif z == 4:
        div(a, b)
    elif z == 5:
        break
