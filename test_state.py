import os
import sys
import math
import time
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from collections import deque

VIEW_WIDTH = 800
VIEW_HEIGHT = 800

class State(object):
    def __init__(self):
        self.posx = -5.5
        self.posy = -1.0
        self.posz = 0.0
        self.left_shoulder = 00
        self.left_elbow = 0
        self.right_shoulder = 0
        self.right_elbow = 0
        self.left_waist = 0
        self.left_knee = 0
        self.right_waist = 0
        self.right_knee = 0
        self.hips = 0
        self.neck = 0
        self.head = 0

    def display(self):
        print 'state display'

        glClear (GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #glMatrixMode(GL_MODELVIEW)
        glColor3f (0.0, 1.0, 1.0)
        gluLookAt(0.0,0.0,6.0,0.0,0.0,0.0,0.0,1.0,0.0)
        glPushMatrix();
        glScalef (0.5, 2.0, 0.5);
        glColor3f(1.0,1.0,1.0)
        glutSolidCube (1.0);
        glPopMatrix();

        glBegin(GL_LINES)
        glVertex3f(0.0,0.0,0.0)
        glVertex3f(6.0,0.0,0.0)
        glEnd()

        glRotatef(90, 1.0, 0.0, 0.0);
        #glTranslatef(0.0,0.0,5.0)

        glPushMatrix();
        glScalef (0.5, 2.0, 0.5);
        glColor3f(0.0,1.0,0.0)
        glutSolidCube (1.0);
        glPopMatrix();
        #glRotatef(-90, 0.0, 1.0, 0.0)
        self.reshape(VIEW_WIDTH, VIEW_HEIGHT)
        #glFlush()


    def reshape(self, w, h):
        print 'state.reshape'

        glViewport (0, 0, w, h) 

        glMatrixMode (GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(90.0, w*1.0/h, 1.0, 15.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        #glTranslatef (0.0, 0.0,-5.0)
        
       # gluLookAt(eyex,eyey,eyez,0.0,0.0,0.0,0.0,1.0,0.0)
        gluLookAt(0.0,0.0,8.0,0.0,0.0,0.0,0.0,1.0,0.0)

    def front_left(self):
        self.posx = -8.5
        self.posy = -1.0
        self.posz = 0.0
        self.left_shoulder = 0
        self.left_elbow = 90
        self.right_shoulder = 0
        self.right_elbow = 0
        self.left_waist = 0
        self.left_knee = 0
        self.right_waist = 0
        self.right_knee = 0
        self.hips = 0
        self.neck = 0
        self.head = 0
        pass

    def front_right(self):
        pass

    def jump(self):
        pass

    def bend(self):
        pass

    def fall(self):
        pass

    def stand(self):
        pass

    def straight(self):
        pass




