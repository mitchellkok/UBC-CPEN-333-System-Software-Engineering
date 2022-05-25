# student name: Mitchell Kok
# student number: 44572246
import turtle

# initialize variables
radius = 45
gap = 8
colors = ["#0081C8", "#FCB131", "#000000", "#00A651", "#EE334E"]

turtle.pensize(8) 
turtle.penup()

for i in range(5):
    turtle.color(colors[i]) # set color
    turtle.goto(-3*radius-gap + (i * (radius+gap)), -radius * (i % 2)) # go to start point
    turtle.pendown()
    turtle.circle(radius)   # draw circle
    turtle.penup()
    
turtle.hideturtle()
turtle.done()