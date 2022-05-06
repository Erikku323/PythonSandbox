from turtle import Turtle

class boarder:
    def __init__(self):
        lim = 300
        self.wall = Turtle()
        self.wall.shape("square")
        self.wall.pensize(20)
        self.wall.penup()
        self.wall.goto(-lim,-lim)


        self.wall.pendown()
        self.wall.goto(-lim,lim)
        self.wall.goto(lim, lim)
        self.wall.goto(lim, -lim)
        self.wall.goto(-lim, -lim)


