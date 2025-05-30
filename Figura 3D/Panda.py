import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Panda:
    def __init__(self):
        self.cuerpo = [
                (2, -2, 0),  # A
                (2, -6, 0),  # B
                (5, -2, 0),  # C
                (5, -6, 0),  # D
                (2, -2, 2),  # E
                (2, -6,2),  # F
                (5, -2, 2),  # G
                (5, -6, 2)   # H
                ]
        self.cara = [
                (4.5, -2, 0),    # I
                (2.5, -2, 0),    # J
                (4.5, -2, 1.5),  # K
                (2.5, -2, 1.5),  # L
                (4.5, -0.5, 0),  # I_1
                (2.5, -0.5, 0),  # J_1
                (4.5, -0.5, 1.5),  # K_1
                (2.5, -0.5, 1.5)   # L_1
            ]
        self.edges = [
                (0, 1), (0, 2), (1, 3), (2, 3),  # Cara frontal
                (4, 5), (4, 6), (5, 7), (6, 7),  # Cara trasera
                (0, 4), (1, 5), (2, 6), (3, 7)   # Conexiones entre caras
            ]
            
    def draw_body(self):
        
        glColor3f(1,1,1)  # Color blanco
        glBegin(GL_QUADS)  # Usar GL_QUADS para rellenar las caras del cubo

        # Cara frontal
        glVertex3f(self.cuerpo[0][0], self.cuerpo[0][1], self.cuerpo[0][2])  # A
        glVertex3f(self.cuerpo[1][0], self.cuerpo[1][1], self.cuerpo[1][2])  # B
        glVertex3f(self.cuerpo[3][0], self.cuerpo[3][1], self.cuerpo[3][2])  # D
        glVertex3f(self.cuerpo[2][0], self.cuerpo[2][1], self.cuerpo[2][2])  # C

        # Cara trasera
        glVertex3f(self.cuerpo[4][0], self.cuerpo[4][1], self.cuerpo[4][2])  # E
        glVertex3f(self.cuerpo[5][0], self.cuerpo[5][1], self.cuerpo[5][2])  # F
        glVertex3f(self.cuerpo[7][0], self.cuerpo[7][1], self.cuerpo[7][2])  # H
        glVertex3f(self.cuerpo[6][0], self.cuerpo[6][1], self.cuerpo[6][2])  # G

        # Conectores entre caras
        glVertex3f(self.cuerpo[0][0], self.cuerpo[0][1], self.cuerpo[0][2])  # A
        glVertex3f(self.cuerpo[2][0], self.cuerpo[2][1], self.cuerpo[2][2])  # C
        glVertex3f(self.cuerpo[6][0], self.cuerpo[6][1], self.cuerpo[6][2])  # G
        glVertex3f(self.cuerpo[4][0], self.cuerpo[4][1], self.cuerpo[4][2])  # E

        # Otras conexiones
        glVertex3f(self.cuerpo[1][0], self.cuerpo[1][1], self.cuerpo[1][2])  # B
        glVertex3f(self.cuerpo[5][0], self.cuerpo[5][1], self.cuerpo[5][2])  # F
        glVertex3f(self.cuerpo[7][0], self.cuerpo[7][1], self.cuerpo[7][2])  # H
        glVertex3f(self.cuerpo[3][0], self.cuerpo[3][1], self.cuerpo[3][2])  # D

        # Conectores entre caras superior e inferior
        glVertex3f(self.cuerpo[0][0], self.cuerpo[0][1], self.cuerpo[0][2])  # A
        glVertex3f(self.cuerpo[1][0], self.cuerpo[1][1], self.cuerpo[1][2])  # B
        glVertex3f(self.cuerpo[5][0], self.cuerpo[5][1], self.cuerpo[5][2])  # F
        glVertex3f(self.cuerpo[4][0], self.cuerpo[4][1], self.cuerpo[4][2])  # E

        glVertex3f(self.cuerpo[2][0], self.cuerpo[2][1], self.cuerpo[2][2])  # C
        glVertex3f(self.cuerpo[3][0], self.cuerpo[3][1], self.cuerpo[3][2])  # D
        glVertex3f(self.cuerpo[7][0], self.cuerpo[7][1], self.cuerpo[7][2])  # H
        glVertex3f(self.cuerpo[6][0], self.cuerpo[6][1], self.cuerpo[6][2])  # G

        glEnd()

        glColor3f(0, 0,0)
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.cuerpo[vertex])
        glEnd()

        # DETALLES CUERPO
    
        # ARRIBA
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(2, -2.3, 2.01)
        glVertex3f(5, -2.3, 2.01)
        glVertex3f(5, -4.2, 2.01)
        glVertex3f(2, -4.2, 2.01)
        glEnd()
        
        # IZQUIERDA
        
            # IZQUIERDA
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(5.01, -2.2, 0.4)
        glVertex3f(5.01, -2, 0.4)
        glVertex3f(5.01, -2, 0)
        glVertex3f(5.01, -2.2, 0)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(5.01, -2.3, 0.8)
        glVertex3f(5.01, -2.2, 0.8)
        glVertex3f(5.01, -2.2, 0)
        glVertex3f(5.01, -2.3, 0)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(5.01, -2.3, 2)
        glVertex3f(5.01, -2.3, 0)
        glVertex3f(5.01, -3.2, 0)
        glVertex3f(5.01, -3.2, 2)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(5.01, -3.4, 0.2)
        glVertex3f(5.01, -3.4, 2)
        glVertex3f(5.01, -3.2, 2)
        glVertex3f(5.01, -3.2, 0.2)
        glEnd()
        
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(5.01, -3.6, 0.4)
        glVertex3f(5.01, -3.6, 2)
        glVertex3f(5.01, -3.4, 2)
        glVertex3f(5.01, -3.4, 0.4)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(5.01, -3.6, 0.8)
        glVertex3f(5.01, -3.8, 0.8)
        glVertex3f(5.01, -3.8, 2)
        glVertex3f(5.01, -3.6, 2)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(5.01, -3.8, 1.2)
        glVertex3f(5.01, -4, 1.2)
        glVertex3f(5.01, -4, 2)
        glVertex3f(5.01, -3.8, 2)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(5.01, -4, 1.6)
        glVertex3f(5.01, -4.2, 1.6)
        glVertex3f(5.01, -4.2, 2)
        glVertex3f(5.01, -4, 2)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(5, -1.99, 0.4)
        glVertex3f(4.8, -1.99, 0.4)
        glVertex3f(4.8, -1.99, 0)
        glVertex3f(5, -1.99, 0)
        glEnd()
        
        # DERECHA
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(1.99, -2.2, 0.4)
        glVertex3f(1.99, -2, 0.4)
        glVertex3f(1.99, -2, 0)
        glVertex3f(1.99, -2.2, 0)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(1.99, -2.3, 0.8)
        glVertex3f(1.99, -2.2, 0.8)
        glVertex3f(1.99, -2.2, 0)
        glVertex3f(1.99, -2.3, 0)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(1.99, -2.3, 2)
        glVertex3f(1.99, -2.3, 0)
        glVertex3f(1.99, -3.2, 0)
        glVertex3f(1.99, -3.2, 2)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(1.99, -3.4, 0.2)
        glVertex3f(1.99, -3.4, 2)
        glVertex3f(1.99, -3.2, 2)
        glVertex3f(1.99, -3.2, 0.2)
        glEnd()
        
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(1.99, -3.6, 0.4)
        glVertex3f(1.99, -3.6, 2)
        glVertex3f(1.99, -3.4, 2)
        glVertex3f(1.99, -3.4, 0.4)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(1.99, -3.6, 0.8)
        glVertex3f(1.99, -3.8, 0.8)
        glVertex3f(1.99, -3.8, 2)
        glVertex3f(1.99, -3.6, 2)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(1.99, -3.8, 1.2)
        glVertex3f(1.99, -4, 1.2)
        glVertex3f(1.99, -4, 2)
        glVertex3f(1.99, -3.8, 2)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(1.99, -4, 1.6)
        glVertex3f(1.99, -4.2, 1.6)
        glVertex3f(1.99, -4.2, 2)
        glVertex3f(1.99, -4, 2)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(2, -1.99, 0.4)
        glVertex3f(2, -1.99, 0)
        glVertex3f(2.2, -1.99, 0)
        glVertex3f(2.2, -1.99, 0.4)
        glEnd()

    def draw_face(self):
        glColor3f(1,1,1)  # Color blanco
        glBegin(GL_QUADS)  # Usar GL_QUADS para rellenar las caras del cubo

        # Cara frontal
        glVertex3f(self.cara[0][0], self.cara[0][1], self.cara[0][2])  # A
        glVertex3f(self.cara[1][0], self.cara[1][1], self.cara[1][2])  # B
        glVertex3f(self.cara[3][0], self.cara[3][1], self.cara[3][2])  # D
        glVertex3f(self.cara[2][0], self.cara[2][1], self.cara[2][2])  # C

        # Cara trasera
        glVertex3f(self.cara[4][0], self.cara[4][1], self.cara[4][2])  # E
        glVertex3f(self.cara[5][0], self.cara[5][1], self.cara[5][2])  # F
        glVertex3f(self.cara[7][0], self.cara[7][1], self.cara[7][2])  # H
        glVertex3f(self.cara[6][0], self.cara[6][1], self.cara[6][2])  # G

        # Conectores entre caras
        glVertex3f(self.cara[0][0], self.cara[0][1], self.cara[0][2])  # A
        glVertex3f(self.cara[2][0], self.cara[2][1], self.cara[2][2])  # C
        glVertex3f(self.cara[6][0], self.cara[6][1], self.cara[6][2])  # G
        glVertex3f(self.cara[4][0], self.cara[4][1], self.cara[4][2])  # E

        # Otras conexiones
        glVertex3f(self.cara[1][0], self.cara[1][1], self.cara[1][2])  # B
        glVertex3f(self.cara[5][0], self.cara[5][1], self.cara[5][2])  # F
        glVertex3f(self.cara[7][0], self.cara[7][1], self.cara[7][2])  # H
        glVertex3f(self.cara[3][0], self.cara[3][1], self.cara[3][2])  # D

        # Conectores entre caras superior e inferior
        glVertex3f(self.cara[0][0], self.cara[0][1], self.cara[0][2])  # A
        glVertex3f(self.cara[1][0], self.cara[1][1], self.cara[1][2])  # B
        glVertex3f(self.cara[5][0], self.cara[5][1], self.cara[5][2])  # F
        glVertex3f(self.cara[4][0], self.cara[4][1], self.cara[4][2])  # E

        glVertex3f(self.cara[2][0], self.cara[2][1], self.cara[2][2])  # C
        glVertex3f(self.cara[3][0], self.cara[3][1], self.cara[3][2])  # D
        glVertex3f(self.cara[7][0], self.cara[7][1], self.cara[7][2])  # H
        glVertex3f(self.cara[6][0], self.cara[6][1], self.cara[6][2])  # G

        glEnd()
         # Dibujar las líneas
        glColor3f(0, 0,0)
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.cara[vertex])
        glEnd()
        
        # DETALLES CARA MANCHAS
        # IZQUIERDA
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(4.5, -0.49, 1.2)
        glVertex3f(4.2, -0.49, 1.2)
        glVertex3f(4.2, -0.49, 0.3)
        glVertex3f(4.5, -0.49, 0.3)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(4.2, -0.49, 1.4)
        glVertex3f(3.8, -0.49, 1.4)
        glVertex3f(3.8, -0.49, 0.9)
        glVertex3f(4.2, -0.49, 0.9)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(3.8, -0.49, 1.2)
        glVertex3f(3.6, -0.49, 1.2)
        glVertex3f(3.6, -0.49, 0.7)
        glVertex3f(3.8, -0.49, 0.7)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(4.2, -0.49, 0.7)
        glVertex3f(4.2, -0.49, 0.5)
        glVertex3f(4, -0.49, 0.5)
        glVertex3f(4, -0.49, 0.7)
        glEnd()
        
        # IZQUIERDA PANEL IZQUIERDO
        
        # DERECHA PANEL DERECHO
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(4.51, -0.5, 1.2)
        glVertex3f(4.51, -0.7, 1.2)
        glVertex3f(4.51, -0.7, 0.3)
        glVertex3f(4.51, -0.5, 0.3)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(4.51, -0.7, 1)
        glVertex3f(4.51, -0.9, 1)
        glVertex3f(4.51, -0.9, 0.3)
        glVertex3f(4.51, -0.7, 0.3)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(4.51, -0.9, 0.8)
        glVertex3f(4.51, -1.1, 0.8)
        glVertex3f(4.51, -1.1, 0.5)
        glVertex3f(4.51, -0.9, 0.5)
        glEnd()
        
        # DERECHA
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(3.4, -0.49, 0.7)
        glVertex3f(3.4, -0.49, 1.2)
        glVertex3f(3.2, -0.49, 1.2)
        glVertex3f(3.2, -0.49, 0.7)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(3.2, -0.49, 1.4)
        glVertex3f(2.8, -0.49, 1.4)
        glVertex3f(2.8, -0.49, 0.9)
        glVertex3f(3.2, -0.49, 0.9)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(2.8, -0.49, 1.2)
        glVertex3f(2.5, -0.49, 1.2)
        glVertex3f(2.5, -0.49, 0.3)
        glVertex3f(2.8, -0.49, 0.3)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(3, -0.49, 0.7)
        glVertex3f(2.8, -0.49, 0.7)
        glVertex3f(2.8, -0.49, 0.5)
        glVertex3f(3, -0.49, 0.5)
        glEnd()
        
        # DERECHA PANEL DERECHO
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(2.49, -0.5, 1.2)
        glVertex3f(2.49, -0.7, 1.2)
        glVertex3f(2.49, -0.7, 0.3)
        glVertex3f(2.49, -0.5, 0.3)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(2.49, -0.7, 1)
        glVertex3f(2.49, -0.9, 1)
        glVertex3f(2.49, -0.9, 0.3)
        glVertex3f(2.49, -0.7, 0.3)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)
        glVertex3f(2.49, -0.9, 0.8)
        glVertex3f(2.49, -1.1, 0.8)
        glVertex3f(2.49, -1.1, 0.5)
        glVertex3f(2.49, -0.9, 0.5)
        glEnd()
        

    def draw_eye1(self,color,color2):
        # Derecho
        glBegin(GL_QUADS)
        #glColor3f(0.5, 0.5, 0.5)
        glColor3f(color[0],color[1],color[2])  # Color blanco
        glVertex3f(3.2, -0.49, 0.9)
        glVertex3f(3, -0.49, 0.9)
        glVertex3f(3, -0.49, 0.7)
        glVertex3f(3.2, -0.49, 0.7)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(color2[0],color2[1],color2[2])
        glVertex3f(3, -0.49, 0.9)
        glVertex3f(2.8, -0.49, 0.9)
        glVertex3f(2.8, -0.49, 0.7)
        glVertex3f(3, -0.49, 0.7)
        glEnd()
        
        # Derecho lineas
        glBegin(GL_LINE_LOOP)
        glColor3f(0, 0.2, 0.6)  # Color rojo
        glVertex3f(3.2, -0.49, 0.9)
        glVertex3f(3, -0.49, 0.9)
        glVertex3f(3, -0.49, 0.7)
        glVertex3f(3.2, -0.49, 0.7)
        glEnd()
        
        glBegin(GL_LINE_LOOP)
        glColor3f(0, 0.2, 0.6)  # Color rojo
        glVertex3f(3, -0.49, 0.9)
        glVertex3f(2.8, -0.49, 0.9)
        glVertex3f(2.8, -0.49, 0.7)
        glVertex3f(3, -0.49, 0.7)
        glEnd()


    def draw_eye2(self,color,color2):
        # Izquierdo
        glBegin(GL_QUADS)
        glColor3f(color2[0],color2[1],color2[2])
        glVertex3f(4.2, -0.49, 0.9)
        glVertex3f(4, -0.49, 0.9)
        glVertex3f(4, -0.49, 0.7)
        glVertex3f(4.2, -0.49, 0.7)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(color[0],color[1],color[2])
        #glColor3f(0.5, 0.49, 0.5)
        glVertex3f(4, -0.49, 0.9)
        glVertex3f(3.8, -0.49, 0.9)
        glVertex3f(3.8, -0.49, 0.7)
        glVertex3f(4, -0.49, 0.7)
        glEnd()
        
        glBegin(GL_LINE_LOOP)
        glColor3f(0, 0.2, 0.6)  # Color rojo
        glVertex3f(4.2, -0.49, 0.9)
        glVertex3f(4, -0.49, 0.9)
        glVertex3f(4, -0.49, 0.7)
        glVertex3f(4.2, -0.49, 0.7)
        glEnd()
        
        glBegin(GL_LINE_LOOP)
        glColor3f(0, 0.2, 0.6)  # Color rojo
        glVertex3f(4, -0.49, 0.9)
        glVertex3f(3.8, -0.49, 0.9)
        glVertex3f(3.8, -0.49, 0.7)
        glVertex3f(4, -0.49, 0.7)
        glEnd()
        

    def draw_muzzle(self):
        # Osico
        glColor3f(1.0, 1.0, 1.0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)  # Establecer el modo de polígono a relleno
        glBegin(GL_POLYGON)
        # Cara frontal
        glVertex3f(3, 0, 0.7)
        glVertex3f(4,0,0.7)
        glVertex3f(4, 0, 0)
        glVertex3f(3, 0, 0)
        # Cara posterior
        glVertex3f(3, -0.5, 0.7)
        glVertex3f(4, -0.5, 0.7)
        glVertex3f(4, -0.5, 0)
        glVertex3f(3, -0.5, 0)
        # Cara superior
        glVertex3f(3, -0.5, 0.7)
        glVertex3f(4, -0.5, 0.7)
        glVertex3f(4, 0, 0.7)
        glVertex3f(3, 0, 0.7)
        # Cara inferior
        glVertex3f(3, -0.5, 0)
        glVertex3f(4, -0.5, 0)
        glVertex3f(4, 0, 0)
        glVertex3f(3, 0, 0)
        # Cara derecha
        glVertex3f(4, -0.5, 0.7)
        glVertex3f(4, 0, 0.7)
        glVertex3f(4, 0, 0)
        glVertex3f(4, -0.5, 0)
        # Cara izquierda
        glVertex3f(3, -0.5, 0.7)
        glVertex3f(3, 0, 0.7)
        glVertex3f(3, 0, 0)
        glVertex3f(3, -0.5, 0)
        glEnd()
        
        # Lineas osico
        glColor3f(0, 0.2, 0.6)
        glBegin(GL_LINES)
        # Cara frontal
        glVertex3f(3, 0, 0.7)
        glVertex3f(4, 0, 0.7)

        glVertex3f(4, 0, 0.7)
        glVertex3f(4, 0, 0)

        glVertex3f(4, 0, 0)
        glVertex3f(3, 0, 0)

        glVertex3f(3, 0, 0)
        glVertex3f(3, 0, 0.7)
        
        

        # Cara posterior
        glVertex3f(3, -0.5, 0.7)
        glVertex3f(4, -0.5, 0.7)

        glVertex3f(4, -0.5, 0.7)
        glVertex3f(4, -0.5, 0)

        glVertex3f(4, -0.5, 0)
        glVertex3f(3, -0.5, 0)

        glVertex3f(3, -0.5, 0)
        glVertex3f(3, -0.5, 0.7)

        # Conexiones verticales
        glVertex3f(3, 0, 0.7)
        glVertex3f(3, -0.5, 0.7)

        glVertex3f(4, 0, 0.7)
        glVertex3f(4, -0.5, 0.7)

        glVertex3f(4, 0, 0)
        glVertex3f(4, -0.5, 0)

        glVertex3f(3, 0, 0)
        glVertex3f(3, -0.5, 0)

        glEnd()
        # Detalles nariz
        # Dibujar una figura 2D en 3D
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)  # Color rojo
        glVertex3f(3.8, 0.01, 0.7)
        glVertex3f(3.8, 0.01, 0.3)
        glVertex3f(3.2, 0.01, 0.3)
        glVertex3f(3.2, 0.01, 0.7)
        glEnd()
        
        #Detalle nariz 2
        glBegin(GL_QUADS)
        glColor3f(0, 0.2, 0.6)  # Color rojo
        glVertex3f(3.6, 0.01, 0.3)
        glVertex3f(3.4, 0.01, 0.3)
        glVertex3f(3.4, 0.01, 0.2)
        glVertex3f(3.6, 0.01, 0.2)
        glEnd()
        
    def draw_mouth_happy(self):
        #Detalle boca
        #Detalle nariz 2
        glBegin(GL_QUADS)
        glColor3f(0.7, 0.7, 0.7)  # Color gris claro
        glVertex3f(3.8, 0.01, 0.1)
        glVertex3f(3.2, 0.01, 0.1)
        glVertex3f(3.2, 0.01, 0)
        glVertex3f(3.8, 0.01, 0)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0.7, 0.7, 0.7)  # Color gris claro
        glVertex3f(3.9, 0.01, 0.2)
        glVertex3f(3.8, 0.01, 0.2)
        glVertex3f(3.8, 0.01, 0.1)
        glVertex3f(3.9, 0.01, 0.1)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0.7, 0.7, 0.7)  # Color gris claro
        glVertex3f(3.2, 0.01, 0.2)
        glVertex3f(3.1, 0.01, 0.2)
        glVertex3f(3.1, 0.01, 0.1)
        glVertex3f(3.2, 0.01, 0.1)
        glEnd()

    def draw_mouth(self):
        #Detalle boca
        #Detalle nariz 2
        glBegin(GL_QUADS)
        glColor3f(0.7, 0.7, 0.7)  # Color gris claro
        glVertex3f(3.8, 0.01, 0.2)
        glVertex3f(3.2, 0.01, 0.2)
        glVertex3f(3.2, 0.01, 0.1)
        glVertex3f(3.8, 0.01, 0.1)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0.7, 0.7, 0.7)  # Color gris claro
        glVertex3f(3.9, 0.01, 0.1)
        glVertex3f(3.8, 0.01, 0.1)
        glVertex3f(3.8, 0.01, 0)
        glVertex3f(3.9, 0.01, 0)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0.7, 0.7, 0.7)  # Color gris claro
        glVertex3f(3.2, 0.01, 0.1)
        glVertex3f(3.1, 0.01, 0.1)
        glVertex3f(3.1, 0.01, 0)
        glVertex3f(3.2, 0.01, 0)
        glEnd()

    def draw_mouth_leng(self):
        #Detalle boca
        #Detalle nariz 2
        glBegin(GL_QUADS)
        glColor3f(0.7, 0.7, 0.7)  # Color gris claro
        glVertex3f(3.8, 0.01, 0.2)
        glVertex3f(3.8, 0.01, 0.1)
        glVertex3f(3.6, 0.01, 0.1)
        glVertex3f(3.6, 0.01, 0.2)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.5, 0.5)  # Color gris claro
        glVertex3f(3.4, 0.01, 0.2)
        glVertex3f(3.6, 0.01, 0.2)
        glVertex3f(3.6, 0.01, 0.1)
        glVertex3f(3.4, 0.01, 0.1)
        glEnd()


        glBegin(GL_QUADS)
        glColor3f(0.5, 0.5, 0.5)  # Color gris claro
        glVertex3f(3.2, 0.01, 0.2)
        glVertex3f(3.4, 0.01, 0.2)
        glVertex3f(3.4, 0.01, 0.1)
        glVertex3f(3.2, 0.01, 0.1)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.5, 0.5)  # Color gris claro
        glVertex3f(3.4, 0.01, 0.1)
        glVertex3f(3.6, 0.01, 0.1)
        glVertex3f(3.6, 0.01, 0)
        glVertex3f(3.4, 0.01, 0)
        glEnd()

    def draw_ears(self):
        # Oreja derecha
        glColor3f(0, 0.2, 0.6)
        glBegin(GL_QUADS)
        # Cara frontal
        glVertex3f(3, -1.25, 2)
        glVertex3f(2.2, -1.25, 2)
        glVertex3f(2.2, -1, 2)
        glVertex3f(3, -1, 2)
        # Cara posterior
        glVertex3f(3, -1.25, 1.3)
        glVertex3f(2.2, -1.25, 1.3)
        glVertex3f(2.2, -1, 1.3)
        glVertex3f(3, -1, 1.3)
        # Cara superior
        glVertex3f(2.2, -1.25, 2)
        glVertex3f(2.2, -1.25, 1.3)
        glVertex3f(2.2, -1, 1.3)
        glVertex3f(2.2, -1, 2)
        # Cara inferior
        glVertex3f(3, -1.25, 2)
        glVertex3f(3, -1.25, 1.3)
        glVertex3f(3, -1, 1.3)
        glVertex3f(3, -1, 2)
        # Cara derecha
        glVertex3f(3, -1.25, 2)
        glVertex3f(3, -1.25, 1.3)
        glVertex3f(2.2, -1.25, 1.3)
        glVertex3f(2.2, -1.25, 2)
        # Cara izquierda
        glVertex3f(3, -1, 2)
        glVertex3f(3, -1, 1.3)
        glVertex3f(2.2, -1, 1.3)
        glVertex3f(2.2, -1, 2)
        glEnd()

        # Oreja izquierda
        # Render cubo con los nuevos puntos
        glBegin(GL_QUADS)
        # Cara frontal
        glVertex3f(5, -1.25, 2)    # P9
        glVertex3f(4.2, -1.25, 2)  # P10
        glVertex3f(4.2, -1, 2)     # P14
        glVertex3f(5, -1, 2)       # P15

        # Cara posterior
        glVertex3f(5, -1.25, 1.3)   # P12
        glVertex3f(4.2, -1.25, 1.3) # P11
        glVertex3f(4.2, -1, 1.3)       # P13
        glVertex3f(5, -1, 1.3)      # P16

        # Cara superior
        glVertex3f(4.2, -1.25, 2)     # P10
        glVertex3f(4.2, -1.25, 1.3)    # P11
        glVertex3f(4.2, -1, 1.3)       # P13
        glVertex3f(4.2, -1, 2)        # P14

        # Cara inferior
        glVertex3f(5, -1.25, 2)    # P9
        glVertex3f(5, -1.25, 1.3)   # P12
        glVertex3f(5, -1, 1.3)      # P15
        glVertex3f(5, -1, 2)       # P16

        # Cara derecha
        glVertex3f(5, -1.25, 2)    # P9
        glVertex3f(5, -1.25, 1.3)   # P12
        glVertex3f(4.2, -1.25, 1.3) # P11
        glVertex3f(4.2, -1.25, 2)     # P10

        # Cara izquierda
        glVertex3f(5, -1, 2)       # P15
        glVertex3f(5, -1, 1.3)      # P16
        glVertex3f(4.2, -1, 1.3)       # P13
        glVertex3f(4.2, -1, 2)        # P14
        glEnd()


    def draw_leg_inf_right(self):
            #PATAS
        #TRASERA DERECHA
        glColor3f(0, 0.2, 0.6)
        glBegin(GL_QUADS)

        # Cara frontal
        glVertex3f(3.8, -5.7, 0)    # A
        glVertex3f(3.8, -4.8, 0)    # B
        glVertex3f(4.7, -4.8, 0)    # C
        glVertex3f(4.7, -5.7, 0)    # D

        # Cara posterior
        glVertex3f(3.8, -5.7, -1.3) # E
        glVertex3f(3.8, -4.8, -1.3) # F
        glVertex3f(4.7, -4.8, -1.3) # G
        glVertex3f(4.7, -5.7, -1.3) # H

        # Cara superior
        glVertex3f(3.8, -4.8, 0)    # B
        glVertex3f(3.8, -4.8, -1.3) # F
        glVertex3f(4.7, -4.8, -1.3) # G
        glVertex3f(4.7, -4.8, 0)    # C

        # Cara inferior
        glVertex3f(3.8, -5.7, 0)    # A
        glVertex3f(3.8, -5.7, -1.3) # E
        glVertex3f(4.7, -5.7, -1.3) # H
        glVertex3f(4.7, -5.7, 0)    # D

        # Cara derecha
        glVertex3f(4.7, -5.7, 0)    # D
        glVertex3f(4.7, -5.7, -1.3) # H
        glVertex3f(4.7, -4.8, -1.3) # G
        glVertex3f(4.7, -4.8, 0)    # C

        # Cara izquierda
        glVertex3f(3.8, -5.7, 0)    # A
        glVertex3f(3.8, -5.7, -1.3) # E
        glVertex3f(3.8, -4.8, -1.3) # F
        glVertex3f(3.8, -4.8, 0)    # B

        glEnd()
    
    def draw_leg_inf_left(self):
            # TRASERA IZQUIERDA
        glColor3f(0, 0.2, 0.6)
        glBegin(GL_QUADS)
        # Cara frontal
        glVertex3f(2.3, -5.7, 0)    # C13
        glVertex3f(3.2, -5.7, 0)    # C14
        glVertex3f(3.2, -4.8, 0)    # C16
        glVertex3f(2.3, -4.8, 0)    # C15

        # Cara posterior
        glVertex3f(2.3, -5.7, -1.3) # C31
        glVertex3f(3.2, -5.7, -1.3) # C30
        glVertex3f(3.2, -4.8, -1.3) # C29
        glVertex3f(2.3, -4.8, -1.3) # C32

        # Cara superior
        glVertex3f(3.2, -5.7, 0)    # C14
        glVertex3f(3.2, -5.7, -1.3) # C30
        glVertex3f(3.2, -4.8, -1.3) # C29
        glVertex3f(3.2, -4.8, 0)    # C16

        # Cara inferior
        glVertex3f(2.3, -5.7, 0)    # C13
        glVertex3f(2.3, -5.7, -1.3) # C31
        glVertex3f(2.3, -4.8, -1.3) # C32
        glVertex3f(2.3, -4.8, 0)    # C15

        # Cara derecha
        glVertex3f(3.2, -5.7, 0)    # C14
        glVertex3f(3.2, -5.7, -1.3) # C30
        glVertex3f(2.3, -5.7, -1.3) # C31
        glVertex3f(2.3, -5.7, 0)    # C13

        # Cara izquierda
        glVertex3f(3.2, -4.8, 0)    # C16
        glVertex3f(3.2, -4.8, -1.3) # C29
        glVertex3f(2.3, -4.8, -1.3) # C32
        glVertex3f(2.3, -4.8, 0)    # C15

        glEnd()
    
    def draw_leg_sup_right(self):
        #DELANTERA DERECHA
        glBegin(GL_QUADS)

        # Cara frontal
        glVertex3f(3.8, -2.3, 0)    # C4
        glVertex3f(4.7, -2.3, 0)    # C3
        glVertex3f(4.7, -3.2, 0)    # C5
        glVertex3f(3.8, -3.2, 0)    # C6

        # Cara posterior
        glVertex3f(3.8, -2.3, -1.3) # C19
        glVertex3f(4.7, -2.3, -1.3) # C18
        glVertex3f(4.7, -3.2, -1.3) # C17
        glVertex3f(3.8, -3.2, -1.3) # C20

        # Cara superior
        glVertex3f(4.7, -2.3, 0)    # C3
        glVertex3f(4.7, -2.3, -1.3) # C18
        glVertex3f(3.8, -2.3, -1.3) # C19
        glVertex3f(3.8, -2.3, 0)    # C4

        # Cara inferior
        glVertex3f(3.8, -3.2, 0)    # C6
        glVertex3f(3.8, -3.2, -1.3) # C20
        glVertex3f(4.7, -3.2, -1.3) # C17
        glVertex3f(4.7, -3.2, 0)    # C5

        # Cara derecha
        glVertex3f(4.7, -2.3, 0)    # C3
        glVertex3f(4.7, -2.3, -1.3) # C18
        glVertex3f(4.7, -3.2, -1.3) # C17
        glVertex3f(4.7, -3.2, 0)    # C5

        # Cara izquierda
        glVertex3f(3.8, -2.3, 0)    # C4
        glVertex3f(3.8, -2.3, -1.3) # C19
        glVertex3f(3.8, -3.2, -1.3) # C20
        glVertex3f(3.8, -3.2, 0)    # C6

        glEnd()
    
    def draw_leg_sup_left(self):
            # DELANTERA IZQUIERDA
        glBegin(GL_QUADS)

        # Cara frontal
        glVertex3f(2.3, -2.3, 0)    # C1
        glVertex3f(3.2, -2.3, 0)    # C2
        glVertex3f(3.2, -3.2, 0)    # C8
        glVertex3f(2.3, -3.2, 0)    # C7

        # Cara posterior
        glVertex3f(2.3, -2.3, -1.3) # C22
        glVertex3f(3.2, -2.3, -1.3) # C24
        glVertex3f(3.2, -3.2, -1.3) # C23
        glVertex3f(2.3, -3.2, -1.3) # C21

        # Cara superior
        glVertex3f(3.2, -2.3, 0)    # C2
        glVertex3f(3.2, -2.3, -1.3) # C24
        glVertex3f(2.3, -2.3, -1.3) # C22
        glVertex3f(2.3, -2.3, 0)    # C1

        # Cara inferior
        glVertex3f(2.3, -3.2, 0)    # C7
        glVertex3f(2.3, -3.2, -1.3) # C21
        glVertex3f(3.2, -3.2, -1.3) # C23
        glVertex3f(3.2, -3.2, 0)    # C8

        # Cara derecha
        glVertex3f(3.2, -2.3, 0)    # C2
        glVertex3f(3.2, -2.3, -1.3) # C24
        glVertex3f(3.2, -3.2, -1.3) # C23
        glVertex3f(3.2, -3.2, 0)    # C8

        # Cara izquierda
        glVertex3f(2.3, -2.3, 0)    # C1
        glVertex3f(2.3, -2.3, -1.3) # C22
        glVertex3f(2.3, -3.2, -1.3) # C21
        glVertex3f(2.3, -3.2, 0)    # C7

        glEnd()