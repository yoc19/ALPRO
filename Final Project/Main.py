import turtle
import time
import Score

ground = -320	#Posisi untuk X paling bawah(ground)
speed = 5 		#Speed dari Player
floornum = 10	#List untuk membuat floor
gravity = -0.22	#Variabel pengubah gravitasi
door = [turtle.Turtle() for i in range(5)]		#Membuat sebuah list door
floor = [turtle.Turtle() for i in range(floornum)]	#Membuat sebuah list floor
deadzone = turtle.Turtle()
coin = [turtle.Turtle() for i in range(3)]
coinscore = 0
isCollected =[False for i in range(len(coin))]
isAlive = True
level = 1
lives = 3

#Screen
wn = turtle.Screen()
wn.title("2D Platformer")
wn.bgcolor("Black")
wn.setup(width=1440, height=900)
wn.tracer(0)
wn.colormode(255)
wn.listen()

#PLAYER
player = turtle.Turtle()
player.shape("circle")
player.color((116,188,255))
player.shapesize(2,2,1)
player.penup()
player.goto(-520,ground+40)
player.dx = 0
player.dy = 0
player.state ="ready"

for i in range(len(coin)):
    coin[i].shape("circle")
    coin[i].color("yellow")
    coin[i].penup()
    coin[i].shapesize(1.5,0.9)

def coinCheck():
    global level
    if level == 0:
        for i in range(len(coin)):
            coin[i].goto(1000,1000)
    if level == 1:
        if isCollected[0] == False:
            coin[0].goto(-500,ground+295)
        if isCollected[1] == False:
            coin[1].goto(30,ground+100)
        if isCollected[2] == False:
            coin[2].goto(500,ground+300)
    if level == 2:
        if isCollected[0] == False:
            coin[0].goto(-570,ground+375)
        if isCollected[1] == False:
            coin[1].goto(550,ground+280)
        if isCollected[2] == False:
            coin[2].goto(550,ground+500)
    if level == 3:
        if isCollected[0] == False:
            coin[0].goto(-550,ground+375)
        if isCollected[1] == False:
            coin[1].goto(500,ground+280)
        if isCollected[2] == False:
            coin[2].goto(500,ground+500)
    if level == 4:
        for i in range(len(coin)):
            coin[i].goto(1000,1000)

coinscoretext = turtle.Turtle()
coinscoretext.shape("square")
coinscoretext.color("white")
coinscoretext.penup()
coinscoretext.hideturtle()
coinscoretext.goto(600,400)
coinscoretext.write(f"Coins = {coinscore}", align="center", font=("Courier", 24, "normal"))

livescore = turtle.Turtle()
livescore.shape("square")
livescore.color("white")
livescore.penup()
livescore.hideturtle()
livescore.goto(-600,400)
livescore.write(f"Lives = {lives}", align="center", font=("Courier", 24, "normal"))

