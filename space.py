import pygame, sys
pygame.init()

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 600
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption("Space Invaders")

#Icon of game
icon = pygame.image.load("spaceship32.png")
pygame.display.set_icon(icon)

#Player setting
playerImg = pygame.image.load("spaceship64.png")
playerX = 370
playerY = 480 
#modify player function to accept x coordinates
def player(x, y):
          screen.blit(playerImg, (x, y))


looping = True
while looping:
    # Get inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()#updates screens
    screen.fill((245, 200, 255))#light purple
#PLAYER MOVEMENT
#get_pressed returns keys on the keyboard
    player(playerX, playerY)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
       playerX -= .5
    elif pressed[pygame.K_RIGHT]:
        playerX += .5
    
    if playerX >=  736:
        playerX = 736
    elif playerX <= 0:
        playerX = 0
    
    

  

