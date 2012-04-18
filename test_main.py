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

from test_state import State

VIEW_WIDTH = 800
VIEW_HEIGHT = 800

class Robot(object):

    def __init__(self):
        print 'init'
        self.state_queue = [] 
        self.state_queue.append(State())
        self.last_state = None
        self.jump_state = 0
        print self.state_queue[0].posx
        pygame.init()
        pygame.key.set_repeat(10,100)
        pygame.display.set_mode((VIEW_WIDTH, VIEW_HEIGHT), OPENGLBLIT|DOUBLEBUF)
        #pygame.display.set_mode((VIEW_WIDTH, VIEW_HEIGHT), 0, 32)
        pygame.display.set_caption("Moving Bot")
        self.initGL()

    def initGL(self):
        print 'initGL'
        glutInit(sys.argv)
        glClearColor(0.0,0.0,0.0,0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LEQUAL)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
        
        self.reshape(VIEW_WIDTH, VIEW_HEIGHT)
        pygame.display.flip()

    def reshape(self, w, h):
        print 'Robot.reshape'
        glViewport(0, 0, w, h)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(65, w*1.0/h, 1.0, 15.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        #glTranslatef(0.0, 0.0, -5.0)

        gluLookAt(0.0, 0.0, 6.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    def display(self):
        #for state in self.state_queue:
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(65, VIEW_WIDTH*1.0/VIEW_HEIGHT, 1.0, 15.0)

        last_state = self.last_state

        while self.state_queue != []:
            self.state_queue[0].display()
            last_state = self.state_queue.pop(0)

        self.last_state = last_state

        pygame.display.flip()

    def handle_keypress(self, event):
        key = event.key
        if self.state_queue == []:
            new_state = self.last_state
        else:
            new_state = self.state_queue[-1]

        if key == K_RIGHT:
            new_state.front_left()
            self.state_queue.append(new_state)
            new_state.front_right()
            self.state_queue.append(new_state)
        elif key == K_UP:
            new_state.jump()
            self.state_queue.append(new_state)
            self.jump_state = self.jump_state + 1
        elif key == K_DOWN:
            new_state.bend()
            self.state_queue.append(new_state)
        else:
            return False
        return True

    def handle_keyrelease(self, event):
        key = event.key
        if self.state_queue == []:
            new_state = self.last_state
        else:
            new_state = self.state_queue[-1]

        if key == K_RIGHT:
            new_state.stand()
            self.state_queue.append(new_state)
        elif key == K_UP:
            while self.jump_state != 0:
                new_state.fall()
                self.state_queue.append(new_state)
                self.jump_state = self.jump_state - 1
        elif key == K_DOWN:
            new_state.straight()
            self.state_queue.append(new_state)
        else:
            return False
        return True
        



    def main(self):
        self.display()
        print 'update'
        #pygame.display.update()
        
        while True:
            for event in pygame.event.get():
                print event.type
                if event.type == QUIT:
                    sys.exit(0)
                elif event.type == KEYDOWN:
                    self.handle_keypress(event)
                elif event.type == KEYUP:
                    self.handle_keyrelease(event)

            self.display()
            pygame.time.wait(10)
# handle keypresses
        
        
if __name__ == '__main__':
    obj = Robot()
    obj.main()


