import time
import os

frameList = ['''
 +---+
 O   |
/|\  |
/ \  |
    ===
 '''
    ,
 '''
 
 +---+
 \O/ |
  |  |  
  \\\   |    
     ===''']

while True:
	os.system("cls")
	for frame in frameList:
		print(frame)
		time.sleep(.2)
		os.system("cls")
