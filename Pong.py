from paddle import Paddle,Ball
from turtle import Screen,Turtle

from scoreBoard import ScoareBoard
import time
from turtle import Turtle

# Simple game of Pong built with Turtle use W and S to go up and down The other paddles AI seems to be too good impossible to win




class Paddle(Turtle):

    def __init__(self,player):
        super(Paddle, self).__init__()
        self.player = player
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.moveSpeed = 3




        if self.player == 0:
            self.goto(-300,0)
        else:
            self.goto(300,0)

    def move_up(self):
        self.goto(self.xcor(),self.ycor() + 10)

    def move_down(self):
        self.goto(self.xcor(),self.ycor() - 10)

    def player2Move(self,ball):
        speed = self.moveSpeed
        if ball.ycor() > self.ycor():
            if ball.ycor() - self.ycor() >10:
                self.goto(self.xcor(),self.ycor() +speed)
        elif  ball.ycor() < self.ycor():
            if self.ycor() - ball.ycor() > 10:
               self.goto(self.xcor(),self.ycor() -speed)


class ScoareBoard(Turtle):

    def __init__(self):
        super(ScoareBoard, self).__init__()
        self.p1Score = 0
        self.p2Score = 0
        self.penup()
        self.hideturtle()
        self.scoreLoc = [250, 300]

    def updateScore(self):
        self.clear()
        self.goto(-self.scoreLoc[0], self.scoreLoc[1])
        self.write(str(self.p1Score), font=("Arial", 20, "normal"))
        self.goto(self.scoreLoc[0], self.scoreLoc[1])
        self.write(str(self.p2Score), font=("Arial", 20, "normal"))







class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.penup()
        self.velocity = 5
        self.speed(10)
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 10


    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()



    # def move_ball(self,p1,p2):
    #     p1Lim = p1.xcor()
    #     lim = 400
    #     print(p1.xcor())
    #     self.forward(self.velocity)
    #     if self.xcor() < -lim or self.xcor() > lim:
    #         print("POINT!")
    #         self.forward(self.velocity)
    #
    #     elif self.ycor() < -lim or self.ycor() > lim:
    #         print("Floor")
    #         self.setheading(90 + self.heading())
    #         self.forward(self.velocity)
    #        # self.velocity = self.velocity * -1
    #        # self.forward(10)
    #         print(self.heading())
    #     elif self.distance(p1) < 50 and self.xcor() < p1.xcor() + 10 :
    #         print("Hit P1")
    #         self.setheading(90 + self.heading())
    #         self.forward(self.velocity)
    #     elif self.distance(p2) < 50 and self.xcor() > p2.xcor() - 10:
    #         print("Hit P2")
    #         self.setheading(90 + self.heading())
    #         self.forward(self.velocity)







class Boarder:
    def __init__(self):
        lim = 400
        self.wall = Turtle()
        self.wall.shape("square")
        self.wall.pensize(20)
        self.wall.penup()
        self.wall.goto(-lim,lim)
        self.wall.pendown()
        self.wall.goto(lim,lim)
        self.wall.penup()
        self.wall.goto(-lim, -lim)
        self.wall.pendown()
        self.wall.goto(lim, -lim)





screen = Screen()
screen.tracer(0)
screen.title("Pong!")
player1 = Paddle(0)
player2 = Paddle(1)
wall = Boarder()
ball = Ball()
ball.setheading(180)
score = ScoareBoard()
score.updateScore()
def move_up():
    player1.move_up()

def move_down():
    player1.move_down()

screen.tracer(0)

screen.listen()
screen.onkeypress(key="w", fun=move_up)
screen.onkeypress(key="s", fun=move_down)
while True:
    ball.move_ball()
    player2.player2Move(ball)


    #Detect collision with wall
    p1Lim = player1.xcor() + 10
    p2Lim = player2.xcor() - 10
    if ball.ycor() > 400 or ball.ycor() < -400:
        ball.bounce_y()
    #Detect collision with paddle
    if ball.distance(player2) < 50 and ball.xcor() > p2Lim or ball.distance(player1) < 50 and ball.xcor() < p1Lim:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.p1Score = score.p1Score + 1
        score.updateScore()

       # scoreboard.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        score.p2Score = score.p2Score + 1
        score.updateScore()
       # scoreboard.r_point()




    time.sleep(0.01)
    screen.update()



screen.exitonclick()
