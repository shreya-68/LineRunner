import math
import os
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from stat import S_ISDIR, S_ISREG
from pygame.locals import *
import logging
import sys

from state import Guy
from text import Text

city_texture_inited = False

class World(object):
    def __init__(self):
        global city_texture_inited, textures
        pygame.display.set_caption("Game")
        if not city_texture_inited:
            city_texture_inited = True
            InitTextGL()
        # layout will update this
        # since it is used every time in display
        # and its best to calculate it only once
        self.texture = textures[0]

        #dim = 20
        self.intersecting = False
        self.render_center = (0, 0)
        self.render_radius = 50

        self.camera_y = 10
        self.camera_y_min = 1.2
        self.first_run = True

        self.guy = Guy()
        self.text = Text(25)

    def display(self):
        glClearColor(1, 1, 1, 1)

        self.drawGround()
        self.drawBar()
        text = 'Level ' + str(self.guy.level)
        self.text.display(text,7,8,25)
        text = 'Cross ' + str(5 - self.guy.boxperlevel) + 'boxes to reach next level'
        self.text.display(text,6,7,15)

        glPushMatrix()
        glTranslatef(-self.guy.posx, 0.0, 0.0)
        box_place = 10 
        self.drawBox(box_place)
        box_place = box_place - 20
        self.drawBox(box_place)
        box_place = box_place + 40
        self.drawBox(box_place)
        glPopMatrix()
        #self.drawDepth()
        #self.drawBackground()
        self.guy.display()
        glFlush()

    def update(self):
        pass

    def handle_keypress(self, event, x, y, world):
        self.guy.handle_keypress(event, x, y, world)
        return
        #self.background.handle_keypress(event, x, y)

    def handle_keyrelease(self, event, x, y, world):
        self.guy.handle_keyrelease(event, x, y, world)
        return

    def drawBar(self):
        glPushMatrix()
        glColor3f(1, 0, 0)
        glTranslatef(-8, 8, 0.0)
        glScalef(1.5 - (self.guy.height*0.1)/2, 0.2, 0.2)
        glBegin(GL_QUADS);
        glVertex3f( 1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0,-1.0, 1.0)
        glVertex3f( 1.0,-1.0, 1.0)
        glEnd()    
        glPopMatrix()
        
    def drawBox(self, box_place):
        glBindTexture(GL_TEXTURE_2D, textures[3])
        glPushMatrix()
        glTranslatef(box_place, 0.5, 0.0)
        glBegin(GL_QUADS);
        glTexCoord2f(0.0,0.0); glVertex3f( 1.0, 1.0,-1.0)
        glTexCoord2f(1.0,0.0); glVertex3f(-1.0, 1.0,-1.0)
        glTexCoord2f(0.0,1.0); glVertex3f(-1.0, 1.0, 1.0)
        glTexCoord2f(1.0,1.0); glVertex3f( 1.0, 1.0, 1.0)
        glTexCoord2f(0.0,0.0); glVertex3f( 1.0,-1.0, 1.0)
        glTexCoord2f(1.0,0.0); glVertex3f(-1.0,-1.0, 1.0)
        glTexCoord2f(0.0,1.0); glVertex3f(-1.0,-1.0,-1.0)
        glTexCoord2f(1.0,1.0); glVertex3f( 1.0,-1.0,-1.0)
        glTexCoord2f(0.0,0.0); glVertex3f( 1.0, 1.0, 1.0)
        glTexCoord2f(1.0,0.0); glVertex3f(-1.0, 1.0, 1.0)
        glTexCoord2f(1.0,1.0); glVertex3f(-1.0,-1.0, 1.0)
        glTexCoord2f(0.0,1.0); glVertex3f( 1.0,-1.0, 1.0)
        glTexCoord2f(0.0,0.0); glVertex3f( 1.0,-1.0,-1.0)
        glTexCoord2f(1.0,0.0); glVertex3f(-1.0,-1.0,-1.0)
        glTexCoord2f(1.0,1.0); glVertex3f(-1.0, 1.0,-1.0)
        glTexCoord2f(0.0,1.0); glVertex3f( 1.0, 1.0,-1.0)
        glTexCoord2f(0.0,0.0); glVertex3f(-1.0, 1.0, 1.0)
        glTexCoord2f(1.0,0.0); glVertex3f(-1.0, 1.0,-1.0)
        glTexCoord2f(1.0,1.0); glVertex3f(-1.0,-1.0,-1.0)
        glTexCoord2f(0.0,1.0); glVertex3f(-1.0,-1.0, 1.0)
        glTexCoord2f(0.0,0.0); glVertex3f( 1.0, 1.0, 1.0)
        glTexCoord2f(1.0,0.0); glVertex3f( 1.0, 1.0,-1.0)
        glTexCoord2f(1.0,1.0); glVertex3f( 1.0,-1.0,-1.0)
        glTexCoord2f(0.0,1.0); glVertex3f( 1.0,-1.0, 1.0)
        glEnd()    
        glPopMatrix()
        glBindTexture(GL_TEXTURE_2D, 0)


    def drawBackground(self):
        glBindTexture(GL_TEXTURE_2D, textures[1])
        glPushMatrix()
        #glTranslatef(0.0,50,0.0)
        glBegin(GL_QUADS);
        #glColor3f(1, 1, 1)
        glTexCoord2f(0.0,1.0); glVertex3f(-100, 100,-12)
        glTexCoord2f(0.0,0.0); glVertex3f(-100,-100,-12)
        glTexCoord2f(1.0,0.0); glVertex3f( 100,-100,-12)
        glTexCoord2f(1.0,1.0); glVertex3f( 100, 100,-12) 
        glEnd()    
        glPopMatrix()
        glBindTexture(GL_TEXTURE_2D, 0)

    def drawGround(self):
        glBindTexture(GL_TEXTURE_2D, textures[0])
        glPushMatrix()
        glBegin(GL_QUADS)                # Start Drawing The Ground

        # Bottom Face
        glTexCoord2f(8.0,8.0); glVertex3f(-40, 0, -40)    # Top Right Of The Texture and Quad
        glTexCoord2f(0.0, 8.0); glVertex3f(40, 0, -40)    # Top Left Of The Texture and Quad
        glTexCoord2f(0.0, 0.0); glVertex3f(40, 0, 40)    # Bottom Left Of The Texture and Quad
        glTexCoord2f(8.0, 0.0); glVertex3f(-40, 0, 40)    # Bottom Right Of The Texture and Quad

        glEnd()
        glPopMatrix()
        glBindTexture(GL_TEXTURE_2D, 0)

    def drawDepth(self):
        glBindTexture(GL_TEXTURE_2D, textures[2])
        glPushMatrix()
        glBegin(GL_QUADS);
        glTexCoord2f(0.0,1.0); glVertex3f(-20, 0, 20)
        glTexCoord2f(0.0,0.0); glVertex3f(-20,-4, 20)
        glTexCoord2f(1.0,0.0); glVertex3f( 20,-4, 20)
        glTexCoord2f(1.0,1.0); glVertex3f( 20, 0, 20) 
        glEnd()    
        glBegin(GL_QUADS);
        glTexCoord2f(0.0,1.0); glVertex3f(20, 0, 20)
        glTexCoord2f(0.0,0.0); glVertex3f(20,-4, 20)
        glTexCoord2f(1.0,0.0); glVertex3f(20,-4,-20)
        glTexCoord2f(1.0,1.0); glVertex3f(20, 0,-20) 
        glEnd()    
        glBegin(GL_QUADS);
        glTexCoord2f(0.0,1.0); glVertex20f( 20, 0,-20)
        glTexCoord2f(0.0,0.0); glVertex20f( 20,-4,-20)
        glTexCoord2f(1.0,0.0); glVertex20f(-20,-4,-20)
        glTexCoord2f(1.0,1.0); glVertex20f(-20, 0,-20) 
        glEnd()    
        glBegin(GL_QUADS);
        glTexCoord2f(0.0,1.0); glVertex20f(-20, 0,-20)
        glTexCoord2f(0.0,0.0); glVertex20f(-20,-4,-20)
        glTexCoord2f(1.0,0.0); glVertex20f(-20,-4, 20)
        glTexCoord2f(1.0,1.0); glVertex20f(-20, 0, 20) 
        glEnd()    
        glPopMatrix()
        glBindTexture(GL_TEXTURE_2D, 0)

def InitTextGL():
    LoadTextures(4)
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

def CreateTexture(imagename, number):
    global textures

    image = pygame.image.load(imagename)
    iw = image.get_width()
    ih = image.get_height()
    image_surface = pygame.image.tostring(image, "RGBA", 1)

    glBindTexture(GL_TEXTURE_2D, int(textures[number]))

    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, iw, ih, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_surface)
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

def LoadTextures(number):
    global textures
    textures = glGenTextures(number)
    CreateTexture("ground.jpg", 0)
    CreateTexture("background.jpg", 1)
    CreateTexture("side.jpg", 2)
    CreateTexture("wood.jpeg", 3)
