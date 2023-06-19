from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *


def draw():
    glMatrixMode()
    glColor3d(1, 1, 0)
    glBegin(GL_LINE_LOOP)
    r1 = .9
    resolution = 1
    for angle in range(0, 360, resolution):
        x = r1 * cos(angle * pi/180)
        y = r1 * sin(angle * pi/180)
        glVertex2d(x, y)
    glEnd()
    glColor3d(1, .5, 0)

    glBegin(GL_LINE_LOOP)
    r2 = .7
    resolution = 1
    for angle in range(0, 360, resolution):
        x = r2 * cos(angle * pi / 180)
        y = r2 * sin(angle * pi / 180)
        glVertex2d(x, y)
    glEnd()
    glFlush()


glutInit()
glutInitWindowSize(500, 500)
glutInitWindowPosition(1000, 100)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"My circle")
glutDisplayFunc(draw)
glutMainLoop()
