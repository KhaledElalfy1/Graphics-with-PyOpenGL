from OpenGL.GL import *
from OpenGL.GLUT import *


def draw():
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3d(1, 0, 1)
    glBegin(GL_LINE_STRIP)
    glVertex2d(0, 1)
    glVertex2d(0, 0)
    glEnd()

    glColor3d(1, 1, 0)
    glBegin(GL_LINE_STRIP)
    glVertex2d(1, 0)
    glVertex2d(0, 0)
    glEnd()

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glRotate(-45, 0, 0, 1)
    glScale(1.5, 1, 1)
    glRotate(45, 0, 0, 1)
    glColor3d(0, 0, 1)
    glBegin(GL_POLYGON)
    glVertex2d(.2, -0.2)
    glVertex2d(-.2, -.2)
    glVertex2d(-.2, .2)
    glVertex2d(.2, .2)
    glEnd()

    glColor3d(1, 1, 0)
    glBegin(GL_POLYGON)
    glVertex2d(-.2, .2)
    glVertex2d(0, .5)
    glVertex2d(.2, .2)
    glEnd()
    glFlush()


glutInit()
glutInitWindowSize(500, 500)
glutInitWindowPosition(1000, 100)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"Home Transformations")
glutDisplayFunc(draw)
glutMainLoop()
