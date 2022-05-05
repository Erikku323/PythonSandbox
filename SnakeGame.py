import random
from turtle import Turtle,Screen
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake")

colors = ["red","blue","green","yellow","purple","black"]
snakeHeading = 0

#Create New Apple

apple = Turtle()
apple.color("red")
apple.shape("square")
apple.penup()
x = random.randint(-250, 250)
y = random.randint(-250, 250)



# Checks if the Turtle will go outside the boundries of the window and adjust accordingly
def checkConstraints(heading,x,y,dist):

    while True:
        # Going East Constraint
        if x+dist < screen.canvwidth and heading == 0:
          # print("east")
           return dist
        #going west Constraint
        elif x - dist > -screen.canvwidth and heading == 180:
           #print("west")
           return dist
            #Going North
        elif y + dist < screen.canvheight and heading == 90:
           #print("north")
           return dist
        #going South
        elif y - dist >-screen.canvheight and heading == 270:
           # print("south")
            return dist
        else:
            #print("I have hit a wall")
            dist = dist - 1


def moveSnake():

    snakeX = []
    snakeY = []




    for i in range(len(snakeBody)):
        snakeX.append(snakeBody[i].xcor())
    for i in range(len(snakeBody)):
        snakeY.append(snakeBody[i].ycor())

    for i in range(1, len(snakeBody)):
        snakeBody[i].goto(snakeX[i - 1], snakeY[i - 1])

    #print(snakeBody[len(snakeBody)-1].xcor())




    global snakeHeading

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


    appleX = apple.xcor()
    appleY = apple.ycor()
    dist = snakeBody[0].distance(appleX,appleY)
    if dist < 20:
        newApple()
        eat()





def eat():

    i = len(snakeBody) - 1
    if snakeBody[i].xcor() == snakeBody[i - 1].xcor():
        print("here X")
        XstartPos = snakeBody[i].xcor()
        if snakeBody[i].ycor() > snakeBody[i - 1].ycor():
            YstartPos = snakeBody[i].ycor() - 20
        else:
            YstartPos = snakeBody[i].ycor()


    elif snakeBody[i].ycor() == snakeBody[i - 1].ycor():
        print("here Y")
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
    snakeBody[i].goto(XstartPos,YstartPos)
    print(len(snakeBody))

def checkCollision():
    snakeX = []
    snakeY = []

    for i in range(len(snakeBody)):
        snakeX.append(snakeBody[i].xcor())
    for i in range(len(snakeBody)):
        snakeY.append(snakeBody[i].ycor())

    for i in range(1,len(snakeBody)-1):
        if snakeBody[0].distance(snakeX[i],snakeY[i]) < 5:
            print("I hit myself")
        elif snakeBody[0].xcor() < -250 or snakeBody[0].xcor() > 250:
            print("Hit the side")
        elif snakeBody[0].ycor() < -250 or snakeBody[0].ycor() > 250:
            print("Hit the ceiling or floor")





def newApple():
    x = random.randint(-250,250)
    y = random.randint(-250, 250)
    apple.goto(x,y)

def move_right():
    global snakeHeading
    snakeHeading = snakeHeading -1
    if snakeHeading < 0:
        snakeHeading = 3



def move_left():
    global snakeHeading
    snakeHeading = snakeHeading + 1
    if snakeHeading > 3:
        snakeHeading = 0




snakeBody=[]
startPos = 0
screen.tracer(0)
for i in range(0,5):
    snakeBody.append(Turtle())
    snakeBody[i].shape("square")
    startPos = -20 * i
    #snakeBody[i].color(colors[i])
    snakeBody[i].penup()
    snakeBody[i].speed(1)
    snakeBody[i].goto(startPos,0)
    snakeBody[i].penup()

#for i in range(len(snakeBody)):
   # print(snakeBody[i].xcor())


#y = snakeBody[0].ycor() + 20
#snakeBody[0].goto(snakeBody[0].xcor(),y)

screen.listen()
screen.onkeypress(key="d",fun=move_right)
screen.onkeypress(key="a",fun=move_left)

i = 0
newApple()









while True:

    moveSnake()
    checkCollision()
    time.sleep(0.1)
    screen.update()


screen.exitonclick()


