import turtle as t

# Les jeux

def jeu1joueur():

    import turtle
    import time
    import random

    sc = turtle.Screen()
    sc.bgcolor("black")
    sc.reset() 
    sc.screensize(1000,560)
    sc.tracer(0)

    # Creation des mannettes

    mannette1 = turtle.Turtle()
    mannette1.pu()
    mannette1.shape("square")
    mannette1.shapesize(10,1)
    mannette1.color("white")
    mannette1.setx(940)

    mannette2 = turtle.Turtle()
    mannette2.pu()
    mannette2.shape("square")
    mannette2.shapesize(10,1)
    mannette2.color("white")
    mannette2.setx(-947)

    # Creation de la balle

    balle = turtle.Turtle()
    balle.pu()
    balle.shape("circle")
    balle.color("white")

    # Fonctions et definitions

    def up1():
        mannette1.sety(mannette1.ycor()+150)

    def down1():
        mannette1.sety(mannette1.ycor()-150)

    movx = -2
    movy = 0

    point = 0
    score = 0

    time.sleep(3)

    # Jeu

    while True:
        a = mannette1.ycor()

        sc.update()
        sc.listen()
        sc.onkeypress(up1, "Up")
        sc.onkeypress(down1, "Down")

        # Ordinateur

        rand = random.randrange(-14,14)
        mannette2_velocity = rand/40

        if mannette2.ycor() < 405 and mannette2.ycor() > -395:
            mannette2.sety(balle.ycor())

        if mannette2.ycor() > 405:
            mannette2.sety(404)

        if mannette2.ycor() < -395:
            mannette2.sety(-394)

        # Mouvement de la balle

        yvel = balle.ycor()+movy
        xvel = balle.xcor()+movx
        balle.sety(yvel)
        balle.setx(xvel)

        # Rebondissement de la balle: Plafond et Plancher

        if balle.ycor() > 495:
            balle.sety(495)
            movy = movy*-1

        if balle.ycor() < -490:
            balle.sety(-490)
            movy = movy*-1

        # Rebondissement de la balle: Ouest et Est

        if balle.xcor() > 999:
            balle.setpos(0,0)
            mannette1.sety(0)
            time.sleep(0.5)
            movx = -2
            movy = 0

            point += 1

            if score == 1:
                score = sc.textinput("Pointage", str(point) +" point, vs 0 points")
            else:
                score = sc.textinput("Pointage", str(point) +" points, vs 0 points")

        # Mannette out of bounds verification

        if mannette1.xcor() != 940:
            mannette1.setx(940)
        if mannette2.xcor() != -947:
            mannette2.setx(-947)

        # Courbure de la balle: MANNETTE VELOCITY CHECK: Mannette1

        b = mannette1.ycor()
        distance_man1 = a-b
        if distance_man1 != 0:
            distance_man1 = -distance_man1
            mannette1_velocity = float(distance_man1)/20
        else:
            mannette1_velocity = 0

        # Courbure de la balle: Mannette1

        if mannette1_velocity != 0:
            if balle.xcor() > 920 and balle.xcor() < 935 and balle.ycor() < mannette1.ycor()+110 and balle.ycor() > mannette1.ycor()-110:
                balle.setx(920)
                movx = movx * -1

                # Pour que la balle va dans la direction du "velocity" de la mannette.
                
                if mannette1_velocity < 0:
                    movy = -1
                if mannette1_velocity > 0:
                    movy = 1

                while not (balle.xcor() < -930 and balle.xcor() > -935 and balle.ycor() < mannette2.ycor()+110 and balle.ycor() > mannette2.ycor()-110):
                    sc.update()

                    # Ordinateur
        
                    if mannette2.ycor() < 405 and mannette2.ycor() > -395:
                        mannette2.sety(balle.ycor())

                    if mannette2.ycor() > 405:
                        mannette2.sety(404)

                    if mannette2.ycor() < -395:
                        mannette2.sety(-394)

                    # Mouvement de la balle

                    movy = movy-mannette1_velocity/100

                    yvel = balle.ycor()+movy
                    xvel = balle.xcor()+movx
                    balle.sety(yvel)
                    balle.setx(xvel)

                    # Rebondissement de la balle: Plafond et Plancher

                    if balle.ycor() > 495:
                        balle.sety(495)
                        movy = movy*-1

                    if balle.ycor() < -490:
                        balle.sety(-490)
                        movy = movy*-1

                    # Pour que les mannettes restes dans leurs axe  

                    if mannette1.xcor() != 940:
                        mannette1.setx(940)
                    if mannette2.xcor() != -947:
                        mannette2.setx(-947)

                    # Mannette out of bounds check

                    if mannette1.ycor() > 405:
                        mannette1.sety(405)

                    if mannette1.ycor() < -395:
                        mannette1.sety(-395)

                    if mannette2.ycor() > 405:
                        mannette2.sety(404)

                    if mannette2.ycor() < -395:
                        mannette2.sety(-394)

                    # Rebondissement de la balle: Ouest et Est

                    if balle.xcor() > 999 or balle.xcor() < -999:
                        mannette1.sety(0)
                        break

            # Courbure de la balle: Mannette2

        if mannette2_velocity != 0:
            if balle.xcor() < -930 and balle.xcor() > -935 and balle.ycor() < mannette2.ycor()+110 and balle.ycor() > mannette2.ycor()-110:

                balle.setx(-930)
                movx = movx*-1

                # Pour que la balle va dans la direction du "velocity" de la mannette.

                if mannette2_velocity < 0:
                    movy = -1
                if mannette2_velocity > 0:
                    movy = 1

                while not (balle.xcor() > 920 and balle.xcor() < 935 and balle.ycor() < mannette1.ycor()+110 and balle.ycor() > mannette1.ycor()-110):
                    sc.update()

                    # Ordinateur
        
                    if mannette2.ycor() < 405 and mannette2.ycor() > -395:
                        mannette2.sety(balle.ycor())

                    if mannette2.ycor() > 405:
                        mannette2.sety(404)

                    if mannette2.ycor() < -395:
                        mannette2.sety(-394)

                    # Mouvement de la balle

                    movy = movy-mannette2_velocity/100

                    yvel = balle.ycor()+movy
                    xvel = balle.xcor()+movx
                    balle.sety(yvel)
                    balle.setx(xvel)

                    # Rebondissement de la balle: Plafond et Plancher

                    if balle.ycor() > 495:
                        balle.sety(495)
                        movy = movy*-1

                    if balle.ycor() < -490:
                        balle.sety(-490)
                        movy = movy*-1

                    # Pour que les mannettes restes dans leurs axe  

                    if mannette1.xcor() != 940:
                        mannette1.setx(940)
                    if mannette2.xcor() != -947:
                        mannette2.setx(-947)

                    # Mannette out of bounds check

                    if mannette1.ycor() > 405:
                        mannette1.sety(404)

                    if mannette1.ycor() < -395:
                        mannette1.sety(-394)

                    if mannette2.ycor() > 405:
                        mannette2.sety(404)

                    if mannette2.ycor() < -395:
                        mannette2.sety(-394)

                    # Rebondissement de la balle: Ouest et Est

                    if balle.xcor() > 999:
                        mannette1.sety(0)
                        break

        # Rebondissement de la balle: Mannette1
        if mannette1_velocity == 0:
            if balle.xcor() > 930 and balle.xcor() < 935 and balle.ycor() < mannette1.ycor()+110 and balle.ycor() > mannette1.ycor()-110:
                balle.setx(930)
                movx = movx*-1

        # Rebondissement de la balle: Mannette2
        if mannette2_velocity == 0:
            if balle.xcor() < -930 and balle.xcor() > -935 and balle.ycor() < mannette2.ycor()+110 and balle.ycor() > mannette2.ycor()-110:
                balle.setx(-930)
                movx = movx*-1

        # Mannette out of bounds check

        if mannette1.ycor() > 405:
            mannette1.sety(404)

        if mannette1.ycor() < -395:
            mannette1.sety(-394)

        if mannette2.ycor() > 405:
            mannette2.sety(404)

        if mannette2.ycor() < -395:
            mannette2.sety(-394)

        # Mannette avec souris

        mannette1.ondrag(mannette1.goto)     

