import pgzrun
import random
WIDTH = 400
HEIGHT = 400
TITLE = "gradient tangle"


def draw():
    r = 255
    g = 0
    b = random.randint(0,255)
    w = WIDTH - 10
    h = HEIGHT /2
    for i in range(20):
        rect = Rect((0,0) , (w, h))
        rect.center = 200,200
        screen.draw.rect(rect, (r,g,b))
        r -= 10
        g += 10
        w -=10
        h += 10

pgzrun.go()

