'''
Created on Aug 30, 2015

@author: v
'''
import os, sys
import pygame
from pygame.locals import *
from PyManMain import PyManMain

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'


if __name__ == '__main__':
    MainWindow = PyManMain()
    MainWindow.MainLoop()
#testing