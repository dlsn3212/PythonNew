import cv2
import numpy as np
import os

recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('trainer.yml')
cascadePath = 'haarcascades/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX

id = 0

names = ['None','yoojin','ashely','yejin','park']

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
    ret, img = cam.read()
    img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #BGR순서 원래는 RGB

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW),int(minH))
    )

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        if(confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(img,str(id), (x+5,y-5), font, 1, (255,255,255),2)
        cv2.putText(img, str(confidence), (x+5,y+h-5),font,1,(255,255,0),1) #putText사용 xy위치에 글자 뿌려줌

    cv2.imshow('camera',img)
    k = cv2.waitKey(10) & 0xff
    if k == 27: # 끝냄
        break

print("\n [INFO] Exiting Progtam and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
