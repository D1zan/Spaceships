import pygame, sys, random
pygame.init()

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 600
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
background = pygame.image.load("bg.jpg")
pygame.display.set_caption("Space Invaders")

#Icon of game
icon = pygame.image.load("spaceship32.png")
pygame.display.set_icon(icon)

#Player setting
playerImg = pygame.image.load("spaceship64.png")
playerX = 370
playerY = 480 

#Enemy settings
enemyX = random.randint(0, 800 - 64)
enemyY = random.randint(50 ,150 )
enemyX_momentum = .05 # enemy starts moving right
enemyY_momentum = 10 
enemyImg = pygame.image.load("alien64 (1).png")
#modify player function to accept x coordinates
#blit draws the player on the screen 
def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

looping = True
while looping:
    # Get inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))
    screen.blit(background, (0,0))
#PLAYER MOVEMENT
#get_pressed returns keys on the keyboard


    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
       playerX -= .5
    elif pressed[pygame.K_RIGHT]:
        playerX += .5
    
    if playerX >=  736:
        playerX = 736
    elif playerX <= 0:
        playerX = 0


    enemyX += enemyX_momentum

    #enemy boundaries
    if enemyX >= 736:
        enemyX_momentum = -.07
        enemyY += enemyY_momentum
    elif enemyX <= 0:
        enemyX_momentum = .07
        enemyY += enemyY_momentum
    
    

    player(playerX, playerY)
    enemy(enemyX, enemyY)
  
    
    pygame.display.update()#updates screens
