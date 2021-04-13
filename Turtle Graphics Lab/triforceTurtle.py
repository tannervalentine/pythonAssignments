import turtle
chet = turtle.Turtle()

def drawTriangle(size):
    for i in range(3):
        chet.fd(size)
        chet.left(120)

drawTriangle(150)
chet.penup()
chet.fd(75)
chet.left(60)
chet.pendown()
drawTriangle(75)
chet.ht()
