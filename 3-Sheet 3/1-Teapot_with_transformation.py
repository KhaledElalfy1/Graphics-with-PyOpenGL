from OpenGL.GL import *
from OpenGL.GLUT import *


def draw():
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3d(1, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    """ #Q1#
    glScale(3, 1, 1)
    glTranslate(0, -.7, 0)
    glRotate(120, 0, 0, 1)"""

    """ #Q2#
    glTranslate(0, -.7, 0)
    glRotate(120, 0, 0, 1)
    glScale(3, 1, 1)"""

    """ #Q3#"""
    glRotate(120, 0, 0, 1)
    glTranslate(0, -.7, 0)
    glScale(3, 1, 1)

    glutWireTeapot(.1)
    glFlush()


glutInit()
glutInitWindowSize(500, 500)
glutInitWindowPosition(1000, 100)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"Teapot Transformations")
glutDisplayFunc(draw)
glutMainLoop()
