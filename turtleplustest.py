#this will test the turtleplus module

import turtleplus as tp


#create a turtle
t = tp.t.Turtle()

tp.t.title("TurtlePlus Python Graphics")

print(t)

#draw a square
tp.square(t, 100)

#draw a triangle
tp.triangle(t, 150)

#create 2 turtles with the create_turtles command that will both draw different shapes
turtles = tp.create_turtles(2)

#turtle 1 will be blue and draw a hexagon
turtles[0].color("blue")
tp.hexagon(turtles[0], 100)

#turtle 2 will be green draw a pentagon
turtles[1].color("green")
tp.pentagon(turtles[1], 100)

#draw a nonagon
tp.regular_polygon(t, 9, 100)

#now we use a regular turtle command
tp.t.rt(34)
tp.t.fd(100)

#that is the end of the test
tp.t.mainloop()