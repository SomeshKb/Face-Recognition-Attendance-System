import os
import sqlite3

import time

	#folderName = "user" + roll                                                        # creating the person or user folder
	#folderPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dataset/"+folderName)
	#if not os.path.exists(folderPath):
    	#os.makedirs(folderPath)

connect = sqlite3.connect("A.db")	

qry="select * from STUDENT"
rows=connect.execute(qry)
count=0
for row in rows:
        count+=1
connect.commit()  
connect.close()

print count

print time.strftime('%d%m%Y')


