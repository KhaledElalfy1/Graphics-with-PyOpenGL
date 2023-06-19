from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *


def draw():
    x_loc = [4.0, 1.2360679774997898, -3.2360679774997894, -3.23606797749979, 1.236067977499789]
    y_loc = [0.0, 3.804226065180614, 2.351141009169893, -2.351141009169892, -3.8042260651806146]
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-7, 7, -7, 7)
    glColor3d(1, 1, 1)
    glBegin(GL_LINE_LOOP)
    r2 = 6
    resolution = 1
    for angle in range(0, 360, resolution):
        x = r2 * cos(angle * pi / 180)
        y = r2 * sin(angle * pi / 180)
        glVertex2d(x, y)
    glEnd()
    glPointSize(7)
    glBegin(GL_POINTS)
    glColor3d(1, 0, 1)
    for i in range(5):
        glVertex2f(x_loc[i], y_loc[i])
    glEnd()
    glFlush()


glutInit()
glutInitWindowSize(500, 500)
glutInitWindowPosition(1000, 100)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"My circle")
glutDisplayFunc(draw)
glutMainLoop()
