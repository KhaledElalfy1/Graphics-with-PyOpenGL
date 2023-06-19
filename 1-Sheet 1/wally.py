from OpenGL.GL import *
from OpenGL.GLUT import *

def draw():
    glColor3d(1, 0, 1)
    """Head"""
    glBegin(GL_POLYGON)
    glVertex2d(.375, .5)
    glVertex2d(.375, .75)
    glVertex2d(-.375, .75)
    glVertex2d(-.375, .5)
    glEnd()

    """Nick"""
    glBegin(GL_POLYGON)
    glVertex2d(.125, .25)
    glVertex2d(.125, .5)
    glVertex2d(-.125, .5)
    glVertex2d(-.125, .25)
    glEnd()

    """Body"""

    glBegin(GL_POLYGON)
    glVertex2d(.75, .25)
    glVertex2d(-.75, .25)
    glVertex2d(-.75, -.5)
    glVertex2d(.75, -.5)
    glEnd()

    """Right Leg"""
    glBegin(GL_POLYGON)
    glVertex2d(.75, -.5)
    glVertex2d(.5, -.5)
    glVertex2d(.5, -.9)
    glVertex2d(.75, -.9)
    glEnd()

    """Left Leg"""
    glBegin(GL_POLYGON)
    glVertex2d(-.75, -.5)
    glVertex2d(-.5, -.5)
    glVertex2d(-.5, -.9)
    glVertex2d(-.75, -.9)
    glEnd()
    """Right Hand"""
    glBegin(GL_LINE_STRIP)
    glVertex2d(.75, .125)
    glVertex2d(.9, -.4)
    glEnd()

    """Left Hand"""
    glBegin(GL_LINE_STRIP)
    glVertex2d(-.75, .125)
    glVertex2d(-.9, -.4)
    glEnd()

    glFlush()

glutInit()

glutInitWindowSize(500, 500)
glutInitWindowPosition(1000, 100)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"My wally")
glutDisplayFunc(draw)
glutMainLoop()