def Level(level):
    for i in range(floornum):
        floor[i].color("white")
        floor[i].hideturtle()
        floor[i].penup()
        floor[i].shape("square")
        deadzone.color("black")
        deadzone.shape("square")
        if level == 0:
            floor[0].st()
            floor[0].shapesize(2,75,1)
            floor[0].goto(0,ground)
        elif level == 1:
            floor[0].st()
            floor[1].st()
            floor[2].st()
            floor[3].st()
            floor[0].shapesize(2,75,1)
            floor[0].goto(0,ground)
            floor[1].shapesize(8,8,1)
            floor[1].goto(-100,ground+60)
            floor[2].shapesize(2,10,1)
            floor[2].goto(-500,ground+245)
            floor[3].shapesize(10,23,1)
            floor[3].goto(500,ground+100)
            deadzone.shapesize(2,14.4,1)
            deadzone.goto(125,ground)
            if player.xcor() < deadzone.xcor()+130 and player.xcor() > deadzone.xcor()-130 and player.ycor() < deadzone.ycor()+50:
                dead(1)

        elif level == 2:
            floor[0].showturtle()
            floor[1].showturtle()
            floor[2].showturtle()
            floor[3].showturtle()
            floor[4].showturtle()
            floor[5].showturtle()
            floor[6].showturtle()
            floor[0].shapesize(2,75,1)
            floor[0].goto(0,ground)
            floor[1].shapesize(8,45,1)
            floor[1].goto(0,ground+60)
            floor[2].shapesize(8,30,1)
            floor[2].goto(0,ground+170)
            floor[3].shapesize(1.3,9,1)
            floor[3].goto(-570,ground+340)
            floor[4].shapesize(1.3,9,1)
            floor[4].goto(-200,ground+450)
            floor[5].shapesize(1.3,9,1)
            floor[5].goto(200,ground+480)
            floor[6].shapesize(1.3,9,1)
            floor[6].goto(550,ground+550)
            deadzone.shapesize(2,14.4,1)
            deadzone.goto(595,ground)
            if player.xcor() < deadzone.xcor()+130 and player.xcor() > deadzone.xcor()-130 and player.ycor() < deadzone.ycor()+50:
                dead(2)

        elif level == 3:
            floor[0].showturtle()
            floor[1].showturtle()
            floor[2].showturtle()
            floor[3].showturtle()
            floor[4].showturtle()
            floor[5].showturtle()
            floor[6].showturtle()
            floor[7].showturtle()
            floor[8].showturtle()
            floor[9].showturtle()
            floor[0].goto(0,ground+300)
            floor[0].shapesize(28,2,1)
            floor[1].goto(500,ground+100)
            floor[1].shapesize(1.2,8,1)
            floor[2].goto(250,ground+230)
            floor[2].shapesize(1.2,8,1)
            floor[3].goto(120,ground+350)
            floor[3].shapesize(1.2,8,1)
            floor[4].goto(120,ground+470)
            floor[4].shapesize(1.2,8,1)
            floor[5].goto(-500,ground+550)
            floor[5].shapesize(1.2,8,1)
            floor[6].goto(-500,ground+100)
            floor[6].shapesize(1.2,8,1)
            floor[7].goto(-250,ground+230)
            floor[7].shapesize(1.2,8,1)
            floor[8].goto(-120,ground+350)
            floor[8].shapesize(1.2,8,1)
            floor[9].goto(-120,ground+470)
            floor[9].shapesize(1.2,8,1)
            deadzone.shapesize(2,75,1)
            deadzone.goto(0,ground)
            if player.ycor() < ground+50:
                dead(3)
        
        elif level == 4:
            deadzone.ht()
            floor[0].showturtle()
            floor[0].goto(0,ground+100)
            floor[0].shapesize(2,75,1)

def doorspawn():
    global level
    for i in range(5):
        door[i].color("red")
        door[i].penup()
        door[i].shape("square")
        door[i].shapesize(8,5,1)
        if level == 0:
            door[0].ht()
            door[1].goto(-320,ground+100)
            door[2].goto(0,ground+100)
            door[3].goto(320,ground+100)
        if level == 1:
            door[i].goto(1000,1000)
            for i in isCollected:
                if i == True:
                    door[2].goto(600,ground+250)
        if level == 2:
            door[i].goto(1000,1000)
            for i in isCollected:
                if i == True:
                    door[3].goto(550,ground+640)
        if level == 3:
            door[i].goto(1000,1000)
            for i in isCollected:
                if i == True:
                    door[4].goto(-500,ground+640)
        if level == 4:
            door[i].goto(1000,1000)

def dead(stage):
    global lives
    lives -=1
    if stage == 1:
        player.goto(-620,ground+40)
    if stage == 2:
        player.goto(-620,ground+40)
    if stage == 3:
        player.goto(620,ground+600)
    livescore.clear()
    livescore.write(f"Lives = {lives}", align="center", font=("Courier", 24, "normal"))
    if lives < 1:
        gameover()

def gameover():
    global gravity
    global isAlive
    global level
    gravity = 0
    player.reset()
    isAlive = False
    level = 4
    text = turtle.Turtle()
    text.shape("square")
    text.color("white")
    text.penup()
    text.hideturtle()
    text.goto(0,0)
    text.write(f"Game Over", align="center", font=("Courier", 50, "normal"))
    

