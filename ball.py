import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Simulator")
wn.tracer(0)

balls = []

for _ in range(100):
  balls.append(turtle.Turtle())

colors = ["red", "blue",  "yellow", "orange", "green", "white", "purple", "grey", "pink", "chocolate", "aquamarine",  "beige", "azure", "lime"]

shapes = ["circle", "square"]

for ball in balls:
   ball.shape(random.choice(shapes))
   ball.color(random.choice(colors))
   ball.penup()
   ball.speed(1)
   x = random.randint(-290, 290)
   y = random.randint(200, 400)
   ball.goto(x, y)
   ball.dy = 0
   ball.dx = random.randint(-3, 3)
   ball.da = random.randint(-5, 5)

gravity = 0.1

while True:
   wn.update()
   for ball in balls:
     ball.rt(ball.da)
     ball.dy -= gravity
     ball.sety(ball.ycor() + ball.dy)
     ball.setx(ball.xcor() + ball.dx)
     if ball.xcor() > 530:
       ball.dx *= -1
       ball.da *= -1
     if ball.xcor() < -530:
       ball.setx(-530)
       ball.dx *= -1
       ball.da *= -1
     if ball.ycor() < -1060:
       ball.sety(-1060)
       ball.dy *= -1
       ball.da *= -1
   
   for i in range(0, len(balls)):
     for j in range(i+1, len(balls)):
       if balls[i].distance(balls[j]) < 20:
         balls[i].dx, balls[j].dx = balls[j].dx, balls[i].dx
         balls[i].dy, balls[j].dy = balls[j].dy, balls[i].dy

wn.mainloop()