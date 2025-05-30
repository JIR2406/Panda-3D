import pygame as py
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image

class Escenario:
    texture_ids = {}  # Diccionario para almacenar los IDs de textura

    def __init__(self):
        pass

    @classmethod
    def load_texture(cls, filename):
        with Image.open(filename) as im:
            ix, iy, image = im.size[0], im.size[1], im.tobytes("raw", "RGBX", 0, -1)

        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

        return texture_id

    @classmethod
    def get_texture_id(cls, filename):
        if filename not in cls.texture_ids:  # Verificar si la textura ya ha sido cargada
            cls.texture_ids[filename] = cls.load_texture(filename)  # Si no se ha cargado, cargarla

        return cls.texture_ids[filename]  # Retornar el ID de textura correspondiente al archivo

    @classmethod
    def escenario(cls, filename):
        texture_id = cls.get_texture_id(filename)  # Obtener el ID de textura correspondiente al archivo

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, texture_id)  # Usar el ID de textura obtenido

        # Definir vértices y coordenadas de textura para el techo, piso y laterales
        vertices = [
            (-30, -25, 30), (30, -25, 30), (30, 25, 30), (-30, 25, 30),  # Frente
            (-30, -25, -30), (30, -25, -30), (30, 25, -30), (-30, 25, -30),  # Atrás
            (-30, 25, 30), (30, 25, 30), (30, 25, -30), (-30, 25, -30),  # Techo
            (-30, -25, 30), (30, -25, 30), (30, -25, -30), (-30, -25, -30),  # Piso
            (-30, -25, 30), (-30, 25, 30), (-30, 25, -30), (-30, -25, -30),  # Lateral izquierdo
            (30, -25, 30), (30, 25, 30), (30, 25, -30), (30, -25, -30)  # Lateral derecho
        ]

        tex_coords = [
            (0, 0), (1, 0), (1, 1), (0, 1),  # Frente
            (0, 0), (1, 0), (1, 1), (0, 1),  # Atrás
            (0, 0), (1, 0), (1, 1), (0, 1),  # Techo
            (0, 0), (1, 0), (1, 1), (0, 1),  # Piso
            (0, 0), (1, 0), (1, 1), (0, 1),  # Lateral izquierdo
            (0, 0), (1, 0), (1, 1), (0, 1)   # Lateral derecho
        ]

        # Dibujar el escenario con los nuevos vértices y coordenadas de textura
        for i in range(0, len(vertices), 4):
            glBegin(GL_QUADS)
            glColor(1, 1, 1)
            for j in range(4):
                glTexCoord2f(tex_coords[i + j][0], tex_coords[i + j][1])
                glVertex3f(*vertices[i + j])
            glEnd()

        glDisable(GL_TEXTURE_2D)