def thedoor():
    for i in range(5):
        if player.xcor() > door[i].xcor()-50 and player.xcor() < door[i].xcor()+50 and player.ycor() > door[i].ycor()-100 and player.ycor() < door[i].ycor() + 100:
            door[i].color("white")

def jump():
	if player.state =="ready":
		player.dy = 7.5
		player.state="jumping"

def right():
    player.dx = 5

def left():
    player.dx = -5

def release():
    player.dx = 0

def levelchange():
    global level
    for i in range(5):
        if player.xcor() > door[i].xcor()-50 and player.xcor() < door[i].xcor()+50 :
            level = i
            isCollected[0]= False
            isCollected[1]= False
            isCollected[2]= False
            if level == 1 or level == 2:
                player.goto(-600,ground+40)
            if level == 3:
                player.goto(600,ground+500)
            if level == 4:
                Win()

def Win():
    global lives
    global coin
    score = lives + coinscore
    name = wn.textinput("PLAYER'S NAME","Player's Name : ")
    text = turtle.Turtle()
    text.shape("square")
    text.color("white")
    text.penup()
    text.hideturtle()
    text.goto(0,0)
    text.write(f"{name}'s Score = {score}", align="center", font=("Courier", 25, "normal"))
    Score.save(name,score)
    wn.listen()


#Input keyboard
wn.onkeypress(jump,"space")
wn.onkeypress(right,"d")
wn.onkeyrelease(release,"d")
wn.onkeypress(left,"a")
wn.onkeyrelease(release,"a")
wn.onkeypress(levelchange,"f")

