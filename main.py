from turtle import *
from random import randint

speed(10)
penup()
goto(-140,140)

for step in range(11):
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)

jay = Turtle()
jay.color('purple')
jay.shape('turtle')

jay.penup()
jay.goto(-160, 100)
jay.pendown()

kate = Turtle()
kate.color('tomato')
kate.shape('turtle')

kate.penup()
kate.goto(-160, 70)
kate.pendown()

sam = Turtle()
sam.color('magenta')
sam.shape('turtle')

sam.penup()
sam.goto(-160, 40)
sam.pendown()

gigi = Turtle()
gigi.color('brown')
gigi.shape('turtle')

gigi.penup()
gigi.goto(-160, 10)
gigi.pendown()


for turn in range(100):
  jay.forward(randint(1,5))
  jay.right(36)
  kate.forward(randint(1,5))
  sam.forward(randint(1,5))
  gigi.forward(randint(1,5))