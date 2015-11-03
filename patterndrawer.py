import turtle

phoebe = turtle.Turtle()
phoebe.color("red")
phoebe.speed(0)

lisa = turtle.Turtle()
lisa.color("white")
lisa.speed(0)

mikey = turtle.Turtle()
mikey.color("blue")
mikey.speed(0)


def draw_square(a_turtle, forward, pivotright):
    for i in range(0,4):
        a_turtle.forward(forward)
        a_turtle.right(pivotright)
      
def draw_triangle(a_turtle, forward, pivotright):
    for i in range(0,3):
        a_turtle.forward(forward)
        a_turtle.right(pivotright)
    
def draw_repeat(a_turtle, turtle_2, turtle_3):
    zone = turtle.Screen()
    zone.bgcolor("orange")

    for i in range(0,80):
        draw_square(a_turtle, 50, 90)
        draw_square(turtle_2, 75, 90)
        draw_square(turtle_3, 100, 90)
        draw_square(turtle_2, 125, 90)
        draw_triangle(a_turtle, 150, 120)
        draw_triangle(turtle_3, 175, 120)
        draw_triangle(turtle_2, 200, 120)
        draw_square(turtle_3, 250, 90)
        draw_square(turtle_2, 300, 90)
        a_turtle.right(5)
        turtle_2.left(5)
        turtle_3.right(5)

    
    zone.exitonclick()
    
draw_repeat(mikey, phoebe, lisa)


