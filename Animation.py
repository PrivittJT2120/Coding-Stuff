import time
import os

frameList = [''']
          ___
 (^u^)    | O
 /||\\     |/ \\
  / \\     |
'''
   ,
'''
      ___
 (^u^)| O
 /||\\|/ \\
  /|   |
'''
   ,
'''
___
|(^u^)  
|/||\\
|/ \\



''']
while True:
	os.system("cls")
	for frame in frameList:
 		print(frame)
 		time.sleep(.5)
 		os.system("cls")
