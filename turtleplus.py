#this program will be an expansion of the turtle module
#it will add new functions to the turtle module


#this is the code for the module
import turtle as t


#we will now create a function that will draw a regular polygon with the specified number of sides and the specified length
def regular_polygon(turtle, sides, length):
    angle = 360 / sides
    for i in range(sides):
        turtle.fd(length)
        turtle.lt(angle)


#this function will draw a square with the specified side length
def square(turtle, length):
    regular_polygon(turtle, 4, length)


#this function will draw a triangle with the specified side length
def triangle(turtle, length):
    regular_polygon(turtle, 3, length)


#this function will draw a pentagon with the specified side length
def pentagon(turtle, length):
    regular_polygon(turtle, 5, length)

#this function will draw a hexagon with the specified side length
def hexagon(turtle, length):
    regular_polygon(turtle, 6, length)


#this function will draw a rectangle with the specified width and height
def rectangle(turtle, width, height):
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)


#this function will draw a circle with the specified radius
def circle(turtle, radius):
    circumference = 2 * 3.14 * radius
    length = circumference / 360
    regular_polygon(turtle, 360, length)


#this function will create a set of turtles
def create_turtles(number):
    turtles = []
    for i in range(number):
        turtles.append(t.Turtle())
    return turtles