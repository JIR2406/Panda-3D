import pygame as py
from OpenGL.GLU import *
from OpenGL.GL import * 
from OpenGL.GLUT import *

def texto(text, posx, posy, posz, sizeFont, R, G, B, RB, GB, BB):
    font = py.font.Font(None, sizeFont)
    text_surface = font.render(text, True, (R, G, B), (RB, GB, BB))
    text_data = py.image.tostring(text_surface, "RGBA", True)
    glRasterPos3d(posx, posy, posz)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)
