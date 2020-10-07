# Space Invaders 
#Set Up The Screen

import turtle
import os
import math
import random
import winsound



wn = turtle.Screen() 
wn.bgcolor("black")
wn.title ("Space Invaders")
wn.bgpic("space_invaders_background.gif")

wn.register_shape("invader.gif")
wn.register_shape("player.gif")
# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition (-300, -300)
border_pen.pendown ()
border_pen.pensize(2)

for side in range (4) :
    border_pen.fd(600)
    border_pen.lt(90)

border_pen.hideturtle ()
# score to zero
score = 0

# draw the score

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("grey")
score_pen.penup()
score_pen.setposition(-290 , 280)

score_pen.write("Score : {} " .format (score) , False , align="left" , font=("Arial" , 15 , "normal" ))
score_pen.hideturtle()

def WS () :
    score_pen.clear()
    score_pen.write("Score : {} " .format (score) , False , align="left" , font=("Arial" , 15 , "normal" ))
    score_pen.hideturtle()


player = turtle.Turtle()
player.color ("blue")
player.shape ("player.gif")
player.penup()
player.speed(0)
player.setposition(0 , -290)
player.setheading (90)

playerspeed = 15






# Choose a number of enemies
number_of_enemies = 5
# Create a list
enemies = []
# Add enemis to the list
for i in range(number_of_enemies) :
    enemies.append(turtle.Turtle())

for enemy in enemies :
    #Create the enemy
    
    enemy.shape("invader.gif")
    enemy.color("red")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200 , 200)
    y = random.randint(100 , 250)
    enemy.setposition(x,y )

enemyspeed = 2
# Create the player bullet
bullet = turtle.Turtle()
bullet.shape("triangle")
bullet.color("yellow")
bullet.speed(0)
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5 , 0.5)
bullet.hideturtle()

bulletspeed = 20

# bullet states 
# ready - ready to fire
bulletstate = "ready"
#fire - bullet is firing


# Move the player left and right 

def move_left () :
    x = player.xcor()
    x-= playerspeed
    if x < -280 :
        x = -280
    player.setx(x)

def move_right() : 
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x =280
    player.setx(x)
    
def fire_bullet () :
    global bulletstate
    if bulletstate == "ready" :
        winsound.PlaySound("laser.wav" , winsound.SND_FILENAME)
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x , y)
        bullet.showturtle()
        
def is_collision(t1 , t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor() , 2) + math.pow(t1.ycor() - t2.ycor() , 2) )
    if distance < 15 :
        return True
    else :
        return False

# create the keyboard bindings
turtle.listen()
turtle.onkeypress( move_left , "a")
turtle.onkeypress(move_right , "d")
turtle.onkeypress(fire_bullet , "space")



# Main game loop

while True :
    
    for enemy in enemies :
        # move the enemy
        x = enemy.xcor()
        x = x + enemyspeed
        enemy.setx(x)

        # Moving enemy back
        if enemy.xcor() > 280 :
            for e in enemies :
               y = e.ycor()
               y -= 40
               e.sety(y)
            enemyspeed *= -1
        if enemy.xcor() < -280 :
            for e in enemies :
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

            # Check for a collision between the bullet and enemy
        if is_collision (bullet , enemy) :
            winsound.PlaySound("explosion.wav" , winsound.SND_FILENAME)
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0 , -400)

            # Reset the enemy
            x = random.randint(-200 , 220)
            y = random.randint(100 , 255)
            enemy.setposition(-x , y)

            # Update the score
            score += 10
            WS ()

        if is_collision (enemy , player) :
            player.hideturtle()
            enemy.hideturtle()
            print ("Game over")
            break
        

    # move the bullet
    if bulletstate == "fire" :
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Check the colloision border
    if bullet.ycor() > 275 :
        bullet.hideturtle()
        bulletstate = "ready"

    


delay = input ()

