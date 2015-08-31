'''
Created on Aug 30, 2015

@author: v
'''
from helpers import *
from pygame import *
class Tile_Conveyer(sprite.Sprite):
    """This is our snake that will move around the screen"""
    
    def __init__(self,x,y,rot=1):
        sprite.Sprite.__init__(self) 
        self.original_image, self.rect = load_image('conveyer.png',-1)
        self.image = rot_center(self.original_image,90*float(rot))
        ypos = y*50
        self.rect.y = ypos
        self.rect.x = x*50

    def doAction(self,tank):
        pass
    
    def updateImg(self):
        pass