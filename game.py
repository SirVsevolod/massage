#!/usr/bin/python
import pygame,sys
import hero
#import pygame.locals

#hero.hero(55,55)
left = right = down = up = False

x = 0
y = 0

platfom_width = 32
platform_height = 32
platform_color = (0,255,0)

level = [
       "-------------------------",
       "-                       -",
       "-                       -",
       "-                       -",
       "-            --         -",
       "-                       -",
       "--                      -",
       "-                       -",
       "-                   --- -",
       "-                       -",
       "-                       -",
       "-      ---              -",
       "-                       -",
       "-   -----------         -",
       "-                       -",
       "-                -      -",
       "-                   --  -",
       "-                       -",
       "-                       -",
       "-------------------------"]

pygame.init()
win = pygame.display.set_mode((800,640))

pygame.display.set_caption("GOD,PLEASE")

run = True
while run:
    
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    x=y=0 # координаты
    for row in level: # вся строка
        for col in row: # каждый символ
            if col == "-":
              #создаем блок, заливаем его цветом и рисеум его
                pygame.draw.rect(win,(platform_color),(x,y,platfom_width,platform_height))    
            x += platfom_width #блоки платформы ставятся на ширине блоков
        y += platform_height    #то же самое и с высотой
        x = 0      
    
    hero.hero(55,55)

    if event.type == pygame.KEYDOWN and event.key == K_LEFT:
        left = True

    if event.type == pygame.KEYDOWN and event.key == K_RIGHT:
        right = True

    if event.type == pygame.KEYDOWN and event.key == K_UP:
        up = True

    if event.type == pygame.KEYDOWN and event.key == K_DOWN:
        down = True



    if event.type == pygame.KEYUP and event.key == K_LEFT:
        left = False

    if event.type == pygame.KEYUP and event.key == K_RIGHT:
        right = False

    if event.type == pygame.KEYUP and event.key == K_UP:
        up = False
    
    if event.type == pygame.KEYUP and event.key == K_DOWN:
        down = False


    hero.hero.update(left,right,up,down)
    hero.draw(win)
    pygame.display.update()

pygame.quit()