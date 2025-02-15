import pgzrun, random
from time import time

WIDTH = 800
HEIGHT = 600
TITLE = "satellite game"
satellites = []
lines = []
nextsatellite = 0
num = random.randint(5,10)
starttime = 0
totaltime = 0
endtime = 0

def create_satellites():
    global starttime 
    for i in range(num):
        satellite = Actor("satellite2.png")
        satellite.pos = random.randint(50,WIDTH - 50), random.randint(50, HEIGHT - 50)
        satellites.append(satellite)
    starttime = time()
def draw():
    global totaltime
    screen.blit("spacee.png", (10,20))
    for i, value in enumerate(satellites) :
        value.draw()
        screen.draw.text(str(i+1), (value.pos[0], value.pos[1] + 20))
    for i in lines:
        screen.draw.line(i[0], i[1], "White") 
    if nextsatellite < num:
        totaltime = time() - starttime
        screen.draw.text(str(round(totaltime, 1)), (50, 10), fontsize = 30) #rounding totaltime to the nearest 1
    else:
        screen.draw.text(str(round(totaltime, 1)), (50, 10), fontsize = 30) 
def update():
    pass
def on_mouse_down(pos):
    global lines, nextsatellite 
    if nextsatellite < num:
        if satellites[nextsatellite].collidepoint(pos):
            if nextsatellite:
                lines.append((satellites[nextsatellite - 1].pos, satellites[nextsatellite].pos))
            nextsatellite += 1
        else:
            lines = []
            nextsatellite = 0
    


create_satellites()

pgzrun.go()