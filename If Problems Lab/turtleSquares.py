color = input("What color would you like your squares to be?").lower()
number = int(input("How many squares would you like? (Max of 3.)"))

import turtle

craig = turtle.Turtle()
craig.shape("turtle")
craig.color(str(color))
craig.penup()
craig.goto(-200,0)
craig.pendown()

for i in range(number):
    for j in range(4):
        craig.fd(80)
        craig.left(90)
    craig.penup()
    craig.fd(100)
    craig.pendown()
