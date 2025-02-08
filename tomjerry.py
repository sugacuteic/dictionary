import pgzrun
from random import randint
WIDTH = 600
HEIGHT = 600
score = 0
gameover = False
tom = Actor("tom.png")
tom.pos = WIDTH/2, HEIGHT/2
jerry2 = Actor("jerry2.png")
jerry2.pos = 200,100
def draw():
    screen.blit("background.jpg", (0,0))
    jerry2.draw()
    tom.draw()
    if gameover:
        screen.fill("orange")
        screen.draw.text("Times up! Here is your final score..." + str(score), midtop = (WIDTH / 2, 10), fontsize = 35, color = "Black")

def update():
    global score
    print(tom.x, tom.y)
    if keyboard.left:
        tom.x -= 2
    if keyboard.right:
        tom.x += 2
    if keyboard.up:
        tom.y -= 2
    if keyboard.down:
        tom.y +=2
    if tom.x <= -50:
        tom.x = WIDTH + 50
    if tom.x > WIDTH + 50:
        tom.x = -40
    if tom.y < 0:
        tom.y = HEIGHT + 50
    if tom.y > HEIGHT:
        tom.y = -40
    jerry_caught = tom.colliderect(jerry2) 
    if jerry_caught:
        score += 10
        jerry2.x = randint(50, WIDTH - 50)   
        jerry2.y = randint(50, HEIGHT - 50)










pgzrun.go()