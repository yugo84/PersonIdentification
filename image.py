import numpy as np
import cv2
import requests
import time
def yeye():
    face_cascade = cv2.CascadeClassifier('/Users/z002r1y/PycharmProjects/openCv/venv/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('/Users/z002r1y/PycharmProjects/openCv/venv/lib/python3.6/site-packages/cv2/data/haarcascade_eye.xml')

    cap = cv2.VideoCapture(0)
    API_ENDPOINT = "https://rest.nexmo.com/sms/json"

    data = {'api_key': "4cba9b75",
            'api_secret':'197da78d',
            'to':'917597071720',
            'from':'Iron man',
            'text': 'Some one is there'}
    wait=0
    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        print(faces==())
        if faces!=():
            wait=wait+1
            print("wait", wait)
            if wait==10:
                r = requests.post(url=API_ENDPOINT, data=data)
                print(r.text)
                print('message sent')
                break
        cv2.imshow('img',img)
        k = cv2.waitKey(20) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

numerOfTimesNotifies=0
while 1:
   yeye()
   numerOfTimesNotifies = numerOfTimesNotifies+1
   time.sleep(5)
   if numerOfTimesNotifies==2:
       print("Inside resetting loop")
       time.sleep(200)
       numerOfTimesNotifies=0

