# 파일을 열고 w는 한번생성 a는 계속 생성 r은 읽음
f = open("./data/basic.txt","w")
# 파일 쓰고
f.write("Hello Python Proframming...!!")
# 파일 닫기
f.close()

f1 = open("./data/basic.txt","a")
f1.write("\nAdded documents")
f.close()

with open("./data/test.txt","a") as f3:
    f3.write("\nWith sentence document")

content = ""
with open("./data/test.txt","r") as f4:
    content = f4.read()

print(content)