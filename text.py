import pygame
from OpenGL.GL import *

class Text(object):
    def __init__(self, size, color=(0, 0, 0), bg=(255, 255, 255), font_name=pygame.font.get_default_font()):
        self.color = color
        self.bg = bg
        self.font = pygame.font.Font(font_name, size)
        self.pixmaps = []
        self.line_height = self.font.get_linesize()

    def display(self, text, x, y, size):
        self.pixmaps = []
        font_name=pygame.font.get_default_font()
        self.font = pygame.font.Font(font_name, size)
        for line in text.split('\n'):
        	surf = self.font.render(line, True, self.color, self.bg)
        	self.pixmaps.append((pygame.image.tostring(surf, 'RGBA', 1), surf.get_width(), surf.get_height()))
        	self.render(x, y)

    def render(self, x, y):
        glPushMatrix()
        for pixmap, w, h in self.pixmaps:
            glRasterPos2i(x, y)
            y += self.line_height
            glDrawPixels(w, h, GL_RGBA, GL_UNSIGNED_BYTE, pixmap)
        glPopMatrix()
