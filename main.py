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
playerX_change = 0
playerY_change = 0

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
    
        # if key-stroke is pressed check whether it's right or left
        if event.type == pygame.KEYDOWN:
            print("KEYSTROKE PRESSED(anykey)")
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
                # print("LEFT ARROW")
            if event.key == pygame.K_RIGHT:
                # print("RIGHT ARROW")
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                # print("KEYSTROKE HAS RELEASED")

    playerX += playerX_change

    if playerX<=0:
        playerX = 0 
    elif playerX >= 736: #800-64 as 64 is the size of spaceship
        playerX = 736



    player(playerX,playerY)
    pygame.display.update() #MANDATORY
