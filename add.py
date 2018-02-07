import cv2                                                                      # openCV
import numpy as np                                                              # for numpy arrays
import sqlite3
import dlib
import os                                                                       # for creating folders
import shutil
import sys



cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()

def insert(roll,name) :                                                # this function is for database
    connect = sqlite3.connect("A.db")                                  # connecting to the database
    params = (roll,name)                                               # insering a new student data
    connect.execute("INSERT INTO Student(Roll,name) VALUES(?, ?)",params)
    connect.commit()                                                   # commiting into the database
    connect.close()


name = raw_input("Enter student's name : ")
roll = raw_input("Enter student's Roll Number : ")

insert(roll,name)

folderName = "user" + roll                                                        # creating the person or user folder
folderPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dataset/"+folderName)
if not os.path.exists(folderPath):
    os.makedirs(folderPath)

new=os.path.join(folderPath,'comImage.py')

shutil.copy2('comImage.py', new) # complete transfer of file

sampleNum = 0
while(True):
    ret, img = cap.read()                                                       # reading the camera input
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                # Converting to GrayScale
    dets = detector(img, 1)
    for i, d in enumerate(dets):                                                # loop will run for each face detected
        sampleNum += 1
        cv2.imwrite(folderPath + "/" + roll +"User" + str(sampleNum) + ".jpg",
                    img[d.top():d.bottom(), d.left():d.right()])                                                # Saving the faces
        cv2.rectangle(img, (d.left(), d.top())  ,(d.right(), d.bottom()),(0,255,0) ,2) # Forming the rectangle
        cv2.waitKey(200)                                                        # waiting time of 200 milisecond
    cv2.imshow('frame', img)                                                    # showing the video input from camera on window
    cv2.waitKey(1)
    if(sampleNum >= 20):                                                        # will take 20 faces
        break

cap.release()                                                # turning the webcam os.system(new+" 1")

cv2.destroyAllWindows()                                                         # Closing all the opened windows
