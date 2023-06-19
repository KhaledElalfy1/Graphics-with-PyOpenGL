from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *
import numpy as np

XLimit = 4
YLimit = 4


def drawaxis():
    glLineWidth(2)
    glColor3d(1, 0, 0)  # x-axis
    glBegin(GL_LINES)
    glVertex2d(-4, 0)
    glVertex2d(4, 0)
    glEnd()
    glColor3d(0, 1, 0)
    glBegin(GL_LINES)
    glVertex2d(0, 4)
    glVertex2d(0, -4)
    glEnd()


def draw():
    glLineWidth(3)
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-XLimit, XLimit, -YLimit, YLimit)
    glColor3d(0, 0, 0)
    glBegin(GL_LINE_STRIP)
    a = .5
    freq = 2
    resolution = .001
    for x in np.arange(0, XLimit, resolution):
        y = a * sin(2 * np.pi * freq * x)
        glVertex2d(x, y)
    glEnd()
    drawaxis()
    glFlush()


glutInit()
glutInitWindowSize(500, 500)
glutInitWindowPosition(1000, 100)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"sine wave")
glutDisplayFunc(draw)
glutMainLoop()
