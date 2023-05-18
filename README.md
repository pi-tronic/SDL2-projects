# SDL2 Projects

Really just everything I want to play around with.

Beware of non SDL2 code ;D

Sometimes python prototypes come first and I then switch to SDL2 and c++ to achieve more performance. \
Maybe I will even try out other media libraries at some point.

## Content

### Floating Lines

Randomly generated Points fly over the screen and if two points are close enough, a line will be drawn between them.

<img src="https://github.com/pi-tronic/SDL2-projects/blob/main/floating%20lines/screenshots/screenshot_03.png" width="500" height="370">

---
## How to compile and run

**If you can not find a build directory, you need to create one!**

<u>Compile:</u>

g++ -o build/{name} {directory}/{name}.cpp -lSDL2 -lSDL2main

<u>Run:</u>

./build/{name}