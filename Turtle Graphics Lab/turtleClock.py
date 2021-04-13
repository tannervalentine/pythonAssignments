import turtle
chet = turtle.Turtle()

chet.shape("turtle")

for i in range(12):
    chet.penup()
    chet.fd(65)
    chet.pendown()
    chet.fd(20)
    chet.penup()
    chet.fd(15)
    chet.stamp()
    chet.goto(0,0)
    chet.right(30)
chet.goto(0,-130)
chet.pendown()
chet.pensize(3)
chet.circle(130)
chet.ht()
