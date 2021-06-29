import turtle
import winsound

win = turtle.Screen()
win.title("Ping Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# First Paddle
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# Second paddle
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# The ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2:0", align="center", font=("Courier", 24, "normal"))

# The score
score_1 = 0
score_2 = 0


# Game functions
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)


# Keyboard links
win.listen()
win.onkeypress(paddle_1_up, "w")
win.onkeypress(paddle_1_down, "s")
win.onkeypress(paddle_2_up, "Up")
win.onkeypress(paddle_2_down, "Down")

# Game loop
while True:
    win.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border for ball moving
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("name.mp3", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("name.mp3", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2:{}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2:{}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))

    # Paddle collisions
    if 340 < ball.xcor() < 350 and (paddle_2.ycor() + 40 > ball.ycor() > paddle_2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if -340 > ball.xcor() > -350 and (paddle_1.ycor() + 40 > ball.ycor() > paddle_1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
