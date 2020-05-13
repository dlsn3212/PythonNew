
# # 재귀 함수
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)

# print("1! : {}".format(factorial(1)))
# print("2! : {}".format(factorial(2)))
# print("3! : {}".format(factorial(3)))
# print("4! : {}".format(factorial(4)))
# print("5! : {}".format(factorial(5)))
# print("10! : {}".format(format(factorial(10),',d')))


import time

dictionary = {
    1:1,
    2:1,
}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n-1) + fibonacci(n - 2)
        dictionary[n] = output
        return output

start = time.time()
print("fibonnaci(35) ", fibonacci(35))
print("실행시간 : ",time.time()-start,"sec")

