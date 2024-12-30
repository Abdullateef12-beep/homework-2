import pgzrun
from random import randint


WIDTH = 500
HEIGHT = 500
TITLE = "SHOOTING THE BOTILA"

message = ""

botila = Actor('botila')
# alien.pos = 50,50


def draw():
    screen.clear()
    screen.fill(color = (255 , 20 , 45))

    place_botila.draw()
    screen.draw.text(message , (400,10) ,fontsize=30 )



def place_botila():
    botila.x = randint(50 , WIDTH - 50 )
    botila.y = randint(50 , HEIGHT - 50 )





def on_mouse_down(pos):
    global message

    if botila.collidepoint(pos):
        message = "Good shot"
        place_botila()
    else :
        message = "try again"



place_botila()






pgzrun.go()
