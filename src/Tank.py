'''
Created on Aug 30, 2015

@author: v
'''
from helpers import *
from pygame import *
class Tank(sprite.Sprite):
    """This is our snake that will move around the screen"""
    
    def __init__(self):
        sprite.Sprite.__init__(self) 
        self.original_image, self.rect = load_image('tank.png',-1)
        self.image = self.original_image
        self.x = 0
        self.y = 0
        
    def move(self, key):
        """Move your self in one of the 4 directions according to key"""
        """Key is the pyGame define for either up,down,left, or right key
        we will adjust ourselves in that direction"""

        
        if (key == K_RIGHT):
            self.x = self.x +50
            self.image = self.original_image
        elif (key == K_LEFT):
            self.x = self.x - 50
            self.image = rot_center(self.original_image,180)
        elif (key == K_UP):
            self.y = self.y - 50
            self.image = rot_center(self.original_image,90)
        elif (key == K_DOWN):
            self.image = rot_center(self.original_image,-90)
            self.y = self.y + 50
        print str(self.x)+" "+str(self.y)
        self.rect.x=self.x
        self.rect.y=self.y