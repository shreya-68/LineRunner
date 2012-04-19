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

from main import Robot 
from bg import *

VIEW_WIDTH = 900
VIEW_HEIGHT = 600

class Guy(object):
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.posz = 0
        self.rotz = 0
        self.left_shoulder = -90
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
        self.jump_state = 0
        self.height = 0

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

        #glMatrixMode(GL_MODELVIEW)
        glColor3f (1.0, 1.0, 1.0)
        #gluLookAt(0.0,0.0,8.0,0.0,0.0,0.0,0.0,1.0,0.0)

        glPushMatrix()
        glTranslatef(0.0, self.posy, self.posz)
        glTranslatef(0, 3, 0)
        glRotatef(self.rotz, 0.0,0.0,1.0)
        glRotatef(90, 0.0,1.0,0.0)
        glScalef(0.5,0.5,0.5);
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
        glPopMatrix();
#*********************************** 8 ---------- 12 ENDS **********************
        #glutSwapBuffers()
        #glMatrixMode(GL_PROJECTION)
        
        self.reshape(VIEW_WIDTH, VIEW_HEIGHT)
        #glFlush()

    def reshape(self, x, y):
        pass

    def check_loss(self, state):
        print 'posx = ' + str(self.posx) + 'posy = ' + str(self.posy)
        if (self.posx >= 9.0 and self.posx <= 10.4 and self.posy <= 0.3 and self.posy>= 0.0) or (self.posx >= 10.4 and self.posx <= 10.8 and self.posy <= 0.8 and self.posy>= 0.0):
            self.height = 60
            self.stand()
            while self.height != 0:
                state.update()
                pygame.time.wait(80)
                self.height = self.height - 1 
                self.posy = self.posy - 0.1
            state.loss = True
            return True
        return False
        

    def handle_keypress(self, event, x, y, state):
        key = event.key
        if key == K_RIGHT:
            #if self.jump_state == 0:
            self.front_right()
            state.update()
            pygame.time.wait(80)
            self.stand()
            if self.check_loss(state):
            	return True
            state.update()
            pygame.time.wait(80)
            self.front_left()
        elif key == K_LEFT:
            self.stand()
        elif key == K_UP:
            self.jump()
            if self.height > 40:
                while self.jump_state != 0:
                    self.fall()
                    if self.check_loss(state):
                    	return True
                    state.update()
                    pygame.time.wait(80)
                self.stand()
        elif key == K_DOWN:
            self.bend()
        #else:
        #    return False
        return self.check_loss(state)

    def handle_keyrelease(self, event, x, y, state):
        key = event.key
        if key in [K_RIGHT, K_LEFT]:
            self.stand()
        elif key == K_DOWN:
            self.stand()
            self.posy = 0.0 
        elif key == K_UP:
            while self.jump_state != 0:
                self.fall()
                if self.check_loss(state):
                	return True
                state.update()
                pygame.time.wait(80)
            self.stand()
        return self.check_loss(state)

    def front_left(self):
        self.rotz = 0
        self.posx = (self.posx + 0.3)%20.4
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
        self.rotz = 0
        self.posx = (self.posx + 0.3)%20.4
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
        if self.posy >= 3.0:
            self.posy = self.posy
        else:
            self.posy = self.posy + 0.1
            self.jump_state = self.jump_state + 1
        self.height = self.height + 1
        self.posx = (self.posx + 0.3)%20.4
        self.rotz = -20
        self.left_shoulder = -110
        self.left_elbow = 0
        self.right_shoulder = -110
        self.right_elbow = 0
        self.left_waist = 40
        self.left_knee = 0
        self.right_waist = 40
        self.right_knee = 0
        self.hips = 0
        self.neck = 0
        self.head = 0

    def bend(self):
        self.posy = -0.25 
        self.rotz = -20
        self.left_shoulder = -50
        self.left_elbow = -90
        self.right_shoulder = -50
        self.right_elbow = -90
        self.left_waist = -40
        self.left_knee = 50
        self.right_waist = -40
        self.right_knee = 50
        self.hips = 0
        self.neck = 0
        self.head = 0
        pass

    def fall(self):
        self.jump_state = self.jump_state - 1
        self.height = 0
        self.rotz = 20
        self.posx = (self.posx + 0.3)%20.4
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
        self.rotz = 0
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




