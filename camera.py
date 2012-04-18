from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
import pygame
import os
import sys
from pygame.locals import *


VIEW_WIDTH = 500
VIEW_HEIGHT = 500

class Camera(object):

    def __init__(self):
        self.eyex = 0.0
        self.eyey = 2.0
        self.eyez = 8.0
        self.centerx = 0.0
        self.centery = 0.0
        self.centerz = 0.0
        self.upx = 0.0
        self.upy = 1.0
        self.upz = 0.0




