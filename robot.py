
#Shreya Agrawal 200901090
#!/usr/bin/python

# This is statement is required by the build system to query build info
if __name__ == '__build__':
    raise Exception

#  Robot.py

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
import pygame
import os
import sys
from pygame.locals import *

from background import Draw

class Robot(object):

    def __init__(self):
        print 'init'
        self.state_queue = [] 
        self.state_queue.append(State())
        self.last_state = None
        self.jump_state = 0
        #self.ground = Backdrop()

    def initGL(self):
        print 'initGL'
        glClearColor(0.0,0.0,0.0,0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LEQUAL)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

    def main(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(100,100)
        glutCreateWindow('Glass')
        self.initGL()
        glutDisplayFunc(self.display)
        glutReshapeFunc(self.reshape)
        glutKeyboardFunc(self.keyboard)
        glutSpecialFunc(self.handle_keypress)
        glutMainLoop()

if __name__ == '__main__':
    obj = Robot()
    obj.main()

global hips,t,left_shoulder,left_elbow,right_shoulder,right_elbow,left_waist,left_knee,right_waist,right_knee,neck,head,eyex,eyey,eyez, ball1, ball2, ball3, rotate, inc1, inc2, inc3, posx, posy, posz
posx = -8.5
posy = -1.0
posz = 0.0
rotate = 0
ball1 = 0
ball2 =270 
ball3 = 90
eyey = 0
eyex = 0 
eyez = 5
right = 0
left_shoulder = 0
left_elbow = 0
right_shoulder = 50
right_elbow = -90
left_waist = 0
left_knee = 0
right_waist = 0
right_knee = 0
#lh = 0
hips = 0
###t = 0
neck = 0
head = 0
inc1 = 0
inc2 = 0
inc3 = 0



def init(): 
   glClearColor (0.0, 0.0, 0.0, 0.0)
   glShadeModel (GL_FLAT)
   glClearDepth(1.0)
   glEnable(GL_DEPTH_TEST)
   glDepthFunc(GL_LEQUAL)
   glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)


