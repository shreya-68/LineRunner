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

VIEW_WIDTH = 900
VIEW_HEIGHT = 600

class State(object):
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.posz = 0
        self.left_shoulder = 0
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

    def drawCube(self, size):
        size = size/2
        glBegin(GL_QUADS);
        glVertex3f( size, size,-size)
        glVertex3f(-size, size,-size)
        glVertex3f(-size, size, size)
        glVertex3f( size, size, size)
        glVertex3f( size,-size, size)
        glVertex3f(-size,-size, size)
        glVertex3f(-size,-size,-size)
        glVertex3f( size,-size,-size)
        glVertex3f( size, size, size)
        glVertex3f(-size, size, size)
        glVertex3f(-size,-size, size)
        glVertex3f( size,-size, size)
        glVertex3f( size,-size,-size)
        glVertex3f(-size,-size,-size)
        glVertex3f(-size, size,-size)
        glVertex3f( size, size,-size)
        glVertex3f(-size, size, size)
        glVertex3f(-size, size,-size)
        glVertex3f(-size,-size,-size)
        glVertex3f(-size,-size, size)
        glEnd()    

    def display(self):
        print 'state display'

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(90, VIEW_WIDTH*1.0/VIEW_HEIGHT, 1.0, 15.0)

        glClearDepth(1.0)
        glDepthFunc(GL_LEQUAL)

        glClear (GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #glMatrixMode(GL_MODELVIEW)
        glColor3f (1.0, 1.0, 1.0)
        gluLookAt(0.0,0.0,8.0,0.0,0.0,0.0,0.0,1.0,0.0)

        glTranslatef(self.posx, self.posy, self.posz)
        glTranslatef(1, 1, 1)
        glRotatef(70, 0.0,1.0,0.0)
        glScalef(0.7,0.7,0.7);
        #glPushMatrix()

        glPushMatrix();
        glScalef(0.5,4.0,0.5);
        glColor3f(1.0,0.0,0.0)
        self.drawCube(1.0);
        glPopMatrix();
#************************************ 1----7 ******************
        glPushMatrix(); 
        
        glTranslatef(0.0,2.0,0.0);
# 7#### shoulder
        glPushMatrix();
        glScalef(3.0,0.5,0.5);
        
        glColor3f(1.0,1.0,0.0)
        self.drawCube(1.0);
        glPopMatrix();
# 7 ends# 7 ends# 7 ends
 # 1_2
        glPushMatrix();
        glTranslatef (1.3, 0.0, 0.0);
        glRotatef (self.left_shoulder, 1.0, 0.0, 0.0);
        glTranslatef (0.0, -1.0, 0.0);
        
        glPushMatrix();
        glScalef (0.5,2.0,0.5);
        glColor3f(1.0,0.0,1.0)
        self.drawCube(1.0);
        glPopMatrix();

        glTranslatef (0.0, -1.0, 0.0);
        glRotatef (self.left_elbow, 1.0, 0.0, 0.0);
        glTranslatef (0.0, -1.0, 0.0);

        glPushMatrix();
        glScalef (0.5, 2.0, 0.5);
        glColor3f(0.0,1.0,0.0)
        self.drawCube(1.0);
        glPopMatrix();
        glPopMatrix();
# 1_2 ends

# 3_4
        glPushMatrix();

        glTranslatef (-1.3, 0.0, 0.0);
        glRotatef (self.right_shoulder, 1.0, 0.0, 0.0);
        glTranslatef (0.0, -1.0, 0.0);

        glPushMatrix();
        glScalef (0.5,2.0,0.5);
        glColor3f(0.0,1.0,1.0)
        self.drawCube (1.0);
        glPopMatrix();

        glTranslatef (0.0, -1.0, 0.0);
        glRotatef (self.right_elbow, 1.0, 0.0, 0.0);
        glTranslatef (0.0, -1.0, 0.0);

        glPushMatrix();
        glScalef (0.5,2.0,0.5);
        glColor3f(0.0,0.0,1.0)
        self.drawCube (1.0);
        glPopMatrix();
       
        glPopMatrix();
        
 #3_4 ends

 #5_6
        glPushMatrix();
       
        glTranslatef(0.0,0.25,0.0);
        glRotatef(self.neck,0.0,0.0,1.0);
        glTranslatef(0.0,0.5,0.0);        
#neck        
        glPushMatrix();
        glScalef (0.5, 1.0, 0.5);
        glColor3f(1.0,0.0,1.0)
        self.drawCube (1.0);
        glPopMatrix();
        
        glTranslatef(0.0,0.5,0.0)
        glRotatef(self.head,0.0,0.0,1.0)
        glTranslatef(0.0,0.5,0.0)
#head
        glPushMatrix();
        glScalef (1.0, 1.0, 1.0);
        glColor3f(0.0,1.0,1.0)
        glutSolidSphere (1.0,100,100);
        glPopMatrix();

        glPopMatrix();
# 5_6 ends

        glPopMatrix();
#************************************* 1-------7 ENDS *************************

#************************************ 8 ---------12 BEGINS *******************
        glPushMatrix();
     
        glTranslatef(0.0,0.0,0.0);
        
        glRotatef(self.hips,0.0,0.0,1.0);
        glTranslatef(0.0,-2.0,0.0);
      
        glPushMatrix();
        glScalef(2.0,0.5,0.5);
        glColor3f(0.2,0.2,0.2)
        self.drawCube(1.0);
        glPopMatrix();
      # 10 _ 11  
        glPushMatrix(); 
        
        glTranslate(1.0,0.0,0.0);
        glRotatef(self.left_waist,1.0,0.0,0.0);
        glTranslatef(0.0,-1.0,0.0);
        
        glPushMatrix();
        glScalef(0.5,2.0,0.5);
        glColor3f(0.5,0.5,0.5)
        self.drawCube(1.0);
        glPopMatrix();
        
        glTranslatef(0.0,-1.0,0.0);
        glRotatef(self.left_knee,1.0,0.0,0.0);
        glTranslatef(0.0,-1.0,0.0);

        glPushMatrix();
        glScalef(0.5,2.0,0.5);
        glColor3f(0.2,0.2,0.0)
        self.drawCube(1.0);
        glPopMatrix();

        glPopMatrix();
      # 10 _ 11 ends 
        
# 8_9
        glPushMatrix();
#right leg       
        glTranslate(-1.0,0.0,0.0);
        glRotatef(self.right_waist,1.0,0.0,0.0);
        glTranslatef(0.0,-1.0,0.0);
        
        glPushMatrix();
        glScalef(0.5,2.0,0.5);
        glColor3f(0.0,0.5,0.5)
        self.drawCube(1.0);
        glPopMatrix();
        
        glTranslatef(0.0,-1.0,0.0);
        glRotatef(self.right_knee,1.0,0.0,0.0);
        glTranslatef(0.0,-1.0,0.0);

        glPushMatrix();
        glScalef(0.5,2.0,0.5);
        glColor3f(0.5,0.5,0.0)
        self.drawCube(1.0);
        glPopMatrix();
#right leg ends
        glPopMatrix();
# 8_9 ends
       
        glPopMatrix();
       # glPopMatrix();
#*********************************** 8 ---------- 12 ENDS **********************
        #glutSwapBuffers()
        #glMatrixMode(GL_PROJECTION)
        
        self.reshape(VIEW_WIDTH, VIEW_HEIGHT)
        #glFlush()


    def reshape(self, w, h):
        print 'state.reshape'

        glViewport (0, 0, w, h) 

        glMatrixMode (GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(90.0, w*1.0/h, 1.0, 15.0)

        #glMatrixMode(GL_MODELVIEW)
        #glLoadIdentity()
        #glTranslatef (0.0, 0.0,0.0)
       # 
       ## gluLookAt(eyex,eyey,eyez,0.0,0.0,0.0,0.0,1.0,0.0)
        gluLookAt(0.0,0.0,8.0,0.0,0.0,0.0,0.0,1.0,0.0)

    def front_left(self):
        self.posx = self.posx + 0.1
        self.left_shoulder = -50
        self.left_elbow = -90
        self.right_shoulder = 50
        self.right_elbow = -90
        self.left_waist = 30
        self.left_knee = 20
        self.right_waist = -30
        self.right_knee = 20
        self.hips = 0
        self.neck = 0
        self.head = 0

    def front_right(self):
        self.posx = self.posx + 0.1
        self.left_shoulder = 50
        self.left_elbow = -90
        self.right_shoulder = -50
        self.right_elbow = -90
        self.left_waist = -30
        self.left_knee = 20
        self.right_waist = 30
        self.right_knee = 20
        self.hips = 0
        self.neck = 0
        self.head = 0

    def jump(self):
        self.posy = self.posy + 0.1
        self.left_shoulder = -50
        self.left_elbow = -90
        self.right_shoulder = -50
        self.right_elbow = -90
        self.left_waist = -30
        self.left_knee = -20
        self.right_waist = -30
        self.right_knee = 20
        self.hips = 0
        self.neck = 0
        self.head = 0

    def bend(self):
        pass

    def fall(self):
        self.posy = self.posy - 0.1
        self.left_shoulder = -50
        self.left_elbow = -90
        self.right_shoulder = -50
        self.right_elbow = -90
        self.left_waist = 0
        self.left_knee = 0
        self.right_waist = 0
        self.right_knee = 0
        self.hips = 0
        self.neck = 0
        self.head = 0

    def stand(self):
        self.left_shoulder = 0
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

    def straight(self):
        pass




