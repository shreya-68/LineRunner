import os
import sys
import math
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *

VIEW_WIDTH = 500
VIEW_HEIGHT = 500
class Backdrop(object):

    global textures
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(10,100)
        pygame.display.set_mode((VIEW_WIDTH, VIEW_HEIGHT), OPENGLBLIT|DOUBLEBUF)
        #pygame.display.set_mode((VIEW_WIDTH, VIEW_HEIGHT), 0, 32)
        pygame.display.set_caption("Moving Bot")
        initTexGL()
        self.texture = textures
        #self.reshape(VIEW_WIDTH, VIEW_HEIGHT)
        pygame.display.flip()

    def reshape(self, w, h):
        #print 'Robot.reshape'
        glViewport(0, 0, w, h)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(90, w*1.0/h, 1.0, 15.0)

        #glMatrixMode(GL_MODELVIEW)
        #glLoadIdentity()
        #glTranslatef(0.0, 0.0, -5.0)

        gluLookAt(0.0, 0.0, 6.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)


    def display(self):

        glClear(GL_COLOR_BUFFER_BIT)
        glDisable(GL_LIGHTING)
        glTranslatef(1.5,0.0,-6.0);
        self.DrawGround()
        glEnable(GL_BLEND)
        glDepthMask(GL_FALSE)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE)
        glDepthMask(GL_TRUE)
        glDisable(GL_BLEND)
        self.reshape(VIEW_WIDTH, VIEW_HEIGHT)

        glFlush()

    def DrawGround(self):
        glBindTexture(GL_TEXTURE_2D, self.texture)
        #glPushMatrix()
        glBegin(GL_QUADS)

        glTexCoord2f(1.0,0.0); glVertex3f(2.0, -2.0,0) #glVertex3f(100,0,-100)
        glTexCoord2f(1.0,1.0); glVertex3f( 2.0, 2.0,0) #glVertex3f(100,0,100) 
        glTexCoord2f(0.0,1.0); glVertex3f(-2.0, 2.0,0) #glVertex3f(-100,0,100)
        glTexCoord2f(0.0,0.0); glVertex3f(-2.0,-2.0,0) #glVertex3f(-100,0,-100)

        glEnd()
        #glPopMatrix()
        #glBindTexture(GL_TEXTURE_2D, 0)

    def main(self):

        print 'main'
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)

            self.display()
            pygame.time.wait(10)

def initTexGL():
    glutInit(sys.argv)
    glEnable(GL_TEXTURE_2D)
    LoadTextures(1)
    glClearColor(0.0,0.0,0.0,0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

def CreateTexture(imagename, number):
    global textures

    image = pygame.image.load(imagename)
    iw = image.get_width()
    ih = image.get_height()
    texture_data = pygame.image.tostring(image, "RGBA", 1)
    print iw
    print ih
    print textures
    glBindTexture(GL_TEXTURE_2D, textures)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, iw, ih, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    print 'texture created'


def LoadTextures(number):
    global textures
    textures = glGenTextures(number)
    print textures
    CreateTexture("background.jpg", 0)

if __name__ == '__main__':
    obj = Backdrop()
    obj.main()
