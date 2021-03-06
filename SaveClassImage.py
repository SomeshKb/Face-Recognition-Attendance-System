import cv2
import os
import sqlite3
import time


cam = cv2.VideoCapture(0)
connect = sqlite3.connect("A.db")                                  # connecting to the database
today=str(time.strftime('%d%m%Y'))
cv2.namedWindow("Image")

img_counter = 0

folderPath=os.path.join(os.path.dirname(os.path.abspath(__file__)),"ClassImage")
if not os.path.exists(folderPath):
    os.makedirs(folderPath)

while True:
    ret, frame = cam.read()
    cv2.imshow("Image", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "Class.png".format(img_counter)
       	cv2.imwrite(os.path.join(folderPath , 'ClassImage.jpg'), frame)
        print("{} written!".format(img_name))
        img_counter += 1


connect.execute("ALTER TABLE STUDENT ADD COLUMN Date"+today+" char(1)")

cam.release()

cv2.destroyAllWindows()
