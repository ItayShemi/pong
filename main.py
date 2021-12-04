import turtle
import sys
import time
from pygame import mixer

wn = turtle.Screen()
wn.title('Pong by Itay Shemi')
wn.bgcolor('black')

pen = turtle.Turtle()
pen.speed(0)

# Menu Options
pen.penup()
pen.color('white')
pen.goto(-90, 0)
pen.write("Start a new game", font=("Arial", 17, "normal"))

pen.penup()
pen.color('white')
pen.goto(-55, 180)
pen.write("Menu", font=("Arial", 30, "normal"))

pen.penup()
pen.color('white')
pen.goto(-35, -50)
pen.write("Quit", font=("Arial", 17, "normal"))

pen.penup()
pen.color('white')
pen.goto(-600, -600)
pen.write(".", font=("Arial", 1, "normal"))

dart = turtle.Turtle()
dart.speed(0)
dart.color('white')
dart.penup()
dart.hideturtle()
dart.goto(-120, 60)
dart.dy = 0.4
dart.dx = 0.4

# Making options clickable

def btnclick(x, y):
    if x > -91 and x < 80 and y > 6 and y < 23:
        turtle.clearscreen()
        win = turtle.Screen()
        win.title("pong by itay shemi")
        win.bgcolor("black")
        win.setup(width=800, height=600)
        win.tracer(0)

        pen.penup()
        pen.color('white')
        pen.goto(-75, 0)
        pen.write("single player", font=("Arial", 21, "normal"))

        pen.penup()
        pen.color('white')
        pen.goto(-40, -60)
        pen.write("1 vs 1", font=("Arial", 21, "normal"))

        pen.penup()
        pen.color('white')
        pen.goto(-600, -600)
        pen.write(".", font=("Arial", 1, "normal"))

        pen.penup()
        pen.color('white')
        pen.goto(-88, 60)
        pen.write("Return to menu", font=("Arial", 21, "normal"))

        dart.write(">", font=("Courier", 21, "normal"))

        def arrow_up():
            y = dart.ycor()
            y += 60
            dart.sety(y)
            dart.clear()
            dart.write(">", font=("Courier", 21, "normal"))
            if y > 60:
                dart.goto(-120, -60)
                dart.sety(-60)
                dart.clear()
                dart.write(">", font=("Courier", 21, "normal"))

        def arrow_down():
            y = dart.ycor()
            y -= 60
            dart.sety(y)
            dart.clear()
            dart.write(">", font=("Courier", 21, "normal"))
            if y < -60:
                dart.goto(-120, 60)
                dart.sety(60)
                dart.clear()
                dart.write(">", font=("Courier", 21, "normal"))

        def options():
            y = dart.ycor()
            if y == 60:
                win.clear()
                exec(open('main.py').read())
            b = dart.ycor()
            if b == 0:

                turtle.clearscreen()
                wn = turtle.Screen()
                wn.title("pong by itay shemi")
                wn.bgcolor("black")
                wn.setup(width=800, height=600)
                wn.tracer(0)

                # score

                score_a = 0
                score_b = 0

                # Paddle A
                paddle_a = turtle.Turtle()
                paddle_a.speed(0)
                paddle_a.shape("square")
                paddle_a.color("white")
                paddle_a.shapesize(stretch_wid=5, stretch_len=1)
                paddle_a.penup()
                paddle_a.goto(-350, 0)

                # Paddle B
                paddle_b = turtle.Turtle()
                paddle_b.speed(0)
                paddle_b.shape("square")
                paddle_b.color("white")
                paddle_b.shapesize(stretch_wid=5, stretch_len=1)
                paddle_b.penup()
                paddle_b.goto(350, 0)

                # Ball
                Ball = turtle.Turtle()
                Ball.speed(0)
                Ball.shape("square")
                Ball.color("white")
                Ball.penup()
                Ball.goto(0, 0)
                Ball.dx = 0.4
                Ball.dy = 0.4

                # Pen
                pen = turtle.Turtle()
                pen.speed(0)
                pen.color("white")
                pen.penup()
                pen.hideturtle()
                pen.goto(0, 260)
                pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "normal"))

                # Winner

                winner = turtle.Turtle()
                winner.speed(0)
                winner.color('white')
                winner.penup()
                winner.hideturtle()
                winner.goto(-100, 150)

                # Return to menu

                back = turtle.Turtle()
                back.speed(0)
                back.color('white')
                back.penup()
                back.hideturtle()
                back.goto(-100, -5)

                # start a new game

                start = turtle.Turtle()
                start.speed(0)
                start.color('white')
                start.penup()
                start.hideturtle()
                start.goto(-115, 35)

                # Quit

                out = turtle.Turtle()
                out.speed(0)
                out.color('white')
                out.penup()
                out.hideturtle()
                out.goto(-35, -45)

                # Arrow

                arrow = turtle.Turtle()
                arrow.speed(0)
                arrow.color('white')
                arrow.penup()
                arrow.hideturtle()
                arrow.goto(-150, 35)
                arrow.dy = 0.4
                arrow.dx = 0.4

                # Function
                def paddle_a_up():
                    y = paddle_a.ycor()
                    y += 20
                    paddle_a.sety(y)
                    if y > 250:
                        paddle_a.sety(-250)
                        paddle_a.clear()

                def paddle_a_down():
                    y = paddle_a.ycor()
                    y -= 20
                    paddle_a.sety(y)
                    if y < -250:
                        paddle_a.sety(250)
                        paddle_a.clear()

                def paddle_b_up():
                    y = paddle_b.ycor()
                    y += 20
                    paddle_b.sety(y)
                    if y > 250:
                        paddle_b.sety(250)
                        paddle_b.clear()

                def paddle_b_down():
                    y = paddle_b.ycor()
                    y -= 20
                    paddle_b.sety(y)
                    if y < -250:
                        paddle_b.sety(-250)
                        paddle_b.clear()

                # Keyborad binding
                wn.listen()
                wn.onkeypress(paddle_a_up, "w")
                wn.onkeypress(paddle_a_down, "s")

                while True:
                    # Move the ball
                    Ball.setx(Ball.xcor() + Ball.dx)
                    Ball.sety(Ball.ycor() + Ball.dy)

                    wn.update()

                    # Border checking
                    if Ball.ycor() > 290:
                        Ball.sety(290)
                        Ball.dy *= -1
                        mixer.init()
                        mixer.music.load('sound.mp3')
                        mixer.music.play()

                    if Ball.ycor() < -290:
                        Ball.sety(-290)
                        Ball.dy *= -1
                        mixer.init()
                        mixer.music.load('sound.mp3')
                        mixer.music.play()

                    if Ball.xcor() < -390:
                        Ball.goto(0, 0)
                        Ball.dx *= -1
                        score_a += 1
                        pen.clear()
                        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center",
                                  font=("Courier", 24, "normal"))
                        mixer.init()
                        mixer.music.load('sound.wav')
                        mixer.music.play()

                    if Ball.xcor() > 390:
                        Ball.goto(0, 0)
                        Ball.dx *= -1
                        score_b += 1
                        pen.clear()
                        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center",
                                  font=("Courier", 24, "normal"))
                        mixer.init()
                        mixer.music.load('sound.wav')
                        mixer.music.play()

                    # AI lose

                    if score_b == 10:
                        paused = False
                        t = turtle.Turtle()

                        def unpause():
                            global paused
                            paused = False

                        def turtle_setup():
                            global wn
                            wn.onkeypress(unpause)
                            wn.listen()

                        def draw_task_finished():
                            global paused, current_task, drawing_task
                            current_task = 0
                            current_task += 1
                            paused = True
                            if current_task < len(drawing_tasks):
                                draw_task_after_keypress()

                        def draw_task_after_keypress():
                            global paused, current_task
                            if paused:
                                turtle.ontimer(draw_task_after_keypress, 100)
                            else:
                                drawing_tasks[current_task]()

                        def draw_thing_one():
                            global t
                            winner.write("You Won", align='center',
                                         font=("Courier", 30, "normal"))
                            back.write("Return to menu",
                                       font=("Courier", 18, "normal"))

                            start.write("Start a new game",
                                        font=("Courier", 18, "normal"))
                            out.write("Quit", font=("Courier", 18, "normal"))
                            arrow.write(">", font=("Courier", 18, "normal"))

                            def arrow_up():
                                y = arrow.ycor()
                                y += 40
                                arrow.sety(y)
                                arrow.clear()
                                arrow.write(">", font=("Courier", 18, "normal"))
                                if y > 35:
                                    arrow.goto(-150, -45)
                                    arrow.sety(35)
                                    arrow.clear()
                                    arrow.write(">", font=("Courier", 18, "normal"))

                            def arrow_down():
                                y = arrow.ycor()
                                y -= 40
                                arrow.sety(y)
                                arrow.clear()
                                arrow.write(">", font=("Courier", 18, "normal"))
                                if y < -45:
                                    arrow.goto(-150, 35)
                                    arrow.sety(-45)
                                    arrow.clear()
                                    arrow.write(">", font=("Courier", 18, "normal"))

                            def options():
                                y = arrow.ycor()
                                if y == 35:
                                    wn.clear()
                                    btnclick(x=12, y=12)
                                b = arrow.ycor()
                                if b == -5:
                                    wn.clear()
                                    exec(open("main.py").read())
                                q = arrow.ycor()
                                if q == -45:
                                    time.sleep(0)
                                    sys.exit()

                            # Keyborad binding
                            wn.listen()
                            wn.onkeypress(arrow_up, "Up")
                            wn.onkeypress(arrow_down, "Down")
                            wn.onkeypress(options, 'Return')

                            draw_task_finished()

                        drawing_tasks = [draw_thing_one, ]

                        turtle_setup()
                        drawing_tasks[0]()

                        wn.mainloop()

                    # AI win

                    if score_a == 10:
                        paused = False
                        t = turtle.Turtle()

                        def unpause():
                            global paused
                            paused = False

                        def turtle_setup():
                            global wn
                            wn.onkeypress(unpause)
                            wn.listen()

                        def draw_task_finished():
                            global paused, current_task, drawing_task
                            current_task = 0
                            current_task += 1
                            paused = True
                            if current_task < len(drawing_tasks):
                                draw_task_after_keypress()

                        def draw_task_after_keypress():
                            global paused, current_task
                            if paused:
                                turtle.ontimer(draw_task_after_keypress, 100)
                            else:
                                drawing_tasks[current_task]()

                        def draw_thing_one():
                            global t
                            winner.write("You lost",
                                         font=("Courier", 30, "normal"))
                            back.write("Return to menu",
                                       font=("Courier", 18, "normal"))

                            start.write("Start a new game",
                                        font=("Courier", 18, "normal"))
                            out.write("Quit", font=("Courier", 18, "normal"))
                            arrow.write(">", font=("Courier", 18, "normal"))

                            # Move the arrow

                            def arrow_up():
                                y = arrow.ycor()
                                y += 40
                                arrow.sety(y)
                                arrow.clear()
                                arrow.write(">", font=("Courier", 18, "normal"))
                                if y > 35:
                                    arrow.goto(-150, -45)
                                    arrow.sety(35)
                                    arrow.clear()
                                    arrow.write(">", font=("Courier", 18, "normal"))

                            def arrow_down():
                                y = arrow.ycor()
                                y -= 40
                                arrow.sety(y)
                                arrow.clear()
                                arrow.write(">", font=("Courier", 18, "normal"))
                                if y < -45:
                                    arrow.goto(-150, 35)
                                    arrow.sety(-45)
                                    arrow.clear()
                                    arrow.write(">", font=("Courier", 18, "normal"))

                            # Options

                            def options():
                                y = arrow.ycor()
                                if y == 35:
                                    wn.clear()
                                b = arrow.ycor()
                                if b == -5:
                                    wn.clear()
                                    exec(open("main.py").read())
                                q = arrow.ycor()
                                if q == -45:
                                    time.sleep(0)
                                    sys.exit()

                            """ Keyboard binding """
                            wn.listen()
                            wn.onkeypress(arrow_up, "Up")
                            wn.onkeypress(arrow_down, "Down")
                            wn.onkeypress(options, 'Return')

                            draw_task_finished()

                        drawing_tasks = [draw_thing_one, ]

                        turtle_setup()
                        drawing_tasks[0]()

                        wn.mainloop()
                    # Paddle and ball collisions
                    if (Ball.xcor() > 340 and Ball.xcor() < 350) and (
                            Ball.ycor() < paddle_b.ycor() + 100 and Ball.ycor() > paddle_b.ycor() - 100):
                        Ball.setx(340)
                        Ball.dx *= -1
                        mixer.init()
                        mixer.music.load('sound.mp3')
                        mixer.music.play()

                    if (Ball.xcor() < -340 and Ball.xcor() > -350) and (
                            Ball.ycor() < paddle_a.ycor() + 100 and Ball.ycor() > paddle_a.ycor() - 100):
                        Ball.setx(-340)
                        Ball.dx *= -1
                        mixer.init()
                        mixer.music.load('sound.mp3')
                        mixer.music.play()

                    # AI
                    if paddle_b.ycor() < Ball.ycor() and abs(paddle_b.ycor() - Ball.ycor() - 10):
                        paddle_b_up()

                    if paddle_b.ycor() > Ball.ycor() and abs(paddle_b.ycor() - Ball.ycor() - 10):
                        paddle_b_down()

            q = dart.ycor()
            if q == -60:
                turtle.clearscreen()
                wn = turtle.Screen()
                wn.title("pong by itay shemi")
                wn.bgcolor("black")
                wn.setup(width=800, height=600)
                wn.tracer(0)

                # score

                score_a = 0
                score_b = 0

                # Paddle A
                paddle_a = turtle.Turtle()
                paddle_a.speed(0)
                paddle_a.shape("square")
                paddle_a.color("white")
                paddle_a.shapesize(stretch_wid=5, stretch_len=1)
                paddle_a.penup()
                paddle_a.goto(-350, 0)

                # Paddle B
                paddle_b = turtle.Turtle()
                paddle_b.speed(0)
                paddle_b.shape("square")
                paddle_b.color("white")
                paddle_b.shapesize(stretch_wid=5, stretch_len=1)
                paddle_b.penup()
                paddle_b.goto(350, 0)

                # Ball
                Ball = turtle.Turtle()
                Ball.speed(0)
                Ball.shape("square")
                Ball.color("white")
                Ball.penup()
                Ball.goto(0, 0)
                Ball.dx = 0.4
                Ball.dy = 0.4

                # Pen
                pen = turtle.Turtle()
                pen.speed(0)
                pen.color("white")
                pen.penup()
                pen.hideturtle()
                pen.goto(0, 260)
                pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "normal"))

                # Winner

                winner = turtle.Turtle()
                winner.speed(0)
                winner.color('white')
                winner.penup()
                winner.hideturtle()
                winner.goto(-150, 150)

                # Return to menu

                back = turtle.Turtle()
                back.speed(0)
                back.color('white')
                back.penup()
                back.hideturtle()
                back.goto(-100, -5)

                # start a new game

                start = turtle.Turtle()
                start.speed(0)
                start.color('white')
                start.penup()
                start.hideturtle()
                start.goto(-115, 35)

                # Quit

                out = turtle.Turtle()
                out.speed(0)
                out.color('white')
                out.penup()
                out.hideturtle()
                out.goto(-35, -45)

                # Arrow

                arrow = turtle.Turtle()
                arrow.speed(0)
                arrow.color('white')
                arrow.penup()
                arrow.hideturtle()
                arrow.goto(-150, 35)
                arrow.dy = 0.4
                arrow.dx = 0.4

                # Function
                def paddle_a_up():
                    y = paddle_a.ycor()
                    y += 20
                    paddle_a.sety(y)
                    if y > 250:
                        paddle_a.sety(-250)
                        paddle_a.clear()

                def paddle_a_down():
                    y = paddle_a.ycor()
                    y -= 20
                    paddle_a.sety(y)
                    if y < -250:
                        paddle_a.sety(250)
                        paddle_a.clear()

                def paddle_b_up():
                    y = paddle_b.ycor()
                    y += 20
                    paddle_b.sety(y)
                    if y > 250:
                        paddle_b.sety(-250)
                        paddle_b.clear()

                def paddle_b_down():
                    y = paddle_b.ycor()
                    y -= 20
                    paddle_b.sety(y)
                    if y < -250:
                        paddle_b.sety(250)
                        paddle_b.clear()

                # Keyborad binding
                wn.listen()
                wn.onkeypress(paddle_a_up, "w")
                wn.onkeypress(paddle_a_down, "s")
                wn.onkeypress(paddle_b_up, "Up")
                wn.onkeypress(paddle_b_down, "Down")

                while True:
                    # Move the ball
                    Ball.setx(Ball.xcor() + Ball.dx)
                    Ball.sety(Ball.ycor() + Ball.dy)

                    wn.update()

                    # Border checking
                    if Ball.ycor() > 290:
                        Ball.sety(290)
                        Ball.dy *= -1
                        mixer.init()
                        mixer.music.load('sound.mp3')
                        mixer.music.play()

                    if Ball.ycor() < -290:
                        Ball.sety(-290)
                        Ball.dy *= -1
                        mixer.init()
                        mixer.music.load('sound.mp3')
                        mixer.music.play()

                    if Ball.xcor() < -390:
                        Ball.goto(0, 0)
                        Ball.dx *= -1
                        score_a += 1
                        pen.clear()
                        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center",
                                  font=("Courier", 24, "normal"))
                        mixer.init()
                        mixer.music.load('sound.wav')
                        mixer.music.play()

                    if Ball.xcor() > 390:
                        Ball.goto(0, 0)
                        Ball.dx *= -1
                        score_b += 1
                        pen.clear()
                        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center",
                                  font=("Courier", 24, "normal"))
                        mixer.init()
                        mixer.music.load('sound.wav')
                        mixer.music.play()

                    # Player A win

                    if score_b == 10:
                        paused = False
                        t = turtle.Turtle()

                        def unpause():
                            global paused
                            paused = False

                        def turtle_setup():
                            global wn
                            wn.onkeypress(unpause)
                            wn.listen()

                        def draw_task_finished():
                            global paused, current_task, drawing_task
                            current_task = 0
                            current_task += 1
                            paused = True
                            if current_task < len(drawing_tasks):
                                draw_task_after_keypress()

                        def draw_task_after_keypress():
                            global paused, current_task
                            if paused:
                                turtle.ontimer(draw_task_after_keypress, 100)
                            else:
                                drawing_tasks[current_task]()

                        def draw_thing_one():
                            global t
                            winner.write("Player A Won",
                                         font=("Courier", 30, "normal"))

                            back.write("Return to menu",
                                       font=("Courier", 18, "normal"))

                            start.write("Start a new game",
                                        font=("Courier", 18, "normal"))
                            out.write("Quit", font=("Courier", 18, "normal"))
                            arrow.write(">", font=("Courier", 18, "normal"))

                            # Move the arrow

                            def arrow_up():
                                y = arrow.ycor()
                                y += 40
                                arrow.sety(y)
                                arrow.clear()
                                arrow.write(">", font=("Courier", 18, "normal"))
                                if y > 35:
                                    arrow.goto(-150, -45)
                                    arrow.sety(35)
                                    arrow.clear()
                                    arrow.write(">", font=("Courier", 18, "normal"))

                            def arrow_down():
                                y = arrow.ycor()
                                y -= 40
                                arrow.sety(y)
                                arrow.clear()
                                arrow.write(">", font=("Courier", 18, "normal"))
                                if y < -45:
                                    arrow.goto(-150, 35)
                                    arrow.sety(-45)
                                    arrow.clear()
                                    arrow.write(">", font=("Courier", 18, "normal"))

                            # options

                            def options():
                                y = arrow.ycor()
                                if y == 35:
                                    wn.clear()
                                    btnclick(x=12, y=12)
                                b = arrow.ycor()
                                if b == -5:
                                    wn.clear()
                                    exec(open("main.py").read())
                                q = arrow.ycor()
                                if q == -45:
                                    time.sleep(0)
                                    sys.exit()

                            # Keyborad binding
                            wn.listen()
                            wn.onkeypress(arrow_up, "Up")
                            wn.onkeypress(arrow_down, "Down")
                            wn.onkeypress(options, 'Return')

                            draw_task_finished()

                        drawing_tasks = [draw_thing_one, ]

                        turtle_setup()
                        drawing_tasks[0]()

                        wn.mainloop()

                    # Player B won

                    if score_a == 10:
                        paused = False
                        t = turtle.Turtle()

                        def unpause():
                            global paused
                            paused = False

                        def turtle_setup():
                            global wn
                            wn.onkeypress(unpause)
                            wn.listen()

                        def draw_task_finished():
                            global paused, current_task, drawing_task
                            current_task = 0
                            current_task += 1
                            paused = True
                            if current_task < len(drawing_tasks):
                                draw_task_after_keypress()

                        def draw_task_after_keypress():
                            global paused, current_task
                            if paused:
                                turtle.ontimer(draw_task_after_keypress, 100)
                            else:
                                drawing_tasks[current_task]()

                        def draw_thing_one():
                            global t
                            winner.write("Player B Won",
                                         font=("Courier", 30, "normal"))
                            back.write("Return to menu",
                                       font=("Courier", 18, "normal"))

                            start.write("Start a new game",
                                        font=("Courier", 18, "normal"))
                            out.write("Quit", font=("Courier", 18, "normal"))
                            arrow.write(">", font=("Courier", 18, "normal"))

                            # Move the arrow

                            def arrow_up():
                                y = arrow.ycor()
                                y += 40
                                arrow.sety(y)
                                arrow.clear()
                                arrow.write(">", font=("Courier", 18, "normal"))
                                if y > 35:
                                    arrow.goto(-150, -45)
                                    arrow.sety(35)
                                    arrow.clear()
                                    arrow.write(">", font=("Courier", 18, "normal"))

                            def arrow_down():
                                y = arrow.ycor()
                                y -= 40
                                arrow.sety(y)
                                arrow.clear()
                                arrow.write(">", font=("Courier", 18, "normal"))
                                if y < -45:
                                    arrow.goto(-150, 35)
                                    arrow.sety(-45)
                                    arrow.clear()
                                    arrow.write(">", font=("Courier", 18, "normal"))

                            # options

                            def options():
                                y = arrow.ycor()
                                if y == 35:
                                    wn.clear()
                                    btnclick(x=12, y=12)
                                b = arrow.ycor()
                                if b == -5:
                                    wn.clear()
                                    exec(open("main.py").read())
                                q = arrow.ycor()
                                if q == -45:
                                    time.sleep(0)
                                    sys.exit()

                            # Keyborad binding
                            wn.listen()
                            wn.onkeypress(arrow_up, "Up")
                            wn.onkeypress(arrow_down, "Down")
                            wn.onkeypress(options, 'Return')

                            draw_task_finished()

                        drawing_tasks = [draw_thing_one, ]

                        turtle_setup()
                        drawing_tasks[0]()

                        wn.mainloop()
                    # Paddle and ball collisions
                    if (Ball.xcor() > 340 and Ball.xcor() < 350) and (
                            Ball.ycor() < paddle_b.ycor() + 100 and Ball.ycor() > paddle_b.ycor() - 100):
                        Ball.setx(340)
                        Ball.dx *= -1
                        mixer.init()
                        mixer.music.load('sound.mp3')
                        mixer.music.play()

                    if (Ball.xcor() < -340 and Ball.xcor() > -350) and (
                            Ball.ycor() < paddle_a.ycor() + 100 and Ball.ycor() > paddle_a.ycor() - 100):
                        Ball.setx(-340)
                        Ball.dx *= -1
                        mixer.init()
                        mixer.music.load('sound.mp3')
                        mixer.music.play()

        # Keyborad binding
        win.listen()
        win.onkeypress(arrow_up, "Up")
        win.onkeypress(arrow_down, "Down")
        win.onkeypress(options, "Return")

    elif x > -35 and x < 2 and y > -41 and y < -28:
        time.sleep(0)
        sys.exit()

turtle.onscreenclick(btnclick, 1)
turtle.listen()
turtle.done()