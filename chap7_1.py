# import sys
# print(sys.argv)

# print(sys.getwindowsversion())
# print(sys.copyright)
# print(sys.version)

# import os
# print("OS : ",os.name)
# print("폴더 : ",os.getcwd())
# print("현재 폴더 내부의 요소 : ",os.listdir())

# #os.mkdir("Hello")
# os.rmdir("Hello")


from urllib import request
target = request.urlopen("https://www.naver.com/")
status = target.getheaders()

for item in status:
    print(item)