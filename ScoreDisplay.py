from turtle import Turtle

class scoreDisplay :

    def __init__(self):
        self.score = 0
        self.scoreDisp = Turtle()
        self.scoreLoc = [-250,250]
        self.scoreDisp.penup()
        self.scoreDisp.hideturtle()
        self.scoreDisp.goto(self.scoreLoc[0],self.scoreLoc[1])
        self.scoreDisp.write("Score = " + str(self.score),font=("Arial", 20, "normal"))

    def addScore(self):
        self.score = self.score + 1
        self.scoreDisp.clear()
        self.scoreDisp.write("Score = " + str(self.score), font=("Arial", 20, "normal"))


    def gameOVer(self):
        self.scoreDisp.goto(-120,0)
        self.scoreDisp.write("GAME OVER!", font=("Arial", 30, "normal"))

    def resetScore(self):
        self.scoreDisp.clear()
        self.score = 0
        self.scoreLoc = [-250, 250]
        self.scoreDisp.write("Score = " + str(self.score), font=("Arial", 20, "normal"))

