import turtle
chet = turtle.Turtle()
chet.pensize(2)
def circleRight(color):
    chet.pencolor(str(color))
    chet.circle(50)
    chet.penup()
    chet.fd(60)
    chet.right(90)
    chet.fd(50)
    chet.left(90)
    chet.pendown()

def circleLeft(color):
    chet.pencolor(str(color))
    chet.circle(50)
    chet.penup()
    chet.fd(60)
    chet.left(90)
    chet.fd(50)
    chet.right(90)
    chet.pendown()

circleRight("blue")
circleLeft("yellow")
circleRight("black")
circleLeft("green")
circleRight("red")
chet.ht()