def jeu2joueurs():
    import turtle
    import time
    import random

    sc = turtle.Screen()
    sc.bgcolor("black")
    sc.reset()
    sc.screensize(1000,560)
    sc.tracer(0)

    # Creation des mannettes

    mannette1 = turtle.Turtle()
    mannette1.pu()
    mannette1.shape("square")
    mannette1.shapesize(10,1)
    mannette1.color("white")
    mannette1.setx(940)

    mannette2 = turtle.Turtle()
    mannette2.pu()
    mannette2.shape("square")
    mannette2.shapesize(10,1)
    mannette2.color("white")
    mannette2.setx(-947)

    # Creation de la balle

    balle = turtle.Turtle()
    balle.pu()
    balle.shape("circle")
    balle.color("white")

    # Fonctions et definitions

    def up1():
        mannette1.sety(mannette1.ycor()+150)

    def down1():
        mannette1.sety(mannette1.ycor()-150)

    def up2():
        mannette2.sety(mannette2.ycor()+150)

    def down2():
        mannette2.sety(mannette2.ycor()-150)

    movx = 2
    movy = 0

    pointman1 = 0
    pointman2 = 0
    score = 0

    time.sleep(3)

    # Jeu

    while True:
        # Premiere valeure pour le velocity check
        a = mannette1.ycor()
        s = mannette2.ycor()

        sc.update()
        sc.listen()
        sc.onkeypress(up1, "Up")
        sc.onkeypress(down1, "Down")
        sc.onkeypress(up2, "w")
        sc.onkeypress(down2, "s")

        # Mouvement de la balle

        yvel = balle.ycor()+movy
        xvel = balle.xcor()+movx
        balle.sety(yvel)
        balle.setx(xvel)

        # Rebondissement de la balle: Plafond et Plancher

        if balle.ycor() > 495:
            balle.sety(495)
            movy = movy*-1

        if balle.ycor() < -490:
            balle.sety(-490)
            movy = movy*-1

        # Rebondissement de la balle: Est

        if balle.xcor() > 999:
            balle.setpos(0,0)
            mannette1.sety(0)
            mannette2.sety(0)
            time.sleep(0.5)
            movx = 2
            movy = 0
            # Pointage mannette 1
            pointman2 += 1

            if pointman2 == 1 and pointman1 == 1:
                score = sc.textinput("Pointage", str(pointman2) +" point, vs "+str(pointman1)+" point")

            elif pointman2 != 1 and pointman1 == 1:
                score = sc.textinput("Pointage", str(pointman2) +" points, vs "+str(pointman1)+" point")

            elif pointman2 == 1 and pointman1 != 1:
                score = sc.textinput("Pointage", str(pointman2) +" point, vs "+str(pointman1)+" points")

            elif pointman2 != 1 and pointman1 != 1:
                score = sc.textinput("Pointage", str(pointman2) +" points, vs "+str(pointman1)+" points")
        
        # Rebondissement de la balle: Est
        if balle.xcor() < -999:
            balle.setpos(0,0)
            mannette1.sety(0)
            mannette2.sety(0)
            time.sleep(0.5)
            movx = -2
            movy = 0
            # Pointage mannette 2
            pointman1 += 1

            if pointman2 == 1 and pointman1 == 1:
                score = sc.textinput("Pointage", str(pointman2) +" point, vs "+str(pointman1)+" point")

            elif pointman2 != 1 and pointman1 == 1:
                score = sc.textinput("Pointage", str(pointman2) +" points, vs "+str(pointman1)+" point")

            elif pointman2 == 1 and pointman1 != 1:
                score = sc.textinput("Pointage", str(pointman2) +" point, vs "+str(pointman1)+" points")

            elif pointman2 != 1 and pointman1 != 1:
                score = sc.textinput("Pointage", str(pointman2) +" points, vs "+str(pointman1)+" points")

        # Mannette out of bounds verification

        if mannette1.xcor() != 940:
            mannette1.setx(940)
        if mannette2.xcor() != -947:
            mannette2.setx(-947)

        # Courbure de la balle: MANNETTE VELOCITY CHECK: Mannette1

        b = mannette1.ycor()
        distance_man1 = a-b
        if distance_man1 != 0:
            distance_man1 = -distance_man1
            mannette1_velocity = float(distance_man1)/20
        else:
            mannette1_velocity = 0

        # Courbure de la balle: Mannette1

        if mannette1_velocity != 0:
            if balle.xcor() > 920 and balle.xcor() < 935 and balle.ycor() < mannette1.ycor()+110 and balle.ycor() > mannette1.ycor()-110:
                balle.setx(920)
                movx = -2

                # Pour que la balle va dans la direction du "velocity" de la mannette.
                
                if mannette1_velocity < 0:
                    movy = -1
                if mannette1_velocity > 0:
                    movy = 1

                while not (balle.xcor() < -925 and balle.xcor() > -935 and balle.ycor() < mannette2.ycor()+110 and balle.ycor() > mannette2.ycor()-110):
                    sc.update()

                    # Mouvement de la balle

                    movy = movy-mannette1_velocity/100

                    yvel = balle.ycor()+movy
                    xvel = balle.xcor()+movx
                    balle.sety(yvel)
                    balle.setx(xvel)

                    # Rebondissement de la balle: Plafond et Plancher

                    if balle.ycor() > 495:
                        balle.sety(495)
                        movy = movy*-1

                    if balle.ycor() < -490:
                        balle.sety(-490)
                        movy = movy*-1

                    # Pour que les mannettes restes dans leurs axe  

                    if mannette1.xcor() != 940:
                        mannette1.setx(940)
                    if mannette2.xcor() != -947:
                        mannette2.setx(-947)

                    # Mannette out of bounds check

                    if mannette1.ycor() > 405:
                        mannette1.sety(404)

                    if mannette1.ycor() < -395:
                        mannette1.sety(-394)

                    if mannette2.ycor() > 405:
                        mannette2.sety(404)

                    if mannette2.ycor() < -395:
                        mannette2.sety(-394)

                    # Rebondissement de la balle: Ouest et Est

                    if balle.xcor() > 999 or balle.xcor() < -999:
                        mannette1.sety(0)
                        mannette2.sety(0)
                        break

        # Courbure de la balle: MANNETTE VELOCITY CHECK: Mannette2

        t = mannette2.ycor()
        distance_man2 = s-t
        if distance_man2 != 0:
            distance_man2 = -distance_man2
            mannette2_velocity = float(distance_man2)/20

            if mannette2_velocity > 0.80:
                mannette2_velocity = random.uniform(0.6)
            if mannette2_velocity < -0.80:
                mannette2_velocity = -0.80

        else:
            mannette2_velocity = 0

        # Courbure de la balle: Mannette2

        if mannette2_velocity != 0:
            if balle.xcor() < -925 and balle.xcor() > -935 and balle.ycor() < mannette2.ycor()+110 and balle.ycor() > mannette2.ycor()-110:
                balle.setx(-925)
                movx=movx*-1
                print(mannette2_velocity)
                # Pour que la balle va dans la direction du "velocity" de la mannette.
                
                if mannette2_velocity < 0:
                    movy = -1
                if mannette2_velocity > 0:
                    movy = 1

                while not (balle.xcor() > 920 and balle.xcor() < 935 and balle.ycor() < mannette1.ycor()+110 and balle.ycor() > mannette1.ycor()-110):
                    sc.update()

                    # Mouvement de la balle

                    movy = movy-mannette2_velocity/100

                    yvel = balle.ycor()+movy
                    xvel = balle.xcor()+movx
                    balle.sety(yvel)
                    balle.setx(xvel)

                    # Rebondissement de la balle: Plafond et Plancher

                    if balle.ycor() > 495:
                        balle.sety(495)
                        movy = movy*-1

                    if balle.ycor() < -490:
                        balle.sety(-490)
                        movy = movy*-1

                    # Pour que les mannettes restes dans leurs axe  

                    if mannette1.xcor() != 940:
                        mannette1.setx(940)
                    if mannette2.xcor() != -947:
                        mannette2.setx(-947)

                    # Mannette out of bounds check

                    if mannette1.ycor() > 405:
                        mannette1.sety(404)

                    if mannette1.ycor() < -395:
                        mannette1.sety(-394)

                    if mannette2.ycor() > 405:
                        mannette2.sety(404)

                    if mannette2.ycor() < -395:
                        mannette2.sety(-394)

                    # Rebondissement de la balle: Ouest et Est

                    if balle.xcor() > 999 or balle.xcor() < -999:
                        mannette1.sety(0)
                        mannette2.sety(0)
                        break

        # Rebondissement de la balle: Mannette1

        if balle.xcor() > 922 and balle.xcor() < 935 and balle.ycor() < mannette1.ycor()+110 and balle.ycor() > mannette1.ycor()-110:
            balle.setx(921)
            movx = movx*-1

        # Rebondissement de la balle: Mannette2

        if balle.xcor() < -925 and balle.xcor() > -935 and balle.ycor() < mannette2.ycor()+110 and balle.ycor() > mannette2.ycor()-110:
            balle.setx(-925)
            movx = movx*-1

        # Mannette out of bounds check

        if mannette1.ycor() > 405:
            mannette1.sety(404)

        if mannette1.ycor() < -395:
            mannette1.sety(-394)

        if mannette2.ycor() > 405:
            mannette2.sety(404)

        if mannette2.ycor() < -395:
            mannette2.sety(-394)

        # Mannette avec souris

        mannette1.ondrag(mannette1.goto)
        mannette2.ondrag(mannette2.goto)

