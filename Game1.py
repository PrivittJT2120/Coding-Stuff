from turtle import *

scoreTurtle = Turtle()
myScreen = scoreTurtle.getscreen()
scoreTurtle.penup()
scoreTurtle.hideturtle()
scoreTurtle.goto(myScreen.window_width() / 2 - 200, myScreen.window_height()/2-50)
score = 0

def updateScore():
	scoreTurtle.clear()
	scoreTurtle.write("Score: " + str(score), False, "left", font=("Times New Roman", 25, "normal"))

updateScore()

myScreen.mainloop()