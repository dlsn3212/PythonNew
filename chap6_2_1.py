import math

try:
    number = int(input("정수 입력 > "))
    if number > 0:
        raise NotImplementedError("0보다 큼 : 구현안됨")
    else:
        raise NotImplementedError("0보다 작음 : 구현안됨")
except NotImplementedError as ex:
    print("구현 좀 하세요~")
    print(ex)
except ValueError as ex:
    print("정수를 넣으세요!!!!")
except Exception as ex:
    print(type(ex))
    print(ex)
finally:
    print("무조건 실행")