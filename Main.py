from Snake import snake,snakeFood, scoreDisplay
from turtle import Screen
from Boarder import boarder
import time

def move_right():
    cobra.snakeHeading= cobra.snakeHeading -1
    if cobra.snakeHeading < 0:
        cobra.snakeHeading = 3



def move_left():
    cobra.snakeHeading = cobra.snakeHeading + 1
    if cobra.snakeHeading > 3:
        cobra.snakeHeading = 0


#setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake")
screen.tracer(0)
wall = boarder()
scoreDisp = scoreDisplay()


while True:

    #Variables
    isGameOver = False


    # init Playfield obj
    cobra = snake()
    apple = snakeFood()


    #Listeners
    screen.listen()
    screen.onkeypress(key="d",fun=move_right)
    screen.onkeypress(key="a",fun=move_left)






    #Main Game loop

    while isGameOver == False:
        scoreadded = cobra.moveSnake(apple)
        if scoreadded == True:
            scoreDisp.addScore()
        isGameOver = cobra.checkCollision()
        time.sleep(0.1)
        screen.update()

    cobra.killSnake()
    apple.killApple()
    scoreDisp.gameOVer()
    screen.update()
    time.sleep(2)
    scoreDisp.clearScore()

    screen.update()


screen.exitonclick()




