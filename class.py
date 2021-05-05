# def show_info(name, major):
#     print("이름은", name)
#     print("학과는", major)


# show_info("임영빈", "컴퓨터공학과")
# show_info("김민지", "문화콘텐츠문화경영학과")
# show_info("김현조", "정보통신공학과")
# show_info("김재원", "전자공학과")
# show_info("한지훈", "컴퓨터공학과")


# 임영빈 컴퓨터공학과
# 김민지 문화콘텐츠문화경영학과

# name1 = "임영빈"
# major1 = "컴퓨터공학과"

# name2 = "김민지"
# major2 = "문화콘텐츠문화경영학과"

# name3 = "김현조"
# major3 = "정보통신공학과"


# def show_info(name,major):
#   print("이름은",name)
#   print("학과는",major)


# show_info(name1,major1)
# show_info(name2,major2)
# show_info(name3,major3)


# 임영빈 25세 컴퓨터공학과 프론트엔드
# 김민지 24세 문화콘텐츠문화경영학과 디자인

# name1 = "임영빈"
# major1 = "컴퓨터공학과"

# name2 = "김민지"
# major2 = "문화콘텐츠문화경영학과"


# def show_info(name, major):
#     print("이름은", name)
#     print("학과는", major)


# def work(name):
#     print(name, "얼른 일하세요 일")


# def order_time(name, time):
#     print("{0}씨 {1}까지 다 해오세요".format(name, time))


# show_info(name1, major1)
# show_info(name2, major2)
# work(name1)
# order_time(name2, "9시")


# # 클래스 선언
# class Member:
#     def __init__(self, name, major):
#         self.name = name
#         self.major = major

#     def show_info(self):
#         print("이름은", self.name)
#         print("학과는", self.major)

#     def work(self):
#         print(self.name, "일하세요 일")

#     def order_time(self, time):
#         print("{0}씨 {1}까지 다 해오세요".format(self.name, time))


# # 객체 생성
# member1 = Member("임영빈", "컴퓨터공학과")
# member2 = Member("김민지", "문화콘텐츠문화경영학과")
# member3 = Member("김현조", "정보통신공학과")
# member4 = Member("김재원", "전자공학과")
# member5 = Member("한지훈", "컴퓨터공학과")

# # 영빈오빠 자기소개시키기
# member1.show_info()
# # 민지언니 일시키기
# member2.work()
# # 현조언니 재촉하기
# member3.order_time("9시")
# # 김재원 이름출력
# print(member4.name)
# # 한지훈 과 출력
# print(member5.major)


# class Member:
#     def __init__(self, name, major):
#         self.name = name
#         self.major = major

#     def show_info(self):
#         print("이름은", self.name)
#         print("학과는", self.major)

#     def work(self):
#         print(self.name, "얼른 일하세요 일")

#     def order_time(self, time):
#         print("{0}씨 {1}까지 다 해오세요".format(self.name, time))


# class Member:
#     def __init__(self, name, major):
#         # init 초기값을 만드는 함수
#         self.name = name
#         self.major = major


# member3 = Member("김현조", "정보통신공학과")
# print(member3.name)
# print(member3.major)


# class Member:
#     def __init__(self, name, major):
#         self.name = name
#         self.major = major

#     def show_info(self):
#         print("이름은", self.name)
#         print("학과는", self.major)

#     def work(self):
#         print(self.name,"얼른 일하세요 일")

#     def order_time(self, time):
#         print("{0}씨 {1}까지 다 해오세요".format(self.name, time))
# #format: 앞에 중괄호 안에 어떤 것들이 들어가야 하는지 정해줌


# class Member:
#     def __init__(self, name, major):
#         self.name = name
#         self.major = major

#     def show_info(self):
#         print("이름은", self.name)
#         print("학과는", self.major)

#     def work(self):
#         print(self.name, "얼른 일하세요 일")
#         self.show_info()

#     def order_time(self, time):
#         print("{0}씨 {1}까지 다 해오세요".format(self.name, time))


# member4 = Member("김재원", "전자공학과")
# print(member4.name)
# member4.work()


# # 클래스 선언
# class Member:
#     def __init__(self, name, major):
#         # 객체 생성
#         self.name = name
#         self.major = major

#     def show_info(self):
#         print("이름은", self.name)
#         print("학과는", self.major)

#     def work(self):
#         print(self.name, "일하세요 일")

#     def order_time(self, time):
#         print("{0}씨 {1}까지 다 해오세요".format(self.name, time))


# # 객체 생성
# member1 = Member("임영빈", "컴퓨터공학과")
# member2 = Member("김민지", "문화콘텐츠문화경영학과")
# member3 = Member("김현조", "정보통신공학과")
# member4 = Member("김재원", "전자공학과")
# member5 = Member("한지훈", "컴퓨터공학과")

# # 영빈오빠 자기소개시키기
# member1.show_info()
# # 민지언니 일시키기
# member2.work()
# # 현조언니 재촉하기
# member3.order_time("9시")
# # 김재원 이름출력
# print(member4.name)
# # 한지훈 과 출력
# print(member5.major)


class Member:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def show_info(self):
        print("이름은", self.name)
        print("학과는", self.major)

    def work(self):
        print(self.name, "얼른 일하세요 일")

    def order_time(self, time):
        print("{0}씨 {1}까지 다 해오세요".format(self.name, time))


class HackathonMember(Member):
    # 상속받을 class의 이름을 괄호 안에 적어준다.
    def __init__(self, name, major, position):
        Member.__init__(self, name, major)
        self.position = position

    def show_info(self):
        print("이름은", self.name)
        print("학과는", self.major)
        print("포지션은", self.position)


member1 = HackathonMember("임영빈", "컴퓨터공학과", "프론트엔드")
member2 = HackathonMember("김민지", "문화콘텐츠문화경영학과", "디자인")

member1.show_info()
member1.work()
member2.order_time("10시")
