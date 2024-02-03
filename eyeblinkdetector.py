import numpy as np
import cv2
import time
import winsound

k = 1


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
cap = cv2.VideoCapture(0)

c1 = 8
c2 = 6
count = 0


while (True):
    
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        
        k = 1
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        u1 = x + w
        u2 = y + h
        cir = cv2.circle(img, (x + w / 2, y + h / 2), 1, (0, 255, 255), 2)
        
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            k = 0
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 255, 0), 2)

    if k == 1:
        print "Blink"
        count = count + 1
        if count>8:
            print "Blink---buzzer blow"
            winsound.PlaySound('sound.wav', winsound.SND_ASYNC)
            time.sleep(2)
    if k == 0:
        print "No Blink"
        winsound.PlaySound(None, winsound.SND_PURGE)
        count = 0
        
    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("img", 600, 450)
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

