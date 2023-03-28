import pygame 

#initalizing the pygame
pygame.init() #MANDATORY

#to creating the screen
screen = pygame.display.set_mode((800, 600)) #800 = width and 600 = height

#title and icon 
pygame.display.set_caption("Space Invanders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#player 
playerImg = pygame.image.load('player.png')
playerX = 370 
playerY = 480 #lower value  inverse to height
# playerX_change = 0
# playerY_change = 0

def player(x,y):
    screen.blit(playerImg,(x,y)) #blit means to draw


#Game Loop
running = True
while running:
     #rgb - red, green, blue (0 to 255)
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False 


    

    player(playerX,playerY)
    pygame.display.update() #MANDATORY