import turtle
chet = turtle.Turtle()


def drawShape(n):
    for i in range(n):
        chet.fd(720/n)
        chet.left(360/n)
number = int(input("How many sides do you want your shape to have?"))
drawShape(number)
print("There's your shape!")
