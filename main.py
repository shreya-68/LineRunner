import os
import sys
import math
import time
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from bg import *

VIEW_WIDTH, VIEW_HEIGHT = 900, 600

class Camera(object):
    def __init__(self, start_pos):
        self.pos = start_pos
        self.angle = 40
        self.pitch = 0
        self.mouse_prev = pygame.mouse.get_pos()

    def handle_keypress(self, event, x, y):
        if event.mod: return False
        key = event.key
        facing = (math.sin(math.radians(self.angle)),
                  0, #math.sin(math.radians(self.pitch)),
                  -math.cos(math.radians(self.angle)))

        facing_perp_x = (math.sin(math.radians(self.angle+90)),
                         0, #math.sin(math.radians(self.pitch)),
                         -math.cos(math.radians(self.angle+90)))
        if key == K_UP or key == K_w:
            self.pos = (self.pos[0] + facing[0], self.pos[1] + facing[1], self.pos[2] + facing[2])
        elif key == K_DOWN or key == K_s:
            self.pos = (self.pos[0] - facing[0], self.pos[1] - facing[1], self.pos[2] - facing[2])
        elif key == K_LEFT or key == K_a:
            self.pos = (self.pos[0] - facing_perp_x[0], self.pos[1] - facing_perp_x[1], self.pos[2] - facing_perp_x[2])
        elif key == K_RIGHT or key == K_d:
            self.pos = (self.pos[0] + facing_perp_x[0], self.pos[1] + facing_perp_x[1], self.pos[2] + facing_perp_x[2])
        else:
            return False

        return True

    def handle_mouse(self, button, state, x, y):
        pass

    def handle_motion(self, x, y):
        d_x = x-self.mouse_prev[0]
        d_y = y-self.mouse_prev[1]

        if abs(d_x) > abs(d_y):
            if d_x < 0:
                self.angle -= 5
            else:
                self.angle += 5
        else:
            if d_y < 0:
                self.pitch += 5
                if self.pitch > 80:
                    self.pitch = 80
            else:
                self.pitch -= 5
                if self.pitch < 0:
                    self.pitch = 0

        self.angle %= (360 * (self.angle < 0 and -1 or 1))
        self.pitch %= (360 * (self.pitch < 0 and -1 or 1))

        self.mouse_prev = (x, y)

    def glulookat_coordinates(self):
        pass

    def apply_transforms(self):
        gluLookAt(0.0,2,10,0.0,0.0,0.0,0.0,1.0,0.0)
        #glRotatef(-self.pitch, 1, 0, 0)
        #glRotatef(self.angle, 0, 1, 0)
        #glTranslatef(0, -5, -8)

class Robot(object):
    state = property(lambda self: self.state_stack[-1])
    def __init__(self):
        self.state_stack = []
        self.loss = False

        pygame.init()
        pygame.key.set_repeat(10, 100)
        pygame.display.set_mode((VIEW_WIDTH, VIEW_HEIGHT), OPENGLBLIT|DOUBLEBUF)
        pygame.display.set_caption("Robot")
        self.initGL()

        self.camera = Camera((4, 1.2, 5))

    def milliseconds(self):
        return int(time.time() * 1000)

    def initGL(self):
        glutInit(sys.argv)
        glClearColor(0, 0, 0, 0)

        glClearDepth(1.0)
        glDepthFunc(GL_LEQUAL)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)

        #glEnable(GL_LIGHTING)

        self.reshape(VIEW_WIDTH, VIEW_HEIGHT)
        pygame.display.flip()

    def update(self):
        #print self.state
        self.time_curr = self.milliseconds()
        frame_time = self.time_curr - self.time_prev
        if frame_time > 25:
            frame_time = 25
        self.accumulator += frame_time

        if self.accumulator > 10:
            self.reshape(VIEW_WIDTH, VIEW_HEIGHT)
            #self.state.update(self, frame_time)
            self.display()

        self.time_prev = self.time_curr

    def reset_camera(self):
        self.camera.pos = (4, 1.2, 5)
        self.camera.angle = 40

    def pop_state(self):
        if len(self.state_stack) > 0:
            self.state_stack.pop()
            return True
        return False

    def push_state(self, next):
        self.state_stack.append(next)

    def switch_state(self, next):
        self.pop_state()
        self.push_state(next)

    def display(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(90, VIEW_WIDTH*1.0/VIEW_HEIGHT, 1.0, 20.0)
        #gluLookAt(*self.camera.glulookat_coordinates())
        self.camera.apply_transforms()

        glMatrixMode(GL_MODELVIEW)
        glClear(GL_DEPTH_BUFFER_BIT|GL_COLOR_BUFFER_BIT)
        self.state.display()
        pygame.display.flip()

    def reshape(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(90, w*1.0/h, 1.0, 20.0)
        glTranslatef(4, -VIEW_HEIGHT, 5)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def handle_keypress(self, event, x, y):
        self.state.handle_keypress(event, x, y, self)
        return
        if self.camera.handle_keypress(event, x, y): return

    def handle_keyrelease(self, event, x, y):
        self.state.handle_keyrelease(event, x, y, self)
        return
        #if self.camera.handle_keypress(event, x, y): return
        # do any remaining handling here

    def handle_mouse(self, button, state, x, y):
        if self.state.handle_mouse(button, state, x, y): return
        if self.camera.handle_mouse(button, state, x, y): return

        # do any remaining handling here

    def run(self):
        self.push_state(World())
        self.time_prev = self.time_curr = self.milliseconds()
        self.accumulator = 0

        while True:
            for event in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE): sys.exit(0)
                elif event.type == KEYDOWN:
                    print event.type
                    self.handle_keypress(event, mouse[0], mouse[1])
                elif event.type == KEYUP:
                    self.handle_keyrelease(event, mouse[0], mouse[1])
                #elif event.type == MOUSEBUTTONDOWN:
                #    self.handle_mouse(event.button, event.type, event.pos[0], event.pos[1])
                #elif event.type == MOUSEMOTION:
                #    self.camera.handle_motion(event.pos[0], event.pos[1])

            self.update()
            pygame.time.wait(10)
            if self.loss == True:
            	break;

        while True:
            for event in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                	sys.exit(0)
            self.update()
            pygame.time.wait(10)


if __name__ == '__main__':
    f = Robot()
    f.run()
