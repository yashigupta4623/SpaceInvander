import pygame 
import random

#initalizing the pygame
pygame.init() #MANDATORY

#to creating the screen
screen = pygame.display.set_mode((800, 600)) #800 = width and 600 = height

#Background
bg = pygame.image.load('background.png')

#title and icon 
pygame.display.set_caption("Space Invanders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#player 
playerImg = pygame.image.load('player.png')
playerX = 370 
playerY = 480 #lower value  inverse to height
playerX_change = 0
playerY_change = 0

#enemy 
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150) #lower value  inverse to height
enemyX_change = 4
enemyY_change = 40

#bullet
#ready - you can't see the bullet on screen
#fire - bullet is currently moving

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480 #lower value  inverse to height
bulletX_change = 4
bulletY_change = 10
bullet_state = "ready"


def player(x,y):
    screen.blit(playerImg,(x,y)) #blit means to draw

def enemy(x,y):
    screen.blit(enemyImg,(x,y)) #blit means to draw

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16,y+10)) #to set the bullet 

#Game Loop
running = True
while running:
     #rgb - red, green, blue (0 to 255)
    screen.fill((0,0,0))
    #background image
    screen.blit(bg,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False 
    
        # if key-stroke is pressed check whether it's right or left
        if event.type == pygame.KEYDOWN:
            print("KEYSTROKE PRESSED(anykey)")
            if event.key == pygame.K_LEFT:
                playerX_change = -5
                # print("LEFT ARROW")
            if event.key == pygame.K_RIGHT:
                # print("RIGHT ARROW")
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX,bulletY)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                # print("KEYSTROKE HAS RELEASED")

    playerX += playerX_change

    if playerX<=0:
        playerX = 0 
    elif playerX >= 736: #800-64 as 64 is the size of spaceship
        playerX = 736

#movement of enemy
    enemyX += enemyX_change

    if enemyX<=0:
        enemyX_change = 4
        enemyY +=  enemyY_change 
    elif enemyX >= 736: #800-64 as 64 is the size of spaceship
        enemyX_change = -4 
        enemyY +=  enemyY_change 




    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update() #MANDATORY
