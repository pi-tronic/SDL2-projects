from tkinter import Tk, Canvas
from random import randint, choice

width = 800
height = 450
thickness = 10
amount = 7
step = 10

window = Tk()

render = Canvas(window, width=width, height=height, bg='white')
render.pack(fill='both', expand=1)

# create coordinates
verticies = []
direction = []
for i in range(amount):
    new_verticy = [i*width/amount+width/(2*amount), randint(0, height)]
    verticies.append(new_verticy)
    direction.append(choice([-1,1]))

# print verticies on canvas
render_objects = []
for item in verticies:
    verticy = render.create_oval(item[0]-thickness/2, item[1]-thickness/2, item[0]+thickness/2, item[1]+thickness/2, fill='black')
    render_objects.append(verticy)

# create and print lines between verticies
lines = []
for i in range(amount-1):
    line = render.create_line(verticies[i][0], verticies[i][1], verticies[i+1][0], verticies[i+1][1])
    lines.append(line)

window.update()


def update_lines():
    for i in range(amount-1):
        render.coords(lines[i], verticies[i][0], verticies[i][1], verticies[i+1][0], verticies[i+1][1])
        render.update()

def update_verticies():
    for i in range(amount):
        render.coords(render_objects[i], verticies[i][0]-thickness/2, verticies[i][1]-thickness/2, verticies[i][0]+thickness/2, verticies[i][1]+thickness/2)

def move_verticies():
    for i in range(amount):
        verticies[i][1] += direction[i] * step
        if verticies[i][1]<=20:
            direction[i] = 1
        elif verticies[i][1]>=height-20:
            direction[i] = -1

# mainloop
from time import sleep
while True:
    sleep(.02)
    move_verticies()
    update_verticies()
    update_lines()
    window.update()
