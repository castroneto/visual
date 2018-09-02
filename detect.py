import numpy as np
import cv2
import sys
import os
from threading import Timer

rostoCascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
corpoCascade = cv2.CascadeClassifier('haarcascade_mcs_upperbody.xml')
carsCascade = cv2.CascadeClassifier('cars.xml')

cap = cv2.VideoCapture(0)

pecoa = False
carro = False

def setTimeOut():
    if pecoa == True:
        os.system("mpg321 audios/pessoa.mp3")
    elif carro == True:
        os.system("mpg321 audios/carro.mp3")
    Timer(2.0, setTimeOut).start()
Timer(2.0, setTimeOut).start()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = carsCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100,150),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    rosto = rostoCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100,150),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    corpo = corpoCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100,150),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    if len(rosto) is not 0:
        pecoa = True
    else:
        pecoa = False

    if len(cars) is not 0:
        carro = True
    else:
        carro = False

    #for (x, y, w, h) in rosto:
    #    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) 
    #for (x, y, w, h) in cars:
    #    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) 
    #for (x, y, w, h) in corpo:
    #    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) 

    # Display the resulting frame
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()