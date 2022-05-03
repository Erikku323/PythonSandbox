#Paints to screen with random RGB colors using Turtle Graphics


import math
import turtle
from turtle import Turtle , Screen
import math
import random


def drawSquare(turtle,multiply):
    turtle.forward(30*multiply)
    turtle.right(-90)
    turtle.forward(30*multiply)
    turtle.right(-90)
    turtle.forward(30*multiply)
    turtle.right(-90)
    turtle.forward(30*multiply)
    turtle.right(-90)

def drawDashed(turtle,size):
    turtle.forward(size)
    turtle.penup()
    turtle.forward(size)
    turtle.pendown()

def drawTriangle(a,b,turtle):

    #a^2 + b^2 = c^2

    c = math.sqrt(pow(a,2) +pow(b,2))
    angle = math.asin(a/c) * 180/math.pi
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90 + angle)
    print(90 + angle)
    turtle.forward(c)
    turtle.setheading(0)

def randAngleWalk(turtle,distance):
    leftOrRight =random.randint(0,1)
    randangle = random.randint(0,359)
    if leftOrRight == 0:
        turtle.left(randangle)
    else:
        turtle.right(randangle)
    turtle.forward(angleCheckConstraint(turtle.xcor(),turtle.ycor(),distance,turtle.heading()))

def randHeadingWalk(turtle,distance):

    heading = [0,90,180,270]

    newheading = random.choice(heading)

    turtle.setheading(newheading)

    turtle.forward(checkConstraints(turtle.heading(),turtle.xcor(),turtle.ycor(),distance))

def newColor(turtle):
    colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
               "SeaGreen"]
    turtle.pencolor(random.choice(colors))



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


def angleCheckConstraint(x,y,dist,angle):
    #dist = c
    #b = X dist
    #a = y dist
    rads = angle * (math.pi / 180)
    x_Lim = screen.canvwidth
    y_Lim = screen.canvheight
    Quadrant = 0

    while True:
        print("current dist is " + str(dist))
        b = dist * math.sin(rads)



        a = math.sqrt(pow(dist, 2) + pow(b, 2))




        if angle >= 0 and angle <= 90:
            #Both Positive
                b = x + b
                a = y + a
                Quadrant = 1
        elif angle > 90 and angle <= 180:
                b = (x + b)
                b = -b
                print("B is " + str(b))
                a = y + a
                Quadrant = 2
        elif angle > 180 and angle <= 270:
                b = (x + b) * -1
                a = (y + a) * -1
                Quadrant = 3
        else:
                b = x + b
                a = (y + a) * -1
                Quadrant = 4

        Newposition = [b, a]

        if (a > 1000) or b > 1000:
            turtle.color("red")
            turtle.goto(0, 0)

            return 0

        #return Newposition
        #print("Quadrant is " +str(Quadrant))
        #print(Newposition)
        if (Quadrant == 1) and ((x_Lim < b ) or (y_Lim < a )):
            print("I")
            print(x_Lim)
            print(y_Lim)
            dist = dist - 1
        elif (Quadrant == 2) and ((-x_Lim > -b ) or (y_Lim < a )):
            dist = dist - 1
            print("II")
        elif (Quadrant == 3) and ((-x_Lim > -b ) or (-y_Lim > -a )):
            dist = dist - 1
            print("III")
        elif (Quadrant == 4) and ((x_Lim < b < 0) or (-y_Lim > -a)):
            dist = dist - 1
            print("IV")
        else:
            print("Dist Is  = " + str(dist))
            return dist

# Set Variables and Objects

timmy = Turtle()
frank = Turtle()
screen = Screen()
timmy.shape("circle")
frank.shape("square")
turtle.colormode(255)
#main Drawing Code-------------------------------

#timmy.dot(20,)

timmy.speed(0)
timmy.pensize(20)
frank.speed(0)
frank.pensize(20)
hitboundry = 0

x = timmy.xcor()
y = timmy.ycor()
dist = 20
heading = timmy.heading()
#screen.screensize(400,400)
print(screen.screensize())



while True:
   # newColor(timmy)
   r = random.randint(0,255)
   g = random.randint(0,255)
   b = random.randint(0,255)
   timmy.pencolor(r,g,b)
   timmy.speed(0)
    #randHeadingWalk(timmy,50)
   randAngleWalk(timmy,dist)














#for i in range(1,10):=
#    drawTriangle(25,30*i,timmy)





# for i in range(1,100):
#     #drawSquare(timmy,i)
#     drawDashed(timmy,10)






#Go Back and forth
# while True:
#     for i in range(450):
#         if timmy.xcor() < 451:
#             timmy.forward(speed)
#
#     for i in range(450):
#         if timmy.xcor() > -451:
#             timmy.back(speed)