#MAIN CALL
while True:
    wn.update()
    time.sleep(0.001)
    Level(level)
    doorspawn()
    thedoor()
    coinCheck()

    for i in range(len(coin)):
        if player.distance(coin[i]) < 15 :
            coin[i].goto(1000,1000)
            isCollected[i] = True
            coinscore+=1
            coinscoretext.clear()
            coinscoretext.write(f"Coins = {coinscore}", align="center", font=("Courier", 24, "normal"))

    #GRAVITY
    player.dy += gravity

    #JUMP
    y = player.ycor()
    y += player.dy
    player.sety(y)

    #MOVING
    x = player.xcor()
    x += player.dx
    player.setx(x)

    #Grounded
    if player.ycor() < ground+40 :
        player.sety(ground+40)
        player.dy = 0
        player.state = "ready"
    
    #SCREEN BOUNDARIES
    if player.xcor() < -696:
        player.setx(-696)
    if player.xcor() > 690:
        player.setx(690)
    
    if level == 1:
        floorxpos = [100,120,250]
        floorypos = [100,39,120]
        for i in range(1,4):
            if player.xcor() < floor[i].xcor()+floorxpos[i-1] and player.xcor() > floor[i].xcor()-floorxpos[i-1] and player.ycor() < floor[i].ycor()+floorypos[i-1]:
            #CheckLeftSide || if (membatasi atas) and (membatasi bawah) and (check bila berada di kiri)
                if player.ycor() < floor[i].ycor()+(floorypos[i-1]-10) and player.ycor() > floor[i].ycor()-(floorypos[i-1]-10) and player.xcor() - floor[i].xcor() < 0:
                    player.setx(floor[i].xcor()-floorxpos[i-1])
                #CheckRightSide || if (membatasi atas) and (membatasi bawah) and (check bila berada di kanan)
                if player.ycor() < floor[i].ycor()+(floorypos[i-1]-10) and player.ycor() > floor[i].ycor()-(floorypos[i-1]-10) and player.xcor() - floor[i].xcor() > 0:
                    player.setx(floor[i].xcor()+floorxpos[i-1])
                #CheckOnTop
                if player.ycor() < floor[i].ycor()+floorypos[i-1] and player.ycor() > floor[i].ycor()-floorypos[i-1] and player.xcor() < floor[i].xcor()+(floorxpos[i-1]-10) and player.xcor() > floor[i].xcor()-(floorxpos[i-1]-10):
                    if player.ycor() - floor[i].ycor() > 0:
                        player.sety(floor[i].ycor()+floorypos[i-1])
                        player.dy = 0
                        player.state ="ready"
                    elif player.ycor() - floor[i].ycor() < 0:
                        player.sety(floor[i].ycor()-floorypos[i-1])
                        player.dy = 0
    elif level ==2:
        floorxpos = [470,320,110,110,110,110,0]
        floorypos = [100,100,32,32,32,32,0]
        for i in range(1,7):
            if player.xcor() < floor[i].xcor()+floorxpos[i-1] and player.xcor() > floor[i].xcor()-floorxpos[i-1] and player.ycor() < floor[i].ycor()+floorypos[i-1]:
            #CheckLeftSide || if (membatasi atas) and (membatasi bawah) and (check bila berada di kiri)
                if player.ycor() < floor[i].ycor()+(floorypos[i-1]-10) and player.ycor() > floor[i].ycor()-(floorypos[i-1]-10) and player.xcor() - floor[i].xcor() < 0:
                    player.setx(floor[i].xcor()-floorxpos[i-1])
                #CheckRightSide || if (membatasi atas) and (membatasi bawah) and (check bila berada di kanan)
                if player.ycor() < floor[i].ycor()+(floorypos[i-1]-10) and player.ycor() > floor[i].ycor()-(floorypos[i-1]-10) and player.xcor() - floor[i].xcor() > 0:
                    player.setx(floor[i].xcor()+floorxpos[i-1])
                #CheckOnTop
                if player.ycor() < floor[i].ycor()+floorypos[i-1] and player.ycor() > floor[i].ycor()-floorypos[i-1] and player.xcor() < floor[i].xcor()+(floorxpos[i-1]-10) and player.xcor() > floor[i].xcor()-(floorxpos[i-1]-10):
                    if player.ycor() - floor[i].ycor() > 0:
                        player.sety(floor[i].ycor()+floorypos[i-1])
                        player.dy = 0
                        player.state ="ready"
                    elif player.ycor() - floor[i].ycor() < 0:
                        player.sety(floor[i].ycor()-floorypos[i-1])
                        player.dy = 0
    elif level ==3:
        floorxpos = [40,100,100,100,100,100,100,100,100,100]
        floorypos = [300,32,32,32,32,32,32,32,32,32]
        for i in range(10):
            if player.xcor() < floor[i].xcor()+floorxpos[i] and player.xcor() > floor[i].xcor()-floorxpos[i] and player.ycor() < floor[i].ycor()+floorypos[i]:
            #CheckLeftSide || if (membatasi atas) and (membatasi bawah) and (check bila berada di kiri)
                if player.ycor() < floor[i].ycor()+(floorypos[i]-10) and player.ycor() > floor[i].ycor()-(floorypos[i]-10) and player.xcor() - floor[i].xcor() < 0:
                    player.setx(floor[i].xcor()-floorxpos[i])
                #CheckRightSide || if (membatasi atas) and (membatasi bawah) and (check bila berada di kanan)
                if player.ycor() < floor[i].ycor()+(floorypos[i]-10) and player.ycor() > floor[i].ycor()-(floorypos[i]-10) and player.xcor() - floor[i].xcor() > 0:
                    player.setx(floor[i].xcor()+floorxpos[i])
                #CheckOnTop
                if player.ycor() < floor[i].ycor()+floorypos[i] and player.ycor() > floor[i].ycor()-floorypos[i] and player.xcor() < floor[i].xcor()+(floorxpos[i]-10) and player.xcor() > floor[i].xcor()-(floorxpos[i]-10):
                    if player.ycor() - floor[i].ycor() > 0:
                        player.sety(floor[i].ycor()+floorypos[i])
                        player.dy = 0
                        player.state ="ready"
                    elif player.ycor() - floor[i].ycor() < 0:
                        player.sety(floor[i].ycor()-floorypos[i-1])
                        player.dy = 0
    elif level == 4:
        if player.ycor() < floor[0].ycor() + 40:
            player.sety(floor[0].ycor() + 40)
            player.state ="ready"