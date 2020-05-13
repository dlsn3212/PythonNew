# a = 10
# b = 20

# if(a>b):
#     print("a가 b보다 큽니다.")
    
# print("정말입니다")


# # 입력
# number = input("수를 입력하세요 : ")
# number = int(number)

# # 양수 조건
# if(number > 0):
#     print("양수입니다.")

# # 음수 조건
# if(number < 0):
#     print("음수입니다.")

# # 0 조건
# if(number == 0):
#     print("0입니다.")

# import datetime

# current = datetime.datetime.now()

# # print(current.year, current.month, current.day)
# # print(current.hour,"시")
# # print(current.min,"분")
# # print(current.second,"초")

# print("{}년 {}월 {}일 {}시 {}분 {}초".format(current.year,current.month,current.day,
# current.hour,current.minute,current.second))

# if(3 <= current.month <=5):
#     print("이번 달은 {}월로 봄입니다!".format(current.month))


# number = input("수 입력 : ")

# last_ch = number[-1]

# # last_num = int(last_ch)

# # if last_num ==1\
# #     or last_num == 3\
# #     or last_num == 5\
# #     or last_num == 7\
# #     or last_num == 9:
# #     print("홀수입니다")

    
# # if last_num == 0\
# #     or last_num == 2\
# #     or last_num == 4\
# #     or last_num == 6\
# #     or last_num == 8:
# #     print("짝수입니다")

# if last_ch in "02468":
#     print("짝수입니다")

# if last_ch in "13579":
#     print("홀수입니다")

# number = input("수입력 : ")
# number = int(number)

# if number % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

import datetime as dt

current = dt.datetime.now()
mon = current.month

if 3 <= mon <= 5:
    print("봄")
elif 6<= mon <= 8:
    print("여름")
elif 9<= mon <= 11:
    print("가을")
else:
    print("겨울")