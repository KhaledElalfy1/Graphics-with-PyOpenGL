from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *


INTERVAL = 10


def draw_axis():
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3d(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(5, 0, 0)

    glColor3d(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 5, 0)

    glColor3d(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 5)
    glEnd()


def init():
    look = 12
    glClearColor(0, 0, 0, 0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, .1, 30)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(
        look, look, look,
        0, 0, 0,
        0, 1, 0
    )


def init_light0():
    glEnable(GL_LIGHT0)
    LightPos = [0, 0, 0, 1]
    LightAmp = [.3, .3, 0, 1]  # r g b alpha
    LightDif = [3, 3, 0, 1]
    LightSpe = [1, 1, 1, 1]

    glLight(GL_LIGHT0, GL_POSITION, LightPos)
    glLight(GL_LIGHT0, GL_AMBIENT, LightAmp)
    glLight(GL_LIGHT0, GL_DIFFUSE, LightDif)
    glLight(GL_LIGHT0, GL_SPECULAR, LightSpe)


def draw_circle(radis):
    resolution = 1
    MaterialAmp = [.5, .5, 0.5, 1]
    MaterialDif = [0, 0, 0, 1]
    MaterialSpe = [0, 0, 0, 1]
    MaterialShn = [128]
    glMaterial(GL_FRONT, GL_AMBIENT, MaterialAmp)
    glMaterial(GL_FRONT, GL_DIFFUSE, MaterialDif)
    glMaterial(GL_FRONT, GL_SPECULAR, MaterialSpe)
    glMaterial(GL_FRONT, GL_SHININESS, MaterialShn)
    glBegin(GL_LINE_LOOP)
    for i in range(0, 360, resolution):
        x = radis * cos(i * pi/180)
        z = radis * sin(i * pi/180)
        glVertex3f(x, 0, z)
    glEnd()


def draw_planet(radis, shift, rotate, r, g, b):
    # glRotate(rotate, 0, 1, 0)
    glPushMatrix()
    MaterialAmp = [r, g, b, 1]
    MaterialDif = [r, g, b, 1]
    MaterialSpe = [r, g, b, 1]
    MaterialShn = [128]
    glMaterial(GL_FRONT, GL_AMBIENT, MaterialAmp)
    glMaterial(GL_FRONT, GL_DIFFUSE, MaterialDif)
    glMaterial(GL_FRONT, GL_SPECULAR, MaterialSpe)
    glMaterial(GL_FRONT, GL_SHININESS, MaterialShn)
    glRotate(rotate, 0, 1, 0)
    glTranslate(shift, 0, 0)
    glutSolidSphere(radis, 100, 100)
    glPopMatrix()


def draw_sun(radis):
    MaterialAmp = [1, 1, 0, 1]
    MaterialDif = [3, 3, 0, 1]
    MaterialSpe = [1, 1, 1, 1]
    MaterialShn = [126]
    glMaterial(GL_FRONT, GL_AMBIENT, MaterialAmp)
    glMaterial(GL_FRONT, GL_DIFFUSE, MaterialDif)
    glMaterial(GL_FRONT, GL_SPECULAR, MaterialSpe)
    glMaterial(GL_FRONT, GL_SHININESS, MaterialShn)
    glutSolidSphere(radis, 100, 100)


rotate_angle = 0


def draw():
    global rotate_angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # draw_axis()
    # TODO the sun
    draw_sun(.5)
    glLineWidth(1)

    # TODO Draw orbit
    draw_circle(1.5)
    draw_circle(2.5)
    draw_circle(3.5)
    draw_circle(4.5)
    draw_circle(5.5)
    draw_circle(6.5)
    draw_circle(7.5)

    # TODO Start to draw planets
    # glRotate(rotate_angle, 0, 1, 0)

    # TODO first planet
    draw_planet(.3, 1.5, -rotate_angle, 1, .5, 1)

    # TODO second planet
    draw_planet(.4, 2.5, -rotate_angle-45, 1, 0, 1)

    # TODO third planet
    draw_planet(.3, 3.5, -rotate_angle+60, 0, 0, 1)

    # TODO fourth planet
    draw_planet(.4, 4.5, rotate_angle+45, 1, 0, .1)

    # TODO fifth planet
    draw_planet(.4, 5.5, rotate_angle+60, 1, 0.1, 0)

    # TODO sixth planet
    draw_planet(.4, 6.5, rotate_angle-90, 1, 1, 0.1)

    # TODO seventh planet
    draw_planet(.4, 7.5, rotate_angle, 1, 0.5, 0.1)

    glutSwapBuffers()
    rotate_angle += 1


def game_timer(v):
    draw()
    # print(v)
    glutTimerFunc(INTERVAL, game_timer, 1)


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(800, 800)
    glutCreateWindow(b"Solar one")
    init()
    init_light0()
    glutDisplayFunc(draw)
    glutTimerFunc(INTERVAL, game_timer, 1)
    glutMainLoop()
