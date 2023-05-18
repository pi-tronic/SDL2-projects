#####################################
#                                   #
# nur für genau drei verticies !!!  #
#                                   #
#####################################

from tkinter import Tk, Canvas
from random import randint, choice
from time import sleep

size = [1600, 900]
thickness = 10
max_dist = 500
step = 5
amount = 6

window = Tk()

render = Canvas(window, width=size[0], height=size[1], bg='white')
render.pack(fill='both', expand=1)

verticies = []
direction = []

for i in range(amount):
    new_verticy = [randint(20,size[0]-20), randint(20,size[1]-20)]
    verticies.append(new_verticy)
    dirx = choice([-1,1])*randint(1,2)
    diry = choice([-1,1])*randint(1,2)
    direction.append([dirx, diry])


render_objects = []
for item in verticies:
    verticy = render.create_oval(item[0]-thickness/2, item[1]-thickness/2, item[0]+thickness/2, item[1]+thickness/2, fill='black')
    render_objects.append(verticy)

lines = []
for i in range(len(verticies)-1):
    line = render.create_line(verticies[i][0], verticies[i][1], verticies[i+1][0], verticies[i+1][1])
    lines.append(line)
line = render.create_line(verticies[-1][0], verticies[-1][1], verticies[0][0], verticies[0][1])
lines.append(line)

window.update()


def move_verticies():
    for i in range(len(verticies)):
        for d in range(len(direction[i])):
            verticies[i][d] += direction[i][d] * step
            if verticies[i][d]<=20 or verticies[i][d]>=size[d]-20:
                direction[i][d] *= -1

def update_verticies():
    for i in range(len(verticies)):
        render.coords(render_objects[i], verticies[i][0]-thickness/2, verticies[i][1]-thickness/2, verticies[i][0]+thickness/2, verticies[i][1]+thickness/2)

def calc_width(x1, y1, x2, y2):
    lenght = ((x2-x1)**2+(y2-y1)**2)**.5
    width = 300/lenght
    if width>thickness:
        width = thickness
    elif lenght>max_dist:
        width = 0
    return width

def update_lines():
    for i in range(len(verticies)-1):
        if [verticies[i][0], verticies[i][1]]!=[verticies[i+1][0], verticies[i+1][1]]:
            width = calc_width(verticies[i][0], verticies[i][1], verticies[i+1][0], verticies[i+1][1])
            if width!=0:
                render.coords(lines[i], verticies[i][0], verticies[i][1], verticies[i+1][0], verticies[i+1][1])
                render.itemconfig(lines[i], width=width)
            else:
                render.coords(lines[i], -1, -1, 0, -1)
            render.update()
    # vllt unnötig
    if [verticies[-1][0], verticies[-1][1]]!=[verticies[0][0], verticies[0][1]]:
            width = calc_width(verticies[-1][0], verticies[-1][1], verticies[0][0], verticies[0][1])
            if width!=0:
                render.coords(lines[-1], verticies[-1][0], verticies[-1][1], verticies[0][0], verticies[0][1])
                render.itemconfig(lines[-1], width=width)
            else:
                render.coords(lines[-1], -1, -1, 0, -1)
            render.update()

while True:
    sleep(.02)
    move_verticies()
    update_verticies()
    update_lines()
    window.update()
