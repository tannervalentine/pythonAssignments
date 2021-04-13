import turtle
import math
ken = turtle.Turtle()

def triangle(side):
    for i in range(3):
        ken.fd(side)
        ken.left(120)
def square(side):
    for i in range(4):
        ken.fd(side)
        ken.left(90)
def octagon(side):
    for i in range(8):
        ken.fd(side)
        ken.left(45)
def circle(radius):
    ken.penup()
    ken.right(90)
    ken.fd(radius)
    ken.left(90)
    ken.pendown()
    c = 2*math.pi*radius
    for i in range(360):
        ken.fd(c/360)
        ken.left(1)
    ken.penup()
    ken.left(90)
    ken.fd(radius)
    ken.right(90)
    ken.pendown()

#length = int(input("What's the side length?"))
#triangle(length)   

#length = int(input("What's the side length?"))
#square(length)    

#length = int(input("What's the side length?"))
#octagon(length)   

radius = int(input("What radius for the circle?"))
circle(radius)

