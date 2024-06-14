from Triangle import Triangle
from random import randint
import turtle

triangles = []
for i in range(100):

    x1 = randint(-100, 100)
    y1 = randint(-100, 100)
    x2 = randint(-100, 100)
    y2 = randint(-100, 100)
    t = Triangle(x1, y1, x2, y2)

    color = "#" + "".join([str(hex(randint(0, 15)))[2:] for _ in range(6)])
    t.set_color(color)

    x = randint(-300, 300)
    y = randint(-300, 300)
    t.set_position((x, y))

    triangles.append(t)

for triangle in triangles:
    triangle.draw()

turtle.update()

turtle.mainloop()