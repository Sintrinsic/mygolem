'''
Created on Aug 30, 2015

@author: v
'''
import os, sys
import pygame
from pygame.locals import *
from helpers import *
from Tank import *
from Tile import *
from Tile_Conveyer import *

#V's random edit. HII!!!
if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class PyManMain:
    """The Main PyMan Class - This class handles the main 
    initialization and creating of the Game."""
    
    def __init__(self, width=25,height=17):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""

        self.width = width*50
        self.height = height*50
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width , self.height))
        self.tiles = []
        self.tank = Tank()
        self.tank_sprites = pygame.sprite.RenderPlain((self.tank))
        self.LoadBoard()


    def MainLoop(self):
        """This is the Main Loop of the Game"""
        while 1:
            self.DrawBoard()

            for event in pygame.event.get():
                """Load All of our Sprites"""
                self.LoadSprites();
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == KEYDOWN:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        self.tank.move(event.key)
            self.tank_sprites.draw(self.screen)
            pygame.display.flip()

    def LoadSprites(self):
        """Load the sprites that we need"""
        pygame.sprite.RenderPlain((self.tank))
           
    def LoadBoard(self):
        y=0
        x=0
        level = open("levels/level1.lvl","r").read()
        for row in level.split("\n"):
            print "newline"
            for element in row.split(","):
                tileMeta = element.split(":")
                rot=1
                if len(tileMeta)>1: rot=tileMeta[1]
                newTile = ""
                if(tileMeta[0]=="0"):
                    newTile = Tile(x,y)
                elif(tileMeta[0]=="1"):
                    newTile  = Tile_Conveyer(x,y,rot)
                tileSprite = pygame.sprite.RenderPlain(newTile)
                tileSprite.draw(self.screen)
                self.tiles.append((newTile,tileSprite))
                
                x+=1
            y+=1
            self.width=x*50
            self.height=y*50
            x=0
        self.screen = pygame.display.set_mode((self.width , self.height))

                    
    def DrawBoard(self):
        for tile in self.tiles:
            tile[1].draw(self.screen)
