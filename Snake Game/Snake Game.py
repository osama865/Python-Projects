# simple Snake Game
# Done By Osama

import turtle
import os
import time
import random

delay = 0.1

score = 0
high_score = 0

# Pen
pen = turtle.Turtle()
pen.speed (0)
pen.color("grey")
pen.penup()
pen.hideturtle()
pen.goto(0 , 270)

def write_score () :
    pen.write("Score : {}  High Score : {} " .format(score , high_score) , align = "center" , font = ("courier" , 24  , "normal" ) )

#setup the screen
wn = turtle.Screen()
wn.title("Simple Snake Game")
wn.bgcolor("black")
wn.setup (width=650 , height= 650)
wn.tracer(0) # turns off the screen updates

#Snake  head
head = turtle.Turtle()
head.speed (0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food 
food = turtle.Turtle()
food.speed (0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(27,150)

segments = [] 

# functions

def GoUp():
   if head.direction != "down" :
        head.direction = "up"

def GoDown():
    if head.direction != "up" :
        head.direction = "down"


def GoRight():
    if head.direction != "left" :
        head.direction = "right"

def GoLeft():
    if head.direction != "right" :
        head.direction = "left"



def Move ():
    if head.direction == "up" :
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down" :
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "right" :
        x = head.xcor()
        head.setx(x+20)

    if head.direction == "left" :
        x = head.xcor()
        head.setx(x-20)


# keyboard bindings
wn.listen()
wn.onkeypress(GoUp , "w")
wn.onkeypress(GoDown , "s")
wn.onkeypress(GoRight , "d")
wn.onkeypress(GoLeft , "a")


# main game loop

while True :
    wn.update()
    write_score ()
    # Check for a collision with the border
    if head.xcor() > 300 or  head.xcor() < -300 or head.ycor()>300 or head.ycor()<-300 :
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop" 
        delay = 0.1
        pen.clear ()

        # hide the segments
        for segment in segments :
            segment.goto (1000, 1000)

        # Clear the segments list
        segments.clear()
        score = 0 
    if head.distance(food) < 20 :
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        food.goto(x,y)



        ns = turtle.Turtle()
        ns.speed (0)
        ns.shape("square")
        ns.color("blue")
        ns.penup()
        segments.append(ns)

        # Shorting the delay
        delay -= 0.004

        score += 10
        if high_score < score :
            high_score +=10
        if score >= high_score :
            high_score = score

        pen.clear()
        write_score ()

    # Move segments
    for index in range (len(segments)-1 , 0 , -1) :
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

        # Move segment 0 to where the head is
        if len(segments) > 0 :
            x = head.xcor ()
            y = head.ycor ()
            segments [0].goto(x,y)


    Move()

    # Check for head collision with body segments
    for segment in segments :
        if segment.distance(head) < 20 :
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            delay = 0.1
            
            for segment in segments :
                segment.goto(1000,1000)

            segments.clear()
            score =0 
            pen.clear()


    
    time.sleep(delay)

wn.mainloop()
