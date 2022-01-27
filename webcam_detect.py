import os
import threading
import time

import cv2
import numpy as np
from keras.models import load_model
from pygame import mixer

# from BT import bluetooth, read
from label_detect import classify_face

mixer.init()
sound = mixer.Sound("alarm.wav")


# face = cv2.CascadeClassifier('/media/preeth/Data/prajna_files/Drowsiness_detection/haar_cascade_files/haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
score = 0
thicc = 2
# bluetooth connection
'''bt = bluetooth("COM11")
while not bt.is_open():
    pass
print("BT Connected!")'''

'''readThread = threading.Thread(target=read)
readThread.setDaemon(True)
readThread.start()'''

# faces = face.detectMultiScale(gray,minNeighbors=5,scaleFactor=1.1,minSize=(25,25))
with_mask = True

while(True):
    ret, frame = cap.read()
    height, width = frame.shape[:2]
    label = classify_face(frame)
    if(label == 'with_mask'):
        '''if (with_mask == False):
            bt.write('o')'''
        cv2.putText(frame, str(label), (100, height-20),
                    font, 1, (51, 255, 51), 1, cv2.LINE_AA)
        cv2.rectangle(frame, (0, 0), (width, height), (51, 255, 51), 5)
        sound.stop()
        with_mask = True
        # print("With Mask")
    else:
        '''if (with_mask == True):
            bt.write('c')'''
        cv2.putText(frame, str(label), (100, height-20),
                    font, 1, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.rectangle(frame, (0, 0), (width, height), (0, 0, 255), 5)
        sound.play()
        with_mask = False
        print("Without Mask")
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
