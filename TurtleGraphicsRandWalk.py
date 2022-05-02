#Demonstrates a Random walk with changing colors The Turtle is constrained to the boundries set by the window and will not go outside



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
    randangle = random.randint(1,359)
    if leftOrRight == 0:
        turtle.left(randangle)
    else:
        turtle.right(randangle)
    turtle.forward(checkConstraints(timmy.heading(), timmy.xcor(), timmy.ycor(), distance))

def randHeadingWalk(turtle,distance):

    heading = [0,90,180,270]

    newheading = random.choice(heading)

    turtle.setheading(newheading)

    turtle.forward(checkConstraints(timmy.heading(), timmy.xcor(), timmy.ycor(), distance))

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
            
       
#incomplete function to do the same thing as above but with any angle
def angleCheckConstraint(x,y,dist,angle):

    #dist = c
    #b = X dist
    #a = y dist
    rads = angle * (math.pi / 180)

    b = dist * math.sin(rads)

    a = math.sqrt(pow(dist, 2) + pow(b, 2))
    position = [a,b]
    return






     















# Set Variables and Objects

timmy = Turtle()
frank = Turtle()
screen = Screen()
timmy.shape("circle")
frank.shape("square")
#main Drawing Code-------------------------------

#timmy.dot(20,)

timmy.speed(0)
timmy.pensize(20)
frank.speed(0)
frank.pensize(20)
hitboundry = 0
#screen.screensize(400,400)
print(screen.screensize())
timmy.setheading(270)
while True:
    newColor(timmy)
    newColor(frank)
    timmy.speed(0)
    randHeadingWalk(timmy,50)








#for i in range(1,10):
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







