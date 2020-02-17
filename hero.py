#!/usr/bin/python

import  pygame

speed = 5

width = 22
height = 32
color = (100,255,100)

class hero():
    def __init__(self,x,y):
        
        self.xvel = 0
        self.startX = x
        self.yvel = 0
        self.startY = y
        '''self.image = Surface((width,height))
                                self.image.fill(Color(color))
                                self.rect = Rect(x,y,width,height)'''

    def update(self,left,right,up,down):
        if left: 
            self.xvel= -speed

        if right:
            self.xvel = speed

        if down:
            self.yvel = speed

        if up:
            self.yvel = -speed 

        if not(left or rigth or down or up):
            self.xvel = 0
            self.yvel = 0

        #self.rect.x += self.xvel
        #self.rect.y += self.yvel

    def draw(self,win):
        pygame.draw.rect(win,(color),(rect.x,rext.y,width,height))
