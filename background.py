from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
import pygame
import os
import sys
from pygame.locals import *

from camera import Camera

try:
    from PIL.Image import open
except ImportError, err:
    from Image import open

VIEW_WIDTH = 900
VIEW_HEIGHT = 600

class Background(object):

    def __init__(self):
        self.camera = Camera()

    def init(self):
        glClearColor(0.3,0.4,0.75,0.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        #pygame.init()
        #pygame.key.set_repeat(10,100)
        #pygame.display.set_mode((VIEW_WIDTH, VIEW_HEIGHT), OPENGLBLIT|DOUBLEBUF)
        ##pygame.display.set_mode((VIEW_WIDTH, VIEW_HEIGHT), 0, 32)
        #pygame.display.set_caption("Moving Bot")
    def LoadTextures(self, number):
        global textures
        textures = glGenTextures(number)
        print textures
        self.CreateTexture("ground.jpg", 0)
        self.CreateTexture("background.jpg", 1)
        self.CreateTexture("side.jpg", 2)
    
    def CreateTexture(self, imagename, number):
        global textures
        image = pygame.image.load(imagename)
        texture_data = pygame.image.tostring(image, 'RGBA', True)
        iw, ih = image.get_rect().size
        print iw
        print ih
        #ID = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, textures[number])
        glPixelStorei(GL_UNPACK_ALIGNMENT,1)
        glTexImage2D(
                GL_TEXTURE_2D, 0,3,iw,ih,0,GL_RGBA,GL_UNSIGNED_BYTE, texture_data)
        print 'Imageloaded'
        
    def setupTexture(self):
        print 'setuptexture'
        glEnable(GL_TEXTURE_2D)
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexEnvf(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_DECAL)
    
    def display(self):
        print 'display'
        #glClear(GL_COLOR_BUFFER_BIT)
        glDepthFunc(GL_LESS)

        #glMatrixMode(GL_PROJECTION)
        #glLoadIdentity()
        #gluPerspective(90.0, VIEW_WIDTH*1.0/VIEW_HEIGHT, 1.0, 15.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        #glMatrixMode(GL_TEXTURE)
        #glLoadIdentity()
    
        #glDisable(GL_LIGHTING)
        self.setupTexture()

        #glPushMatrix()
        #glTranslatef(0.0,-2.0,0.0);
        #self.drawDepth()
        #glPopMatrix()

        #glPushMatrix()
        #glTranslatef(0.0,-2.0,0.0);
        ##glScalef(2.0,2.0,2.0)
        #self.drawGround()
        #glPopMatrix()

        glPushMatrix()
        glTranslate(0.0,0.0,-6.0)
        glScalef(2.0,2.0,2.0)
        self.drawBackground()
        glPopMatrix()

        #glDisable(GL_TEXTURE_2D)
     #   glEnable(GL_BLEND)
     #   glDepthMask(GL_FALSE)
     #   glBlendFunc(GL_SRC_ALPHA, GL_ONE)
     #   glDepthMask(GL_TRUE)
     #   glDisable(GL_BLEND)
     #   glFlush()
        #glutSwapBuffers()
        #self.reshape(500, 500)

    def drawDepth(self):
        glBindTexture(GL_TEXTURE_2D, textures[2])
        glBegin(GL_QUADS);
        glTexCoord2f(0.0,1.0); glVertex3f(-10, 0, 3)
        glTexCoord2f(0.0,0.0); glVertex3f(-10,-4, 3)
        glTexCoord2f(1.0,0.0); glVertex3f( 10,-4, 3)
        glTexCoord2f(1.0,1.0); glVertex3f( 10, 0, 3) 
        glEnd()    
        glBegin(GL_QUADS);
        glTexCoord2f(0.0,1.0); glVertex3f(10, 0, 3)
        glTexCoord2f(0.0,0.0); glVertex3f(10,-4, 3)
        glTexCoord2f(1.0,0.0); glVertex3f(10,-4,-3)
        glTexCoord2f(1.0,1.0); glVertex3f(10, 0,-3) 
        glEnd()    
        glBegin(GL_QUADS);
        glTexCoord2f(0.0,1.0); glVertex3f( 10, 0,-3)
        glTexCoord2f(0.0,0.0); glVertex3f( 10,-4,-3)
        glTexCoord2f(1.0,0.0); glVertex3f(-10,-4,-3)
        glTexCoord2f(1.0,1.0); glVertex3f(-10, 0,-3) 
        glEnd()    
        glBegin(GL_QUADS);
        glTexCoord2f(0.0,1.0); glVertex3f(-10, 0,-3)
        glTexCoord2f(0.0,0.0); glVertex3f(-10,-4,-3)
        glTexCoord2f(1.0,0.0); glVertex3f(-10,-4, 3)
        glTexCoord2f(1.0,1.0); glVertex3f(-10, 0, 3) 
        glEnd()    

    def drawGround(self):
        glBindTexture(GL_TEXTURE_2D, textures[0])
        print 'draw ground'
        glBegin(GL_QUADS);
        glTexCoord2f(0.0,0.0); glVertex2f(-6, 0, 6)#glVertex2f(-9, 0, 2)
        glTexCoord2f(1.0,0.0); glVertex2f(-6, 0,-6)#glVertex2f(-9, 0,-2)
        glTexCoord2f(0.0,1.0); glVertex2f( 6, 0, 6)#glVertex2f( 9, 0, 2)
        glTexCoord2f(1.0,1.0); glVertex2f( 6, 0,-6)#glVertex2f( 9, 0,-2) 
        glEnd()    

    
    def drawBackground(self):
        glBindTexture(GL_TEXTURE_2D, textures[1])
        glBegin(GL_QUADS);
        glTexCoord2f(0.0,1.0); glVertex3f(-20, 22, 0)
        glTexCoord2f(0.0,0.0); glVertex3f(-20,-20, 0)
        glTexCoord2f(1.0,0.0); glVertex3f( 20,-20, 0)
        glTexCoord2f(1.0,1.0); glVertex3f( 20, 22, 0) 
        glEnd()    
    
    def reshape (self, w, h):
    
        glViewport (0, 0, w, h) 
    
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(90.0, w*1.0/h, 1.0, 15.0)
        gluLookAt(0.0,0.0,8.0,0.0,0.0,0.0,0.0,1.0,0.0)
        #glMatrixMode(GL_MODELVIEW)
        #glLoadIdentity()
    
            
    def handle_keypress(self, key, x, y):
        if key == GLUT_KEY_RIGHT:
            front_left()
        elif key == GLUT_KEY_LEFT:
            front_right()
        elif key == GLUT_KEY_UP:
            jump()
        elif key == GLUT_KEY_DOWN:
            bend()
        glutPostRedisplay()
    

    def main(self):
        self.LoadTextures(3)
        #glutInit(sys.argv)
        #glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
        #glutInitWindowSize(500,500)
        #glutInitWindowPosition(100,100)
        #glutCreateWindow('Glass')
        #self.init()
        #glutDisplayFunc(self.display)
        #glutReshapeFunc(self.reshape)
        ##glutKeyboardFunc(self.keyboard)
        ##glutSpecialFunc(self.handle_keypress)
        #glutMainLoop()

if __name__ == '__main__':
    obj = Background()
    obj.main()
