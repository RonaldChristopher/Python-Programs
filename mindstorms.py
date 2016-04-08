import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_creative():
    window = turtle.Screen()
    window.bgcolor("blue")
    #draw square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(3)
    for i in range (1,36):
        draw_square(brad)
        brad.right(10)

    #draw circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("white")
    angie.circle(100)

    window.exitonclick()
   

draw_creative()
