import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from escenario import Escenario as es
from Panda import Panda
import textos as txt
import iluminacion as li
import audio as au

class Main:
    # Función para inicializar Pygame y OpenGL
    
    def __init__(self):
        pygame.init()
        width, height = 800, 600
        window = pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
        pygame.display.set_caption('Panda')
        self.pd = Panda()
        self.op = True
        self.x = 0
        self.y = 0
        self.audio = au.ReproductorAudio(num_canales=2)
        self.colorOjo = (0.5, 0.49, 0.5)
        self.colorOjo2 = (1,1,1)
        self.escenario = "Fondos/R.jpeg"
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, (width / height), 0.1, 130.0)
        glMatrixMode(GL_MODELVIEW)
        glEnable(GL_DEPTH_TEST)
        self.camera_position = [0, 0, 15.0]
        self.camera_speed = 0.1


    
    # Función para manejar la entrada del teclado
    def handle_input(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        if keys[pygame.K_ESCAPE]:
            return False

        # Movimiento de la cámara
        if keys[pygame.K_LEFT]:
            self.camera_position[0] -= self.camera_speed
        if keys[pygame.K_RIGHT]:
            self.camera_position[0] += self.camera_speed
        if keys[pygame.K_UP]:
            self.camera_position[1] += self.camera_speed
        if keys[pygame.K_DOWN]:
            self.camera_position[1] -= self.camera_speed
        if keys[pygame.K_w]:
            self.camera_position[2] -= self.camera_speed
        if keys[pygame.K_s]:
            self.camera_position[2] += self.camera_speed
        
        # Restaurar posición de la cámara
        if keys[pygame.K_LSHIFT]:
            self.camera_position = [0, 0, 15.0]

        return True

    # Función para dibujar la escena
    def draw(self):
        keys = pygame.key.get_pressed()
        glLoadIdentity()
        gluLookAt(
            self.camera_position[0], self.camera_position[1], self.camera_position[2],
            self.camera_position[0], self.camera_position[1], self.camera_position[2] - 1,
            0, 1, 0
        )
        es.escenario(self.escenario)
        
        glRotatef(180, 0, 1, 1)  # Rotar 90 grados alrededor del eje X
        
        if keys[pygame.K_q]:
            
            if(self.op):
                self.op = not(self.op)
            txt.texto("Acerca de:", -1, 0, 5.0, 25, 255, 255, 255, 0, 0, 0)
            txt.texto("Alumno: Jair Garduño Rodriguez", -1, 0, 4.5, 25, 255, 255, 255, 0, 0, 0)
            txt.texto("No. Control: 21281153", -1, 0, 4, 25, 255, 255, 255, 0, 0, 0)
            pygame.time.wait(100)

        
        
        if self.op:
                # TEXTO POSX POSY POSZ TAM R G B RB GB BB
            txt.texto("Instrucciones", -1, 0, 5.0, 25, 255, 255, 255, 0, 0, 0)
            txt.texto("Teclas de flecha: Mover cámara", -1, 0, 4.5, 25, 255, 255, 255, 0, 0, 0)
            txt.texto("W/S: Avanzar/Retroceder", -1, 0, 4.0, 25, 255, 255, 255, 0, 0, 0)
            txt.texto("L SHIFT: Restaurar posición de la cámara", -1, 0, 3.5, 25, 255, 255, 255, 0, 0, 0)
            txt.texto("O/P: Cerrar ojo Izquierdo/Derecho", -1, 0, 3.0, 25, 255, 255, 255, 0, 0, 0)
            txt.texto("L: Tristeza", -1, 0, 2.5, 25, 255, 255, 255, 0, 0, 0)
            txt.texto("K: Sonrisa", -1, 0, 2.0, 25, 255, 255, 255, 0, 0, 0)
            txt.texto("I: Mostrar Lengua", -1, 0, 1.5, 25, 255, 255, 255, 0, 0, 0)
            txt.texto("U/J: Mover patas delanteras", -1, 0, 1.0, 25, 255, 255, 255, 0, 0, 0)
            txt.texto("M/N: Mover patas traseras", -1, 0, 0.5, 25, 255, 255, 255, 0, 0, 0)
            txt.texto("Y: Mover ambas patas traseras", -1, 0, 0.0, 25, 255, 255, 255, 0, 0, 0)
            txt.texto("1/2/3/4/5: Cambiar fondo", -1, 0, -0.5, 25, 255, 255, 255, 0, 0, 0)
            txt.texto("Z/X/C/V: Derecha/Izquierda/Adelante/Atras", -1, 0, -1, 25, 255, 255, 255, 0, 0, 0)
            txt.texto("G: Expresión, Movimiento, Sonido, Escenario", -1, 0, -1.5, 25, 255, 255, 255, 0, 0, 0)
            txt.texto("H/B: Encender sonido/Apagar sonido", -1, 0, -2, 25, 255, 255, 255, 0, 0, 0)
            txt.texto("T: Ocultar/Mostrar instrucciones", -1, 0, -2.5, 25, 255, 255, 255, 0, 0, 0)
            txt.texto("E: Iluminación", -1, 0, -3, 25, 255, 255, 255, 0, 0, 0)
            txt.texto("A: Original", -1, 0, -3.5, 25, 255, 255, 255, 0, 0, 0)
            txt.texto("Q: Acerca de Jair", -1, 0, -4, 25, 255, 255, 255, 0, 0, 0)
        glTranslatef(self.x,self.y,0)

        if keys[pygame.K_t]:
            self.op = not(self.op)
            pygame.time.wait(100)

       

        if keys[pygame.K_z]:
            self.x += 1
            pygame.time.wait(100)
        if keys[pygame.K_x]:
            self.x -= 1
            pygame.time.wait(100)
        if keys[pygame.K_c]:
            self.y += 1
            pygame.time.wait(100)
        if keys[pygame.K_v]:
            self.y -= 1
            pygame.time.wait(100)
        

        if keys[pygame.K_e]:
            # Iluminacion
            li.iluminacion(1.0, 1.0, 1.0)  # Luz blanca
            li.toggle_iluminacion()

        self.pd.draw_body()

        self.pd.draw_face()

        if keys[pygame.K_o]:
            self.pd.draw_eye1((0, 0.2, 0.6),(0, 0.2, 0.6))
            self.audio.reproducir_audio("Audio/1.wav",canal=0)
            pygame.time.wait(150)

        else:
            self.pd.draw_eye1(self.colorOjo,self.colorOjo2)

        if keys[pygame.K_p]:
            self.pd.draw_eye2((0, 0.2, 0.6),(0, 0.2, 0.6))
            self.audio.reproducir_audio("Audio/2.wav",canal=0)
            pygame.time.wait(150)
        else:
            self.pd.draw_eye2(self.colorOjo,self.colorOjo2)


        self.pd.draw_muzzle()

        if keys[pygame.K_l]:
            self.pd.draw_mouth()
            self.audio.reproducir_audio("Audio/3.wav",canal=0)
            pygame.time.wait(150)
        
        if keys[pygame.K_k]:
            self.pd.draw_mouth_happy()
            self.audio.reproducir_audio("Audio/4.wav",canal=0)
            pygame.time.wait(150)
        elif keys[pygame.K_i]:
            self.pd.draw_mouth_leng()
            self.audio.reproducir_audio("Audio/5.wav",canal=0)
            pygame.time.wait(150)
        self.pd.draw_ears()

        if keys[pygame.K_g]:
            es.escenario("Fondos/fondo1.jpg")            
            self.pd.draw_mouth_leng()
            self.audio.reproducir_audio("Audio/3.wav",canal=0)
            pygame.time.wait(150)
            self.pd.draw_leg_inf_left()
            self.pd.draw_leg_inf_right()
            glRotatef(20, 1, 0, 0)  # Rotar 90 grados alrededor del eje X
            glTranslatef(0,0,1)
            self.pd.draw_leg_sup_left()
            self.pd.draw_leg_sup_right()
            glLoadIdentity()

        if keys[pygame.K_u]:
            self.pd.draw_leg_inf_left()
            self.pd.draw_leg_sup_left()
            self.pd.draw_leg_inf_right()
            glRotatef(20, 1, 0, 0)  # Rotar 90 grados alrededor del eje X
            glTranslatef(0,0,1)
            self.pd.draw_leg_sup_right()
            glLoadIdentity()
            
        
        elif keys[pygame.K_j]:
            self.pd.draw_leg_inf_left()
            self.pd.draw_leg_sup_right()
            self.pd.draw_leg_inf_right()
            glRotatef(20, 1, 0, 0)  # Rotar 90 grados alrededor del eje X
            glTranslatef(0,0,1)
            self.pd.draw_leg_sup_left()
            glLoadIdentity()

        if keys[pygame.K_m]:
            self.pd.draw_leg_sup_left()
            self.pd.draw_leg_sup_right()
            self.pd.draw_leg_inf_right()
            glRotatef(20, 1, 0, 0)  # Rotar 90 grados alrededor del eje X
            glTranslatef(0,0,2)
            self.pd.draw_leg_inf_left()
            glLoadIdentity()
        else:
            self.pd.draw_leg_inf_left()
        if keys[pygame.K_n]:
            self.pd.draw_leg_sup_left()
            self.pd.draw_leg_sup_right()
            self.pd.draw_leg_inf_left()
            glRotatef(20, 1, 0, 0)  # Rotar 90 grados alrededor del eje X
            glTranslatef(0,0,2)
            self.pd.draw_leg_inf_right()
            glLoadIdentity()
        else:
            self.pd.draw_leg_inf_right()

        if keys[pygame.K_y]:
            self.pd.draw_leg_inf_left()
            glRotatef(20, 1, 0, 0)  # Rotar 90 grados alrededor del eje X
            glTranslatef(0,0,1)
            self.pd.draw_leg_sup_left()
            self.pd.draw_leg_sup_right()
            glLoadIdentity()
        else:
            self.pd.draw_leg_sup_left()
            self.pd.draw_leg_sup_right()


        if keys[pygame.K_h]:
            self.audio.reproducir_audio("Audio/zelda.wav",canal=1)
        elif keys[pygame.K_b]:
            self.audio.detener_audio(canal=1)
        

        if keys[pygame.K_a]:
            self.x = self.x - self.x
            self.x = self.y - self.y

        

        if keys[pygame.K_1]:
            self.escenario = ("Fondos/R.jpeg")
        elif keys[pygame.K_2]:
            self.escenario = ("Fondos/fondo1.jpg")
        elif keys[pygame.K_3]:
            self.escenario = ("Fondos/fondo2.jpg")
        elif keys[pygame.K_4]:
            self.escenario = ("Fondos/fondo3.jpg")
        elif keys[pygame.K_5]:
            self.escenario = ("Fondos/fondo4.jpg")

        pygame.display.flip()
        pygame.time.wait(10)

    # Función principal del programa
def main():
    main_instance = Main()

    running = True
    while running:
        running = main_instance.handle_input()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        main_instance.draw()

    pygame.quit()

if __name__ == "__main__":
    main()
