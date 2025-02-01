import pgzrun
from random import randint
WIDTH = 600
HEIGHT = 600
score = 0
gameover = False
bee = Actor("bee.png")
bee.pos = WIDTH/2, HEIGHT/2
flower = Actor("flower.png")
flower.pos = 200,100
def draw():
    screen.blit("background.jpg", (0,0))
    flower.draw()
    bee.draw()
    if gameover:
        screen.fill("orange")
        screen.draw.text("Times up! Here is your final score..." + str(score), midtop = (WIDTH / 2, 10), fontsize = 35, color = "Black")

def update():
    global score
    print(bee.x, bee.y)
    if keyboard.left:
        bee.x -= 2
    if keyboard.right:
        bee.x += 2
    if keyboard.up:
        bee.y -= 2
    if keyboard.down:
        bee.y +=2
    if bee.x <= -50:
        bee.x = WIDTH + 50
    if bee.x > WIDTH + 50:
        bee.x = -40
    if bee.y < 0:
        bee.y = HEIGHT + 50
    if bee.y > HEIGHT:
        bee.y = -40
    flower_collect = bee.colliderect(flower) 
    if flower_collect:
        score += 10
        flower.x = randint(50, WIDTH - 50)   
        flower.y = randint(50, HEIGHT - 50)
def timeup():
    global gameover
    gamover = True
clock.schedule(timeup, 7.0)









pgzrun.go()