from tkinter import Tk, Canvas
from random import randint, choice
from time import sleep

bg = 'grey'
fg = 'white'
size = [800, 450]
thickness = 10
max_dist =200
offset = 0
step = 3
amount = 10

window = Tk()

render = Canvas(window, width=size[0], height=size[1], bg=bg)
render.pack(fill='both', expand=1)

verticies = []
direction = []

for i in range(amount):
    new_verticy = [randint(offset,size[0]-offset), randint(offset,size[1]-offset)]
    verticies.append(new_verticy)
    dirx = choice([-1,1])*randint(1,2)
    diry = choice([-1,1])*randint(1,2)
    direction.append([dirx, diry])


render_objects = []
for item in verticies:
    verticy = render.create_oval(item[0]-thickness/2, item[1]-thickness/2, item[0]+thickness/2, item[1]+thickness/2, fill=fg, outline=fg)
    render_objects.append(verticy)

lines = []
for a in range(len(verticies)-1):
    line_section = []
    for b in range(len(verticies)-a):
        if [verticies[a][0], verticies[a][1]]!=[verticies[a+b][0], verticies[a+b][1]]:
            line = render.create_line(verticies[a][0], verticies[a][1], verticies[a+b][0], verticies[a+b][1], fill=fg)
            line_section.append(line)
    lines.append(line_section)
window.update()


def move_verticies():
    size = [render.winfo_width(), render.winfo_height()]

    for i in range(len(verticies)):
        for d in range(len(direction[i])):
            verticies[i][d] += direction[i][d] * step
            if verticies[i][d]<=offset or verticies[i][d]>=size[d]-offset:
                direction[i][d] *= -1

def update_verticies():
    for i in range(len(verticies)):
        render.coords(render_objects[i], verticies[i][0]-thickness/2, verticies[i][1]-thickness/2, verticies[i][0]+thickness/2, verticies[i][1]+thickness/2)

def calc_width(x1, y1, x2, y2):
    lenght = ((x2-x1)**2+(y2-y1)**2)**.5
    width = (max_dist*thickness)/(10*lenght)
    if width>thickness:
        width = thickness
    elif lenght>max_dist:
        width = 0
    return width

def update_lines():
    for a in range(len(verticies)-1):
        for b in range(len(verticies)-a):
            if [verticies[a][0], verticies[a][1]]!=[verticies[a+b][0], verticies[a+b][1]]:
                width = calc_width(verticies[a][0], verticies[a][1], verticies[a+b][0], verticies[a+b][1])
                if width!=0:
                    render.coords(lines[a][b-1], verticies[a][0], verticies[a][1], verticies[a+b][0], verticies[a+b][1])
                    render.itemconfig(lines[a][b-1], width=width)
                else:
                    render.coords(lines[a][b-1], -1, -1, 0, -1)
                render.update()

while True:
    sleep(.01)
    move_verticies()
    update_verticies()
    update_lines()
    window.update()
