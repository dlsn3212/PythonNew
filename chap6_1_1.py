# # try except 연습

# try:
#     radius = int(input("정수입력 > "))
#     print("원의 반지름 : ",radius)
#     print("원의 둘레 : ",2 * 3.141592 * radius)
#     print("원의 넓이 : ",3.141592 * radius * radius)
# except Exception as ex:
#     print("뭔가 잘못되었습니다.")
# else:
#     print("에러가 발생하지않았습니다.")
# finally:
#     print("프로그램 종료")

except ValueError as ex:
    print(ex)
    print("점수를 입력하세요")
except IndexError as ex:
    print("인덱스를 벗어났어요")
except Exception as ex:
    print("에러났습니다")
    

# lists = ['11','22','33','하이','55']
# outputs = []

# for item in lists:
#     try:
#         float(item)
#         outputs.append(item)
#     except:
#         pass

# print(outputs)

# f = open("PythonNew/data/basic.txt",'r')
# try:
#     f.write("TEST!!")

# except Exception as e:
#     print(e)
# finally:
#     f.close()

# print("파일 클로즈?",f.closed)

# def test():
#     print("test() start")
#     try:
#         print("test() try")
#         return
#         print("test() after return")
#     except:
#         print("test() except")
#     else:
#         print("test() else")
#     finally:
#         print("test() finally")

# print("test() end")
# test()