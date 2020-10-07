# Simple Pong Game Py Osama
# Import The Needed Libraries
import turtle
import random


wn = turtle.Screen()
wn.setup(800 , 600)
wn.bgcolor("black")
wn.title("PONG")
wn.tracer(0)

# Pen To Write Score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.shapesize(6 , 1)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,256)



# Paddle A
a = turtle.Turtle()
a.speed(0)
a.shape("square")
a.shapesize(6 , 1)
a.color("white")
a.penup()
a.goto(-350 ,  0)
a.score = 0

# Paddle B
b = turtle.Turtle()
b.speed(0)
b.shape("square")
b.shapesize(6 , 1)
b.color("white")
b.penup()
b.goto(350 ,  0)
b.score = 0

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(1 , 1)
ball.color("red")
ball.penup()
ball.goto(0 ,  0)
ball.dx = 2
ball.dy = -2

# Functions
def paddle_a_up():
    y = a.ycor()
    y += 20
    a.sety(y)

def paddle_a_down():
	y = a.ycor()
	y -= 20
	a.sety(y)

def paddle_b_up():
	y = b.ycor()
	y += 20
	b.sety(y)

def paddle_b_down():
	y = b.ycor()
	y -= 20
	b.sety(y)

def is_collision_b ():
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < b.ycor() + 40 and ball.ycor() > b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        b.score += 1
        pen.clear()
        

def is_collision_a ():
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < a.ycor() + 40 and ball.ycor() > a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        a.score +=1
        pen.clear()
        

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

def write_score():
    print("Player A: {}  Player B: {}".format(a.score , b.score))


# Main Game Loop
while True:
    wn.update()

    # Move The Ball
    sx = ball.xcor() + ball.dx
    sy = ball.ycor() + ball.dy
    ball.goto(sx , sy)

    # Border Checking
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390 :
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    is_collision_b()
    is_collision_a()
    write_score()
    
