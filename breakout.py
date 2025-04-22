import pygame as pg
import os
import sys
import numpy as np
import math

pg.init()
pg.display.set_caption('Practice game')
running = True
screenSize = (1280, 720)
surface = pg.display.set_mode(screenSize)
bg = pg.color.Color((0, 0, 0))
fpsClock = pg.time.Clock()
fpsClock.tick(30)
font = pg.font.Font('freesansbold.ttf', 32)
lives = 3
text = font.render(f'Lives: {lives}', True, (255, 255, 255))
textRect = text.get_rect()
textRect.center = (1000, 50)
gameOver = False
gameOverText = font.render('GAME OVER', True, (255, 255, 255))
gameOverTextRect = gameOverText.get_rect()
gameOverTextRect.center = (screenSize[0] // 2, screenSize[1] // 2)

# Bat and control by player
playerY = 540
mouseX, mouseY = (0, playerY)
batWidth = 100
bat = pg.rect.Rect((mouseX, mouseY, batWidth, 10))


# Bricks why did i store the objects as arrays, doesnt really make sense
bricksX, bricksY = (15, 6)
mult = bricksX*bricksY
bricksArray = [None] * (mult)
counter = 0
gapX = math.floor((screenSize[0] -200)/bricksX)
gapY = math.floor((screenSize[1]*0.25)/bricksY)
brickWidth, brickHeight = (math.floor(0.9*gapX), math.floor(0.8*gapY))

for i in range(bricksX):
    for j in range(bricksY):
        bricksArray[counter] = (100 + gapX*i, 50 + gapY*j)
        counter += 1

rect_list = [None] * mult

for bricks in range(len(bricksArray)):
    if bricks != None:
        rect_list[bricks] = pg.rect.Rect(bricksArray[bricks], (brickWidth, brickHeight))

rect_list = [x for x in rect_list if x != None]

# Ball
ballPos = (screenSize[0]/2, screenSize[1]/2)
ballRad = 8
ballsurf = pg.surface.Surface(screenSize)
ballRect = pg.draw.circle(surface, (255, 255, 255), ballPos, ballRad)
Velocity = [0, 2]
move = False





while running:
    surface.fill(bg)
    surface.fill((0, 0, 255), bat)

    surface.fill((0, 255, 0), ballRect)

    

    # Add velocity on ball when the game starts
    if move == True:
        ballRect[0] += Velocity[0]
        ballRect[1] += math.ceil(Velocity[1])
        # print(Velocity)

    
    # Change velocity when certain things happen
    if ballRect.left <= -2:
        ballRect.left += 5
        Velocity[0] = math.ceil(Velocity[0] * -1)
        # collideTimer = 5

    if ballRect.right >= screenSize[0] + 2:
        ballRect.right -= 5
        Velocity[0] = math.floor(Velocity[0] * -1)

    if ballRect.top <= 1:
        ballRect.top += 1
        Velocity[1] = Velocity[1] * -1
        # collideTimer = 5

    if ballRect.bottom >= screenSize[1]:
        ballRect.center = ballPos
        Velocity = [0, 2]
        
        if lives > 0:
            lives -= 1
            text = font.render(f'Lives: {lives}', True, (255, 255, 255))

    if lives == 0:
        surface.blit(gameOverText, gameOverTextRect)


    # for bricks in bricksArray:
    #     if bat.collidepoint(ballRect.topleft):
    #         print('top-left collision')
    #         if bricks.right == ballRect.left:
    #             Velocity[0] = Velocity[0] * -1
    #         elif bricks.bottom == ballRect.top:
    #             Velocity[1] = Velocity[1] * -1
    #         bricks = None

    #     if bat.collidepoint(ballRect.bottomright):
    #         print('bot-right collision')
    #         if bricks.left == ballRect.right:
    #             Velocity[0] = Velocity[0] * -1
    #         if bricks.top == ballRect.bottom:
    #             Velocity[1] = Velocity[1] * -1
    #         bricks = None

    
            

    for bricks in rect_list:
        if bricks != None:
            surface.fill((255, 0, 0), bricks)

    surface.blit(text, textRect)


    if ballRect.collidelist != -1:

        collideIndex = ballRect.collidelist([x for x in rect_list if x != None])

        if bat.collidepoint((ballRect.left, ballRect.bottom)) or bat.collidepoint((ballRect.right, ballRect.bottom)):
            batCollideLength = ballRad + ballRect.left - bat.left
            batCollideLengthDir = (batWidth/2) - batCollideLength
            Velocity[0] -= batCollideLengthDir/(batWidth/2)
            Velocity[1] = Velocity[1] * -1
            
        elif collideIndex != -1:

            brickHit = rect_list[collideIndex]

            if ballRect.x <= brickHit.left and ballRect.x >=brickHit.right:
                
                print('left collision detected')
                Velocity[0] *= -1
            
            else:
                
                print('bot collision detected')
                Velocity[1] *= -1

            del rect_list[collideIndex]
            
            
    

    

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.MOUSEMOTION:
            mouseX, mouseY = event.pos
            bat.topleft = (mouseX, playerY)
            move = True

        if event.type == pg.KEYUP:
            if event.key == pg.K_r:
                ballRect.center = ballPos
                Velocity = [0, 2]
    


    pg.display.update()