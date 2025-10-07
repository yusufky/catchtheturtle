import turtle
import random

WIDTH, HEIGHT = 600, 600
TURTLE_SPEED = 1500
MARGIN = 100
GAME_TIME = 2

gameScreen = turtle.Screen()
gameScreen.setup(WIDTH, HEIGHT)
gameScreen.title("Catch the Turtle")
gameScreen.tracer(0)

score = 0
scorePen = turtle.Turtle()
scorePen.hideturtle()
scorePen.penup()
scorePen.goto(0, HEIGHT/2 - 40)

def updateScore():
    scorePen.clear()
    scorePen.write(f"Score: {score}", align="center", font=("Arial", 18, "bold"))

updateScore()

timeLeft = GAME_TIME
timerPen = turtle.Turtle()
timerPen.hideturtle()
timerPen.penup()
timerPen.goto(0, HEIGHT/2 - 70)

def updateTimer():
    global timeLeft
    timerPen.clear()
    timerPen.write(f"Time: {timeLeft}", align="center", font=("Arial", 18, "bold"))

updateTimer()

target = turtle.Turtle()
target.shape("turtle")
target.penup()
target.speed(0)
target.shapesize(2)

def randomPosition():
    x = random.randint(-WIDTH//2 + MARGIN, WIDTH//2 - MARGIN)
    y = random.randint(-HEIGHT//2 + MARGIN, HEIGHT//2 - MARGIN)
    return x, y

def moveTarget():
    if timeLeft > 0:
        x, y = randomPosition()
        target.goto(x, y)
        gameScreen.update()
        gameScreen.ontimer(moveTarget, TURTLE_SPEED)

def onClick(x, y):
    global score
    if timeLeft > 0:
        score = score + 1
        updateScore()
        moveTarget()

target.onclick(onClick)

def countdown():
    global timeLeft
    if timeLeft > 0:
        timeLeft = timeLeft - 1
        updateTimer()
        gameScreen.ontimer(countdown, 1000)
    else:
        target.hideturtle()
        gameScreen.update()
        scorePen.clear()
        timerPen.clear()
        timerPen.goto(0,0)
        timerPen.write(f"Game over ! Your score was {score}", align="center", font=("Arial", 22, "bold"))

moveTarget()
countdown()
gameScreen.update()
gameScreen.mainloop()

