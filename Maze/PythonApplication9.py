# A Simple Maze Game 
# First we need to set up th maze
import turtle
import random
import math
import winsound
import time

wn = turtle.Screen()
wn.title ("A Maze Game")
wn.bgcolor("black")
wn.setup(700 , 700)
#  Registering Shapes
wn.register_shape("player_l.gif")
wn.register_shape("player_r.gif")
wn.register_shape("enemy_r.gif")
wn.register_shape("enemy_l.gif")
wn.register_shape("treasuer.gif")

wn.tracer(0)

# Class lolies
class Lolies (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed(0)
# Create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


class Player (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("player_r.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up (self):
        move_to_x = self.xcor()
        move_to_y = self.ycor()+24
        if is_no_walls(move_to_x , move_to_y) :
            self.goto(self.xcor() , self.ycor()+24)

    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor()-24
        if is_no_walls(move_to_x , move_to_y) :
            self.goto(self.xcor() , self.ycor()-24)

    def go_right (self):
        self.shape("player_r.gif")
        move_to_x = self.xcor()+24
        move_to_y = self.ycor()
        if is_no_walls(move_to_x , move_to_y) :
            self.goto(self.xcor() + 24 , self.ycor())

    def go_left(self):
        self.shape("player_l.gif")
        move_to_x = self.xcor()-24
        move_to_y = self.ycor()
        if is_no_walls(move_to_x , move_to_y) :
            self.goto(self.xcor() - 24 , self.ycor())
    def is_collision (self , other) :
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt( (a**2) + (b**2) )

        if distance < 5:
            return True
        else :
            return False

#class Treasuer 
class Treasuer(turtle.Turtle):
    def __init__(self , x , y):
        turtle.Turtle.__init__(self)
        self.shape("treasuer.gif")
        self.speed(0)
        self.color("gold")
        self.penup()
        self.gold = 100
        self.goto(x , y)

    def destroy (self):
        self.goto(2000 , 2000)
        self.hideturtle()

    def replace(self):
        
        self.goto(0 ,0)

class Enemy(turtle.Turtle):
    def __init__(self,x, y):
        turtle.Turtle.__init__(self)
        self.shape("enemy_r.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x,y)
        self.direction = random.choice(["Up", "Down", "Left", "Right"])

        # Vérifie si le joueur est à proximité du danger
    def is_close(self, other):
        a = self.xcor() - other.xcor()
        b = self.xcor() - other.ycor()
        distance = math.sqrt((a ** 2) + math.sqrt(b ** 2))
        if distance < 5:
            return True
        else:
            return False
    #Fonction définissant le mouvement, d'après le choix aléatoire exprimé dans random.choice.
    #Chaque mouvement correspond à une case
    def move(self):
        if self.direction == "Up":
            dx = 0
            dy = 24
        elif self.direction == "Down":
            dx = 0
            dy = -24
        elif self.direction == "Left":
            self.shape("enemy_l.gif")
            dx = -24
            dy = 0
        elif self.direction == "Right":
            self.shape("enemy_r.gif")
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0
        #Calcule le point vers lequel se rendre
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        #Rapproche le danger du Joueur
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "Left"
            elif player.xcor() >self.xcor():
                self.direction == "Right"
            elif player.ycor() < self.ycor():
                self.direction == "Down"
            elif player.ycor() > self.ycor():
                self.direction == "Up"

        #Fonction pour s'assurer que le danger ne rencontre pas un mur
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        else:
            self.direction = self.direction = random.choice(["Up", "Down", "Left", "Right"])

        #Mise en place d'un timer pour faire bouger le danger
        turtle.ontimer(self.move, t = random.randint(100,300))

        #Possibilité de détruire le danger
        def destroy(self):
            self.goto(2000, 2000)
            self.hideturtle()



def is_no_walls (mx , my):
    if (mx, my) not in walls :
        return True
    else :
        return False
# Create lists
levels = [""]
walls = []
enemies = []


# define the first level
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXX",
    "XP  XXXXX N       XXXXXX",
    "X   XXXXX  XXXX   XXXXXX",
    "X      XX  XXXX      XXX",
    "X      XX  XXXX     TXXX",
    "XXXXX  XX  XXX    XXXXXX",
    "XXXXX  XX  XXXXX  XXXXXX",
    "XXXXX  XX    XXX  XXXXXX",
    "X  XX        XXX  XXXXXX",
    "X  XX   XXXXXXXXXXXXXXXX",
    "X         XXXXXXXXXXXXXX",
    "X             XXXXXXXXXX",
    "XXXXXXXXX      XXXX N XX",
    "XXXXXXXXXXX    XXXX    X",
    "XXX  XXXXXXXX          X",
    "XXXX    N              X",
    "XXXX           XXXXXXXXX",
    "XXXXXXXXXX   XXXXXXXXXXX",
    "XXXXXXXXXX           N X",
    "XX    XXXX             X",
    "XX    XXXXXXXXXX   XXXXX",
    "XX     XXXXXXXXX   XXXXX",
    "XX        NXXX         X",
    "XXXX                   X",
    "XXXXXXXXXXXXXXXXXXXXXXXX" ]

# Mode 2 Survaiving
level_2 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X    T   N                      X",
    "X                               X",
    "X            T              N   X",
    "X                               X",
    "X                               X",
    "X    T                          X",
    "X             N               N X",
    "X                               X",
    "X                       N       X",
    "X                               X",
    "X                               X",
    "X      N                        X",
    "X        T                      X",
    "X                               X",
    "X                         N     X",
    "X                               X",
    "X    N                   N      X",
    "X                               X",
    "X                N              X",
    "X                               X",    
    "X   T                           X",
    "X                              PX",                            
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ]

# Mode 3 Cute
level_3 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXX                        XXXXX",
    "XXXXX                        XXXXX",
    "XXXXXP          XX           XXXXX",
    "XXXXX          XXXX          XXXXX",
    "XXXXX         XXXXXX         XXXXX",
    "XXXXX     N  XXXXXXXX    N   XXXXX",
    "XXXXX       XXXXXXXXXX       XXXXX",
    "XXXXX      XXXXXXXXXXXX      XXXXX",
    "XXXXX     XXXXXXXXXXXXXX     XXXXX",
    "XXXXX    XXXXXXXXXXXXXXXX    XXXXX",
    "XXXXX   XXXXXXXXXXXXXXXXXX   XXXXX",
    "XXXXX                        XXXXX",
    "XXXXX            T           XXXXX",
    "XXXXX   XXXXXXXXXXXXXXXXXX   XXXXX",
    "XXXXX    XXXXXXXXXXXXXXXX    XXXXX",
    "XXXXX     XXXXXXXXXXXXXX     XXXXX",
    "XXXXX      XXXXXXXXXXXX      XXXXX",
    "XXXXX       XXXXXXXXXX       XXXXX",
    "XXXXX        XXXXXXXX        XXXXX",
    "XXXXX  N      XXXXXX    N    XXXXX",
    "XXXXX          XXXX          XXXXX",
    "XXXXX           XX       N   XXXXX",
    "XXXXX                        XXXXX",
    "XXXXX                        XXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ]

# Level 4 LOLIES
level_4 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"                                                                                                                                    ",
"                                                                                                                                    ",
"                                                                                                                                    ",
"LLL                          OOOOOOOOO               LLL                       III      EEEEEEEEEEEEEE              SSSS            ",
"LLL   			             O         O              LLL                       III      EEEEEEEEEEEEEE             SS               ",
"LLL                        O           O             LLL                       III      EEE                      SS                 ",
"LLL                       O             O            LLL                       III      EEE                    SS                   ",
"LLL                      O               O           LLL                       III      EEE                      SS                 ",
"LLL                     O                 O          LLL                       III      EEE                         SS              ",
"LLL                     O                 O          LLL                       III      EEEEEEEEEEEEEE                SS            ",
"LLL                     O                 O          LLL                       III      EEEEEEEEEEEEEE              SS            ",  
"LLL                     O                 O          LLL                       III      EEE                         SS              ",
"LLL                      O               O           LLL                       III      EEE                       SS                ",
"LLL                       O             O            LLL                       III      EEE                    SSS                  ",
"LLL                        O           O             LLL                       III      EEE                                         ",
"LLL                         O         O              LLL                       III      EEEEEEEEEEEEEE                              ",
"LLLLLLLLLLLLLLLLL            OOOOOOOOO               LLLLLLLLLLLLLLLLLLL       III      EEEEEEEEEEEEEE                              ",
"                                                                                                                                    ",
"                                                                                                                                    ",
"                                                                                                                                    ",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]
# Add treasures list
treasures = []
# Add level to mazes list
levels.append(level_1)
levels.append(level_2)
levels.append(level_3)
levels . append(level_4)
# Create Level setup func
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            # Get the char at x,y
            character = level[y][x]
            # Calculate the screen x , y cor
            global screen_x
            screen_x = -288 + (x*24)
            global screen_y
            screen_y = 288 - (y*24)

            # Check for X 
            if character == "X":
                pen.goto(screen_x , screen_y)
                pen.stamp()
                # Add X,Y coordinates to the 
                walls.append((screen_x , screen_y))

            if character =="P":
                player.goto(screen_x , screen_y)

            if character == "T":
                treasures.append(Treasuer(screen_x , screen_y))

            if character == "N" :
                enemies.append(Enemy(screen_x , screen_y))

            if character == "L" :
                lolies.goto(screen_x , screen_y)
                lolies.stamp()
                walls.append((screen_x , screen_y))

            if character == "O" :
                lolies.goto(screen_x , screen_y)
                lolies.stamp()
                walls.append((screen_x , screen_y))

            if character == "I" :
                lolies.goto(screen_x , screen_y)
                lolies.stamp()
                walls.append((screen_x , screen_y))

            if character == "E" :
                lolies.goto(screen_x , screen_y)
                lolies.stamp()
                walls.append((screen_x , screen_y))

            if character == "S" :
                lolies.goto(screen_x , screen_y)
                lolies.stamp()
                walls.append((screen_x , screen_y))

# Create Classes Instances
pen = Pen()
player = Player()
lolies = Lolies()
# Set up the level
print ("Hi bro! Mmm There Is Thee Modes Here To Play This Game")
print("For Normal Maze Press 1")
print("For Surviving Mode Press 2")
print("For The New Map Press 3 And Have Fun!")
print("Mmmm hello mina san ogikenyo we have added lolies map now to play with it press 4 and discover the power of the lolies hh nrm ;) ")
choise = input()
ch = int(choise)
if ch == 1:
    setup_maze(level_1)
elif ch == 2:
    setup_maze(level_2)
elif ch == 3:
    setup_maze(level_3)
elif ch == 4:
    setup_maze(level_4)

print (walls)
# Keyboard Binding
wn.listen()
wn.onkeypress(player.go_up , "w")
wn.onkeypress(player.go_down , "s")
wn.onkeypress(player.go_right , "d")
wn.onkeypress(player.go_left , "a")



# Start Moving The Enemies
for enemy in enemies :
        wn.ontimer(enemy.move , 250)

# Main Game Loop
while True:
    # Check for player collision with treasure
    for treasure in treasures :
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print ("PLAYER GOLD : {}".format(player.gold))
            # destroy the treasure from the treasurs list
            treasure.destroy()
            treasure.replace()

    for enemy in enemies:
        if player.is_collision(enemy):
            time.sleep(1)
            player.goto(-264 , 264)
            if player.gold >= 100 :
                player.gold -= 100
            else :
                player.hideturtle()
            if ch == 3 :
                player.goto(0 , 0)
            print("Player loose!")
            print ("PLAYER GOLD : {}".format(player.gold))
            break

    
    
        if player.is_collision(enemy):
            winsound.PlaySound("explosion.wav" , winsound.SND_FILENAME)
        
            if player.gold >= 100 :
                player.gold -= 100
                time.sleep(1)
                player.goto(-264 , 264)

            else :
                player.goto(1000 ,1000)
                player.hideturtle()


    wn.update()









