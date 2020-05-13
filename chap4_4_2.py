array = []
# 빈 리스트 생성

# for문
for i in range(1,20,2):
    array.append(2 **i)

# 출력
print(list(array))

array2 = [2 ** i for i in range(4,20)]
print(array2)