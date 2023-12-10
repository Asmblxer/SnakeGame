from turtle import *
from random import randrange
from time import sleep

win = Screen()
win.title("Local Snake Game")
win.bgcolor("gray")
win.setup(width=700, height=700)
win.tracer(0)

name = win.textinput("User_Name", "Enter Your Name: ")

head = Turtle()
head.speed(0)
head.shape("circle")
head.color("yellow")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = Turtle()
food.speed(0)
food.shape("square")
food.color("green")
food.penup()
food.goto(randrange(-290, 290, 20), randrange(-290, 290, 20))

body = []

def add_body():
    new_body = Turtle()
    new_body.speed(0)
    new_body.shape("square")
    new_body.color("yellow")
    new_body.penup()
    body.append(new_body)

# Score
score = 0
high_score = 0
rond = 0

board = Turtle()
board.speed(0)
board.color("white")
board.penup()
board.hideturtle()
def scoreboard(rond, score, high_score):
    board.clear()
    board.goto(0, 310)
    board.write("Round {} {} Score: {}  High Score: {}".format(rond, name ,score, high_score), align="center", font=("Courier", 20, "normal"))
scoreboard(rond, score, high_score)
 

border = Turtle()
border.color("black","blue")
border.pensize(10)
border.penup()
border.goto(-310, 310)
border.pendown()
border.begin_fill()
border.goto(310, 310)
border.goto(310, -310)
border.goto(-310, -310)
border.goto(-310, 310)
border.end_fill()
border.hideturtle()


def escape():
    win.bye()
    exit()

def gameover():
    over = Turtle()
    win.clear()
    win.bgcolor("red")

    over.color("black")
    over.pensize(10)
    over.hideturtle()
    over.goto(30, -100)
    over.write(f"Game Over\n{name}\nhigh score {high_score} ", align="center", font=("Courier", 35, "normal"))
    sleep(3)
    over.clear()
    win.bye()
    exit()

def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


def move_mechanism():
    
    for index in range(len(body) - 1, 0, -1):
        x = body[index - 1].xcor()
        y = body[index - 1].ycor()
        body[index].goto(x, y)

    
    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)

def collision():
    
    if (
        head.xcor() > 300
        or head.xcor() < -300
        or head.ycor() > 300
        or head.ycor() < -300
    ) : return True
    
    for segment in body:
        if segment.distance(head) < 20: return True
        
    return False

def reset ():
    global score
    global high_score
    if score > high_score:
        high_score = score
    score = 0
    board.clear()
    head.goto(0, 0)
    head.direction = "stop"
    for segment in body:
        segment.hideturtle()
        segment.goto(1000, 1000)
    body.clear()



win.listen()
win.onkeypress(move_up, "Up")
win.onkeypress(move_down, "Down")
win.onkeypress(move_left, "Left")
win.onkeypress(move_right, "Right")
win.onkeypress(move_up, "w")
win.onkeypress(move_down, "s")
win.onkeypress(move_left, "a")
win.onkeypress(move_right, "d")
win.onkeypress(reset, "r")
win.onkeypress(escape, "Escape")

while True:
    win.update()

    if head.distance(food) < 20:

        food.goto(randrange(-290, 290, 20), randrange(-290, 290, 20))

        add_body()

        score += 10
        if score > high_score: high_score = score
        scoreboard(rond, score, high_score)

    move_mechanism()
    move()
    if collision() and rond < 2:
        rond += 1
        reset()
    elif collision() and rond >= 2: gameover()
    sleep(0.1)
