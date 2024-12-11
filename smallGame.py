import turtle
import time
import random 

score_a = 0
score_b = 0
# sound_path = "ping_pong_hit.wav" 

# Display screen
win = turtle.Screen()
win.setup(width=800, height=600)
win.bgcolor("black")
win.title("Pong Game")
win.tracer(0)

# Left paddle (AI)
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("green")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-380, 0)

# Right paddle (Player)
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("green")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(380, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3 

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jarvis: 0  You: 0", align="center", font=("Ariel", 24, "normal"))

# Moving paddles
def right_paddle_up():
    y = right_paddle.ycor()
    if y < 250: 
        right_paddle.sety(y + 30)

def right_paddle_down():
    y = right_paddle.ycor()
    if y > -240: 
        right_paddle.sety(y - 30)

win.listen()
win.onkeypress(right_paddle_up, 'Up')
win.onkeypress(right_paddle_down, 'Down')

def gameStop(message):
    pen.clear()
    ball.hideturtle()
    pen.goto(0, 0) 
    pen.write(message, align="center", font=("Ariel", 36, "bold"))
    win.update()  
    time.sleep(3)
    win.bye()

# Main game loop
while True:
    win.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = -ball.dx
        score_a += 1
        pen.clear()
        pen.goto(0, 260)
        pen.write(f"Jarvis: {score_a}  You: {score_b}", align="center", font=("Ariel", 24, "normal"))
        
        if score_a == 5:
            gameStop("Jarvis Won The Match")
            break  
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = -ball.dx
        score_b += 1
        pen.clear()
        pen.goto(0, 260)
        pen.write(f"Jarvis: {score_a}  You: {score_b}", align="center", font=("Ariel", 24, "normal"))
        
        if score_b == 5:
            gameStop("You Won The Match")
            break  # Exit the loop after stopping the game
    
    # Paddle (AI) movement
    if random.random() < 0.1:  # AI reacts only 10% of the time
        if left_paddle.ycor() < ball.ycor() and abs(left_paddle.ycor() - ball.ycor()) > 10:
            left_paddle.sety(left_paddle.ycor() + 5)  
        elif left_paddle.ycor() > ball.ycor() and abs(left_paddle.ycor() - ball.ycor()) > 10:
            left_paddle.sety(left_paddle.ycor() - 5)  
    
    # Paddle and ball collisions
    if (ball.xcor() > 370 and ball.xcor() < 380) and (right_paddle.ycor() - 50 < ball.ycor() < right_paddle.ycor() + 50):
        ball.setx(370)
        ball.dx *= -1
    
    if (ball.xcor() < -370 and ball.xcor() > -380) and (left_paddle.ycor() - 50 < ball.ycor() < left_paddle.ycor() + 50):
        ball.setx(-370)
        ball.dx *= -1

win.bye()
