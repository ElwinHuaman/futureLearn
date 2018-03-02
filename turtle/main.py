from random import randint
from turtle import Turtle

laura = Turtle()
laura.color('blue')
laura.shape('turtle')

elwin = Turtle()
elwin.color('pink')
elwin.shape('turtle')

irene = Turtle()
irene.color('yellow')
irene.shape('turtle')

elwin.penup()
elwin.goto(-150,100)
elwin.pendown()
laura.penup()
laura.goto(-150,90)
laura.pendown()
irene.penup()
irene.goto(-150,60)
irene.pendown()

for movement in range(100):
  laura.forward(randint(1,20))
  elwin.forward(randint(1,20))
  irene.forward(rnadint(1,20))