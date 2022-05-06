from turtle import Turtle
import random




class snake :

    def __init__(self):
        self.snakeHeading = 0
        self.snakeBody = []
        self.startPos = 0

        # create a new snake
        for i in range(0, 3):
            self.snakeBody.append(Turtle())
            self.snakeBody[i].shape("square")
            self.startPos = -20 * i
            # snakeBody[i].color(colors[i])
            self.snakeBody[i].penup()
            self.snakeBody[i].speed(1)
            self.snakeBody[i].goto(self.startPos, 0)
            self.snakeBody[i].penup()



    def moveSnake(self,apple):

        snakeX = []
        snakeY = []
        snakeBody = self.snakeBody
        snakeHeading = self.snakeHeading



        for i in range(len(snakeBody)):
            snakeX.append(snakeBody[i].xcor())
        for i in range(len(snakeBody)):
            snakeY.append(snakeBody[i].ycor())

        for i in range(1, len(snakeBody)):
            snakeBody[i].goto(snakeX[i - 1], snakeY[i - 1])


        if snakeHeading == 0:
            #print("East")
            #going East
            x = snakeBody[0].xcor() + 20
            y = snakeBody[0].ycor()
            snakeBody[0].goto(x,y)
        elif snakeHeading == 1:
            #going North
            #print("Nort")
            x = snakeBody[0].xcor()
            y = snakeBody[0].ycor() +20
        elif snakeHeading == 2:
            #going West
            #print("West")
            x = snakeBody[0].xcor() - 20
            y = snakeBody[0].ycor()
        elif snakeHeading == 3:
            #going South
            #print("South")
            x = snakeBody[0].xcor()
            y = snakeBody[0].ycor() - 20

        snakeBody[0].goto(x,y)


        appleX = apple.x
        appleY = apple.y
        dist = snakeBody[0].distance(appleX,appleY)
        if dist < 20:
            apple.newApple()
            self.eat(apple)
            return True
        return False



    def eat(self,apple):
        snakeBody = self.snakeBody
        snakeHeading = self.snakeHeading

        i = len(snakeBody) - 1
        if snakeBody[i].xcor() == snakeBody[i - 1].xcor():
            XstartPos = snakeBody[i].xcor()
            if snakeBody[i].ycor() > snakeBody[i - 1].ycor():
                YstartPos = snakeBody[i].ycor() - 20
            else:
                YstartPos = snakeBody[i].ycor()


        elif snakeBody[i].ycor() == snakeBody[i - 1].ycor():
            print(len(self.snakeBody))
            YstartPos = snakeBody[i].ycor()
            if snakeBody[i].xcor() > snakeBody[i - 1].xcor():
                XstartPos = snakeBody[i].xcor() - 20
            else:
                XstartPos = snakeBody[i].xcor()

        snakeBody.append(Turtle())
        i = i + 1
        # print(i)
        snakeBody[i].shape("square")
        # snakeBody[i].color(colors[i])
        snakeBody[i].penup()
        snakeBody[i].speed(1)
        snakeBody[i].goto(XstartPos, YstartPos)

    def checkCollision(self):
        snakeX = []
        snakeY = []
        lim = 289

        for i in range(len(self.snakeBody)):
            snakeX.append(self.snakeBody[i].xcor())
        for i in range(len(self.snakeBody)):
            snakeY.append(self.snakeBody[i].ycor())
        for i in range(1, (len(self.snakeBody) - 1)):
            if self.snakeBody[0].distance(snakeX[i], snakeY[i]) < 5:
                #print("I hit myself")
                return True
            elif self.snakeBody[0].xcor() <= -lim or self.snakeBody[0].xcor() >= lim:
                #print("Hit the side")
                return True
            elif self.snakeBody[0].ycor() <= -lim or self.snakeBody[0].ycor() >= lim:
                #print("Hit the ceiling or floor")
                return True

        return False

    def killSnake(self):
        for i in range(len(self.snakeBody)):
            self.snakeBody[i].hideturtle()

class snakeFood:


    def __init__(self):
        self.apple = Turtle()
        self.apple.color("red")
        self.apple.shape("circle")
        self.apple.penup()
        self.x = random.randint(-250, 250)
        self.y = random.randint(-250, 250)
        self.newApple()

    def newApple(self):
        self.x = random.randint(-250, 250)
        self.y = random.randint(-250, 250)
        self.apple.goto(self.x, self.y)

    def killApple(self):
        self.apple.hideturtle()

class scoreDisplay :

    def __init__(self):
        self.highScore = 0
        self.score = 0
        self.scoreDisp = Turtle()
        self.scoreLoc = [-250,250]
        self.highScoreLoc = [80,250]
        self.scoreDisp.penup()
        self.scoreDisp.hideturtle()
        self.scoreDisp.goto(self.scoreLoc[0],self.scoreLoc[1])
        self.scoreDisp.write("Score = " + str(self.score),font=("Arial", 20, "normal"))
        self.scoreDisp.goto(self.highScoreLoc[0], self.highScoreLoc[1])
        self.scoreDisp.write("High Score = " + str(self.highScore), font=("Arial", 20, "normal"))

    def addScore(self):
        self.score = self.score + 1
        self.scoreDisp.clear()
        self.scoreDisp.goto(self.scoreLoc[0], self.scoreLoc[1])
        self.scoreDisp.write("Score = " + str(self.score), font=("Arial", 20, "normal"))
        self.scoreDisp.goto(self.highScoreLoc[0], self.highScoreLoc[1])
        self.scoreDisp.write("High Score = " + str(self.highScore), font=("Arial", 20, "normal"))


    def gameOVer(self):
        self.scoreDisp.goto(-120,0)
        self.scoreDisp.write("GAME OVER!", font=("Arial", 30, "normal"))

    def clearScore(self):
        if self.highScore < self.score:
            self.highScore = self.score
        self.score = 0
        self.scoreDisp.clear()
        self.scoreDisp.goto(self.scoreLoc[0], self.scoreLoc[1])
        self.scoreDisp.write("Score = " + str(self.score), font=("Arial", 20, "normal"))
        self.scoreDisp.goto(self.highScoreLoc[0], self.highScoreLoc[1])
        self.scoreDisp.write("High Score = " + str(self.highScore), font=("Arial", 20, "normal"))


