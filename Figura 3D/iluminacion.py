from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *

iluminacion_activada = True

def toggle_iluminacion():
    global iluminacion_activada
    iluminacion_activada = not iluminacion_activada

    if iluminacion_activada:
        glEnable(GL_LIGHTING)
    else:
        glDisable(GL_LIGHTING)

def iluminacion(R, G, B):
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    glEnable(GL_LIGHT2)
    glEnable(GL_LIGHT3)
    glEnable(GL_DEPTH_TEST)

    # Light properties
    light_ambient = (0.0, 0.0, 0.0, 1.0)
    light_diffuse = (R, G, B, 1.0)

    # Set up light 0 (frontal light)
    glLightfv(GL_LIGHT0, GL_POSITION, (0.0, 10.0, 30.0, 1.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)

    # Set up light 1 (rear light)
    glLightfv(GL_LIGHT1, GL_POSITION, (0.0, 10.0, -30.0, 1.0))
    glLightfv(GL_LIGHT1, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light_diffuse)

    # Set up light 2 (left light)
    glLightfv(GL_LIGHT2, GL_POSITION, (-30.0, 10.0, 20.0, 1.0))
    glLightfv(GL_LIGHT2, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, light_diffuse)

    # Set up light 3 (right light)
    glLightfv(GL_LIGHT3, GL_POSITION, (30.0, 10.0, 20.0, 1.0))
    glLightfv(GL_LIGHT3, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT3, GL_DIFFUSE, light_diffuse)

    # Material properties
    material_ambient = (0.2, 0.2, 0.2, 1.0)
    material_diffuse = (R, G, B, 1.0)
    material_specular = (1.0, 1.0, 1.0, 1.0)

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, material_ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, material_diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, material_specular)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, 50.0)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(1.0, 1.0, 1.0)
    glutSolidTeapot(1.0)
    glutSwapBuffers()