def jeu0joueurs():

    import turtle
    import time
    import random

    sc = turtle.Screen()
    sc.bgcolor("black")
    sc.reset() 
    sc.screensize(1000,560)
    sc.tracer(0)

    # Creation des mannettes

    mannette1 = turtle.Turtle()
    mannette1.pu()
    mannette1.shape("square")
    mannette1.shapesize(10,1)
    mannette1.color("white")
    mannette1.setx(940)

    mannette2 = turtle.Turtle()
    mannette2.pu()
    mannette2.shape("square")
    mannette2.shapesize(10,1)
    mannette2.color("white")
    mannette2.setx(-947)

    # Creation de la balle

    balle = turtle.Turtle()
    balle.pu()
    balle.shape("circle")
    balle.color("white")

    # Fonctions et definitions

    movx = 2
    movy = 0

    pointman1 = 0
    pointman2 = 0
    score = 0

    rand3 = random.uniform(-10,10)
    rand4 = random.uniform(-10,10)

    # Jeu

    while True:

        sc.update()

        # Ordinateur #1

        rand1 = random.randrange(-14,14)

        mannette1_velocity = rand1/80

        dist1 = (balle.xcor()-940)/rand3

        mannette1.sety(balle.ycor()-dist1)

        if mannette1.ycor() > 405:
            mannette1.sety(404)

        if mannette1.ycor() < -395:
            mannette1.sety(-394)

        # Ordinateur #2

        rand2 = random.randrange(-14,14)

        mannette2_velocity = rand2/80

        dist2 = (balle.xcor()+940)/rand4

        mannette2.sety(balle.ycor()+dist2)

        if mannette2.ycor() > 405:
            mannette2.sety(404)

        if mannette2.ycor() < -395:
            mannette2.sety(-394)

        # Mouvement de la balle

        yvel = balle.ycor()+movy
        xvel = balle.xcor()+movx
        balle.sety(yvel)
        balle.setx(xvel)

        # Rebondissement de la balle: Plafond et Plancher

        if balle.ycor() > 495:
            balle.sety(495)
            movy = movy*-1

        if balle.ycor() < -490:
            balle.sety(-490)
            movy = movy*-1

        # Rebondissement de la balle: Ouest et Est

        if balle.xcor() > 999:
            rand4 = random.uniform(-10,10)
            rand3 = random.uniform(-10,10)
            balle.setpos(0,0)
            time.sleep(0.5)
            movx = 2
            movy = 0

            pointman2 += 1

            if pointman2 == 1 and pointman1 == 1:
                score = sc.textinput("Pointage", str(pointman2) +" point, vs "+str(pointman1)+" point")

            elif pointman2 != 1 and pointman1 == 1:
                score = sc.textinput("Pointage", str(pointman2) +" points, vs "+str(pointman1)+" point")

            elif pointman2 == 1 and pointman1 != 1:
                score = sc.textinput("Pointage", str(pointman2) +" point, vs "+str(pointman1)+" points")

            elif pointman2 != 1 and pointman1 != 1:
                score = sc.textinput("Pointage", str(pointman2) +" points, vs "+str(pointman1)+" points")

        if balle.xcor() < -999:
            rand3 = random.uniform(-10,10)
            rand4 = random.uniform(-10,10)
            balle.setpos(0,0)
            time.sleep(0.5)
            movx = -2
            movy = 0

            pointman1 += 1

            if pointman2 == 1 and pointman1 == 1:
                score = sc.textinput("Pointage", str(pointman2) +" point, vs "+str(pointman1)+" point")

            elif pointman2 != 1 and pointman1 == 1:
                score = sc.textinput("Pointage", str(pointman2) +" points, vs "+str(pointman1)+" point")

            elif pointman2 == 1 and pointman1 != 1:
                score = sc.textinput("Pointage", str(pointman2) +" point, vs "+str(pointman1)+" points")

            elif pointman2 != 1 and pointman1 != 1:
                score = sc.textinput("Pointage", str(pointman2) +" points, vs "+str(pointman1)+" points")

        # Mannette out of bounds verification

        if mannette1.xcor() != 940:
            mannette1.setx(940)
        if mannette2.xcor() != -947:
            mannette2.setx(-947)

        # Courbure de la balle: Mannette1

        if mannette1_velocity != 0:
            if balle.xcor() > 920 and balle.xcor() < 935 and balle.ycor() < mannette1.ycor()+110 and balle.ycor() > mannette1.ycor()-110:
                balle.setx(920)
                movx = movx * -1
                rand3 = random.uniform(-10,10)
                # Pour que la balle va dans la direction du "velocity" de la mannette.
                
                if mannette1_velocity < 0:
                    movy = -1
                if mannette1_velocity > 0:
                    movy = 1

                while not (balle.xcor() < -927 and balle.xcor() > -935 and balle.ycor() < mannette2.ycor()+1100 and balle.ycor() > mannette2.ycor()-1100):
                    sc.update()

                    # Ordinateur #1

                    rand1 = random.randrange(-14,14)

                    mannette1_velocity = rand1/80

                    dist1 = (balle.xcor()-940)/rand3

                    mannette1.sety(balle.ycor()-dist1)

                    if mannette1.ycor() > 405:
                        mannette1.sety(404)

                    if mannette1.ycor() < -395:
                        mannette1.sety(-394)

                    # Ordinateur #2

                    rand2 = random.randrange(-14,14)

                    mannette2_velocity = rand2/80

                    dist2 = (balle.xcor()+940)/rand4

                    mannette2.sety(balle.ycor()+dist2)

                    if mannette2.ycor() > 405:
                        mannette2.sety(404)

                    if mannette2.ycor() < -395:
                        mannette2.sety(-394)

                    # Mouvement de la balle

                    movy = movy-mannette1_velocity/100

                    yvel = balle.ycor()+movy
                    xvel = balle.xcor()+movx
                    balle.sety(yvel)
                    balle.setx(xvel)

                    # Rebondissement de la balle: Plafond et Plancher

                    if balle.ycor() > 495:
                        balle.sety(495)
                        movy = movy*-1

                    if balle.ycor() < -490:
                        balle.sety(-490)
                        movy = movy*-1

                    # Pour que les mannettes restes dans leurs axe  

                    if mannette1.xcor() != 940:
                        mannette1.setx(940)
                    if mannette2.xcor() != -947:
                        mannette2.setx(-947)

                    # Mannette out of bounds check

                    if mannette1.ycor() > 405:
                        mannette1.sety(404)

                    if mannette1.ycor() < -395:
                        mannette1.sety(-394)

                    if mannette2.ycor() > 405:
                        mannette2.sety(404)

                    if mannette2.ycor() < -395:
                        mannette2.sety(-394)

                    # Rebondissement de la balle: Ouest et Est

                    if balle.xcor() > 999 or balle.xcor() < -999:
                        mannette1.sety(0)
                        break

        # Courbure de la balle: Mannette2

        if mannette2_velocity != 0:
            if balle.xcor() < -927 and balle.xcor() > -935 and balle.ycor() < mannette2.ycor()+1100 and balle.ycor() > mannette2.ycor()-1100:
                balle.setx(-927)
                movx = movx * -1
                rand4 = random.uniform(-10,10)

                # Pour que la balle va dans la direction du "velocity" de la mannette.
                
                if mannette2_velocity < 0:
                    movy = -1
                if mannette2_velocity > 0:
                    movy = 1

                while not (balle.xcor() > 920 and balle.xcor() < 935 and balle.ycor() < mannette1.ycor()+110 and balle.ycor() > mannette1.ycor()-110):
                    sc.update()

                    # Ordinateur #1

                    rand1 = random.randrange(-14,14)

                    mannette1_velocity = rand1/80

                    dist1 = (balle.xcor()-940)/rand3

                    mannette1.sety(balle.ycor()-dist1)

                    if mannette1.ycor() > 405:
                        mannette1.sety(404)

                    if mannette1.ycor() < -395:
                        mannette1.sety(-394)

                    # Ordinateur #2

                    rand2 = random.randrange(-14,14)

                    mannette2_velocity = rand2/80

                    dist2 = (balle.xcor()+940)/rand4

                    mannette2.sety(balle.ycor()+dist2)

                    if mannette2.ycor() > 405:
                        mannette2.sety(404)

                    if mannette2.ycor() < -395:
                        mannette2.sety(-394)

                    # Mouvement de la balle

                    movy = movy-mannette2_velocity/100

                    yvel = balle.ycor()+movy
                    xvel = balle.xcor()+movx
                    balle.sety(yvel)
                    balle.setx(xvel)

                    # Rebondissement de la balle: Plafond et Plancher

                    if balle.ycor() > 495:
                        balle.sety(495)
                        movy = movy*-1

                    if balle.ycor() < -490:
                        balle.sety(-490)
                        movy = movy*-1

                    # Pour que les mannettes restes dans leurs axe  

                    if mannette1.xcor() != 940:
                        mannette1.setx(940)
                    if mannette2.xcor() != -947:
                        mannette2.setx(-947)

                    # Mannette out of bounds check

                    if mannette1.ycor() > 405:
                        mannette1.sety(404)

                    if mannette1.ycor() < -395:
                        mannette1.sety(-394)

                    if mannette2.ycor() > 405:
                        mannette2.sety(404)

                    if mannette2.ycor() < -395:
                        mannette2.sety(-394)

                    # Rebondissement de la balle: Ouest et Est

                    if balle.xcor() > 999 or balle.xcor() < -999:
                        mannette1.sety(0)
                        break

