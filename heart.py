import math
from turtle import *

def hearta(k):
    return 15*math.sin(k)**3

def heartb(k):
    return 12*math.cos(k) - 5*math.cos(2*k) - 2*math.cos(3*k) - math.cos(4*k)

speed(0)
bgcolor("black")
penup()
goto(0,0)
pendown()
color("red")

# Precompute values
coords = [(hearta(i)*20, heartb(i)*20) for i in range(6000)]

for x, y in coords:
    goto(x, y)
    goto(0, 0)

done()
