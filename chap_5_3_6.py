# def test():
#     print("A 지점 통과")
#     yield 1
#     print("B 지점 통과")
#     yield 2
#     print("C 지점 통과")

# print("A 지점 통과")
# test()

# output = test()
# print("D 지점 통과")
# a = next(output)
# print(a)

# print("E 지점 통과")
# b = next(output)
# print(b)

# print("F 지점 통과")
# c = next(output)
# print(c)

def num_gen():
    yield 1
    yield 2
    yield 3 # 함수 자체를 반복해줌
    yield 4 

print(list(num_gen()))
for i in num_gen():
    print(i)