# Le Menu

ans = t.textinput("Quel Jeu?", "Voulez vous jouer contre l'ordinateur, a deux joueurs ou regarder un match?")

while True:
    if "chien" in ans or "Chien" in ans:
        ans = t.textinput("Quel Jeu?", "'"+str(ans)+"'"+" n'est pas une reponse valide, essaye encore.")

    elif "deux" in ans or "2" in ans or "de" in ans or "a" in ans:
        t.textinput("Jeu", "Le joueur a gauche peut utiliser 'w' et 's' pour bouger sa mannette. Le joueur a droite peut utiliser les fleches 'Haut' et 'Bas' pour bouger sa mannette. Un des joueurs peut aussi utiliser la souris pour cliquer sur sa mannette et la bouger. Ceci est plus facile que le clavier.")
        t.textinput("Jeu", "Pour courber la balle, pendant que la balle frappe ta mannette, bouge la, et la balle aurait une courbe!")
        jeu2joueurs()

    elif "c" in ans or "l'" in ans or "or" in ans or "1" in ans:
        t.textinput("Jeu", "Tu peut utiliser les fleches 'Haut' et 'Bas' pour bouger ta mannette. Tu peut aussi utiliser la souris pour cliquer sur ta mannette et la bouger. Ceci est beaucoup plus facile que le clavier.")
        t.textinput("Jeu", "Pour courber la balle, pendant que la balle frappe ta mannette, bouge la, et la balle aurait une courbe!")
        
        jeu1joueur()

    elif "reg" in ans or " un " in ans or "ma" in ans or "0" in ans:
        jeu0joueurs()

    else:
        ans = t.textinput("Quel Jeu?", "'"+str(ans)+"'"+" n'est pas une reponse valide, essaye encore.")