def display():
        
        global eyex, eyey, eyez
        glClear (GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glColor3f (1.0, 1.0, 1.0)
        
       # glPushMatrix()
       # glTranslatef(0.0,2.0 + inc1 ,0.0)
       # glRotatef(ball1, 0.0,0.0,1.0)
       # glTranslatef(0.0,4.0 + inc1,0.0)
       # glRotatef(rotate, 0.0, 0.0, 1.0)
       # glScalef(0.2,0.2,0.2)
       # glColor3f(1.0,1.0,0.0)
       # glutSolidSphere(1.0,100,100)
       # glPopMatrix()

       # glPushMatrix()
       # glTranslatef(0.0,2.0 + inc2,0.0)
       # glRotatef(ball2, 0.0,0.0,1.0)
       # glTranslatef(0.0,4.0 + inc2,0.0)
       # glRotatef(rotate, 0.0, 0.0, 1.0)
       # glScalef(0.2,0.2,0.2)
       # glColor3f(0.0,1.0,1.0)
       # glutSolidSphere(1.0,100,100)
       # glPopMatrix()
       # 
       # glPushMatrix()
       # glTranslatef(0.0,2.0 + inc3,0.0)
       # glRotatef(ball3, 0.0,0.0,1.0)
       # glTranslatef(0.0,4.0 + inc3,0.0)
       # glRotatef(rotate, 0.0, 0.0, 1.0)
       # glScalef(0.2,0.2,0.2)
       # glColor3f(1.0,0.0,1.0)
       # glutSolidSphere(1.0,100,100)
       # glPopMatrix()

        glTranslatef(posx, posy, posz)
        glRotatef(110, 0.0,1.0,0.0)
        glScalef(0.7,0.7,0.7);
        glPushMatrix()

        glPushMatrix();
        glScalef(0.5,4.0,0.5);
        glColor3f(1.0,0.0,0.0)
        glutSolidCube(1.0);
        glPopMatrix();
#************************************ 1----7 ******************
        glPushMatrix(); 
        
        glTranslatef(0.0,2.0,0.0);
# 7#### shoulder
        glPushMatrix();
        glScalef(3.0,0.5,0.5);
        
        glColor3f(1.0,1.0,0.0)
        glutSolidCube(1.0);
        glPopMatrix();
# 7 ends# 7 ends# 7 ends
 # 1_2
        glPushMatrix();
        glTranslatef (1.3, 0.0, 0.0);
        glRotatef (left_shoulder, 1.0, 0.0, 0.0);
        glTranslatef (0.0, -1.0, 0.0);
        
        glPushMatrix();
        glScalef (0.5,2.0,0.5);
        
        glColor3f(1.0,0.0,1.0)
        glutSolidCube (1.0);
        glPopMatrix();

        glTranslatef (0.0, -1.0, 0.0);
        glRotatef (left_elbow, 1.0, 0.0, 0.0);
        glTranslatef (0.0, -1.0, 0.0);

        glPushMatrix();
        glScalef (0.5, 2.0, 0.5);
        glColor3f(0.0,1.0,0.0)
        glutSolidCube (1.0);
        glPopMatrix();
        glPopMatrix();
# 1_2 ends

# 3_4
        glPushMatrix();

        glTranslatef (-1.3, 0.0, 0.0);
        glRotatef (right_shoulder, 1.0, 0.0, 0.0);
        glTranslatef (0.0, -1.0, 0.0);

        glPushMatrix();
        glScalef (0.5,2.0,0.5);
        glColor3f(0.0,1.0,1.0)
        glutSolidCube (1.0);
        glPopMatrix();

        glTranslatef (0.0, -1.0, 0.0);
        glRotatef (right_elbow, 1.0, 0.0, 0.0);
        glTranslatef (0.0, -1.0, 0.0);

        glPushMatrix();
        glScalef (0.5,2.0,0.5);
        glColor3f(0.0,0.0,1.0)
        glutSolidCube (1.0);
        glPopMatrix();
       
        glPopMatrix();
        
 #3_4 ends

 #5_6
        glPushMatrix();
       
        glTranslatef(0.0,0.25,0.0);
        glRotatef(neck,0.0,0.0,1.0);
        glTranslatef(0.0,0.5,0.0);        
#neck        
        glPushMatrix();
       # glTranslatef (0.0,3.0, 0.0);
        glScalef (0.5, 1.0, 0.5);
        glColor3f(1.0,0.0,1.0)
        glutSolidCube (1.0);
        glPopMatrix();
        
        glTranslatef(0.0,0.5,0.0)
        glRotatef(head,0.0,0.0,1.0)
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
        
        glRotatef(hips,0.0,0.0,1.0);
        glTranslatef(0.0,-2.0,0.0);
      
        glPushMatrix();
        glScalef(2.0,0.5,0.5);
        glColor3f(0.2,0.2,0.2)
        glutSolidCube(1.0);
        glPopMatrix();
      # 10 _ 11  
        glPushMatrix(); 
        
        glTranslate(1.0,0.0,0.0);
        glRotatef(left_waist,1.0,0.0,0.0);
        glTranslatef(0.0,-1.0,0.0);
        
        glPushMatrix();
        glScalef(0.5,2.0,0.5);
        glColor3f(0.5,0.5,0.5)
        glutSolidCube(1.0);
        glPopMatrix();
        
        glTranslatef(0.0,-1.0,0.0);
        glRotatef(left_knee,1.0,0.0,0.0);
        glTranslatef(0.0,-1.0,0.0);

        glPushMatrix();
        glScalef(0.5,2.0,0.5);
        glColor3f(0.2,0.2,0.0)
        glutSolidCube(1.0);
        glPopMatrix();

        glPopMatrix();
      # 10 _ 11 ends 
        
# 8_9
        glPushMatrix();
#right leg       
        glTranslate(-1.0,0.0,0.0);
        glRotatef(right_waist,1.0,0.0,0.0);
        glTranslatef(0.0,-1.0,0.0);
        
        glPushMatrix();
        glScalef(0.5,2.0,0.5);
        glColor3f(0.0,0.5,0.5)
        glutSolidCube(1.0);
        glPopMatrix();
        
        glTranslatef(0.0,-1.0,0.0);
        glRotatef(right_knee,1.0,0.0,0.0);
        glTranslatef(0.0,-1.0,0.0);

        glPushMatrix();
        glScalef(0.5,2.0,0.5);
        glColor3f(0.5,0.5,0.0)
        glutSolidCube(1.0);
        glPopMatrix();
#right leg ends
        glPopMatrix();
# 8_9 ends
       
        glPopMatrix();
        glPopMatrix();
#*********************************** 8 ---------- 12 ENDS **********************
        glutSwapBuffers();
        #juggle()
        reshape(1200,600)
        return 

def reshape (w, h):

        glViewport (0, 0, w, h) 

        glMatrixMode (GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(65.0, w/h, 1.0, 15.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef (0.0, 0.0,-5.0)
        
       # gluLookAt(eyex,eyey,eyez,0.0,0.0,0.0,0.0,1.0,0.0)
        gluLookAt(0.0,0.0,5.0,0.0,0.0,0.0,0.0,1.0,0.0)
        return 1

def front():
    global hips,t,left_shoulder,left_elbow,right_shoulder,right_elbow,left_waist,left_knee,right_waist,right_knee,neck,head,eyex,eyey,eyez, ball1, ball2, ball3, rotate, inc1, inc2, inc3, posx, posy, posz
    posx = posx + 1.0
#    left_waist = (time
    return 1

def jump():
    global posy
    posy = posy + 1.0
    return 1

           
def juggle():
    global left_shoulder,left_elbow,right_shoulder,right_elbow,left_waist,left_knee,right_waist,right_knee, hips,t,neck,head,eyex,eyey,eyez
    global ball1, ball2, ball3, rotate
    ball1 = time.time()%4/4*360
    ball2 = time.time()%5/5*360
    ball3 = time.time()%3/3*360
    if ball1 >= 90 and ball1 <=270:
        inc1 = 2
    else:
        inc1 = 0
    if ball2 >= 90 and ball2 <=270:
        inc2 = 2
    else:
        inc2 = 0
    if ball3 >= 90 and ball3 <=270:
        inc3 = 2
    else:
        inc3 = 0
    left_waist = (time.time()%6/6*360)%90 + 270
    right_waist = (time.time()%6/6*360)%90 + 270
    left_knee = (time.time()%6/6*360)%90 
    right_knee = (time.time()%6/6*360)%90 + 90
    if left_shoulder == -50:
        left_shoulder = left_shoulder + 10
    else:
        left_shoulder = left_shoulder - 10
    if right_shoulder == 50:
        right_shoulder = right_shoulder + 10
    else:
        right_shoulder = right_shoulder - 10

    rotate = rotate + 1
    glutPostRedisplay()
    return 1
        
def front_left():
    global left_shoulder,left_elbow,right_shoulder,right_elbow,left_waist,left_knee,right_waist,right_knee, hips,t,neck,head,eyex,eyey,eyez, posx, posy, posz
    
    left_shoulder = -50
    left_elbow = -90
    right_shoulder = 50
    right_elbow = -90
    left_waist = 30
    left_knee = 20
    right_waist = -30
    right_knee = 20
    posx = posx + 0.1
    glutPostRedisplay()

def front_right():
    global left_shoulder,left_elbow,right_shoulder,right_elbow,left_waist,left_knee,right_waist,right_knee, hips,t,neck,head,eyex,eyey,eyez, posx, posy, posz
    
    right_shoulder = -50
    right_elbow = -90
    right_waist = 30
    right_knee = 20
    left_shoulder = 50
    left_elbow = -90
    left_waist = -30
    left_knee = 20
    posx = posx + 0.1
    glutPostRedisplay()

def jump():
    global left_shoulder,left_elbow,right_shoulder,right_elbow,left_waist,left_knee,right_waist,right_knee, hips,t,neck,head,eyex,eyey,eyez, posx, posy, posz
    right_shoulder = -50
    right_elbow = -90
    right_waist = -30
    right_knee = 20
    left_shoulder = -50
    left_elbow = -90
    left_waist = -30
    left_knee = 20
    posy = posy + 0.1
    glutPostRedisplay()

def bend():
    global left_shoulder,left_elbow,right_shoulder,right_elbow,left_waist,left_knee,right_waist,right_knee, hips,t,neck,head,eyex,eyey,eyez, posx, posy, posz
    right_shoulder = -50
    right_elbow = -90
    right_waist = -30
    right_knee = 40
    left_shoulder = -50
    left_elbow = -90
    left_waist = -30
    left_knee = 40
    posy = posy - 0.1
    glutPostRedisplay()

def specialKeys(key, x, y):
    if key == GLUT_KEY_RIGHT:
        front_left()
    elif key == GLUT_KEY_LEFT:
        front_right()
    elif key == GLUT_KEY_UP:
        jump()
    elif key == GLUT_KEY_DOWN:
        bend()
    glutPostRedisplay()

def keyboard(key, x, y):
    global left_shoulder,left_elbow,right_shoulder,right_elbow,left_waist,left_knee,right_waist,right_knee, hips,t,neck,head,eyex,eyey,eyez
         
    if key == chr(27): sys.exit(0)
    elif key == 's':
            left_shoulder = (left_shoulder + 5) % 360
            glutPostRedisplay()
    elif key == 'S':
            left_shoulder = (left_shoulder - 5) % 360
            glutPostRedisplay()
    elif key == 'a':
            right_shoulder = (right_shoulder + 5) % 360
            glutPostRedisplay()
    elif key == 'A':
            right_shoulder = (right_shoulder - 5) % 360
            glutPostRedisplay()
    elif key == 'r':
            left_elbow = (left_elbow + 5) % 360
            glutPostRedisplay()
    elif key == 'R':
            left_elbow = (left_elbow - 5) % 360
            glutPostRedisplay()
    elif key == 'e':
            right_elbow = (right_elbow + 5) % 360
            glutPostRedisplay()
    elif key == 'E':
            right_elbow = (right_elbow - 5) % 360
            glutPostRedisplay()
    elif key == 'q':
            left_waist = (left_waist + 5) % 360
            glutPostRedisplay()
    elif key == 'Q':
            left_waist = (left_waist - 5) % 360
            glutPostRedisplay()
    elif key == 'w':
            right_waist = (right_waist + 5) % 360
            glutPostRedisplay()
    elif key == 'W':
            right_waist = (right_waist - 5) % 360
            glutPostRedisplay()
    elif key == 'x':
            left_knee = (left_knee + 5) % 360
            glutPostRedisplay()
    elif key == 'X':
            left_knee = (left_knee - 5) % 360
            glutPostRedisplay()
    elif key == 'z':
            right_knee = (right_knee - 5) % 360
            glutPostRedisplay()
    elif key == 'Z':
            right_knee = (right_knee + 5) % 360
            glutPostRedisplay()
    elif key == 'c':
            hips = (hips - 5) % 360
            hips = (hips + 5) % 360
            glutPostRedisplay()
   # elif key == 't':
   #          t = (t - 5) % 360
   #          glutPostRedisplay()
    elif key == 'v':
            neck = (neck + 5) % 360
            glutPostRedisplay()
    elif key == 'V':
            neck = (neck - 5) % 360
            glutPostRedisplay()
    elif key == 'H':
            head = (head - 5) % 360
            glutPostRedisplay()
    elif key == 'k':
            eyey = eyey + 0.1  
            glutPostRedisplay()
    elif key == 'j':
            eyey = eyey - 0.1  
            glutPostRedisplay()
    elif key == 'l':
            eyex = eyex + 0.1  
            glutPostRedisplay()
    elif key == 'h':
            eyex = eyex - 0.1  
            glutPostRedisplay()

glutInit(sys.argv)
glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize (1200, 600)
glutInitWindowPosition (100, 100)
glutCreateWindow ('HUMAN')
init ()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutSpecialFunc(specialKeys)
glutMainLoop()
