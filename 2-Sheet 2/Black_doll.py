from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *


def draw():
    glLineWidth(3)
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3d(0, 0, 0)
    """Body"""
    glBegin(GL_POLYGON)
    glVertex2d(0, .6)
    glVertex2d(.4, -.4)
    glVertex2d(-.4, -.4)
    glEnd()

    """Right led"""
    glBegin(GL_POLYGON)
    glVertex2d(.2, -.4)
    glVertex2d(.2, -.7)
    glVertex2d(.1, -.7)
    glVertex2d(.1, -.4)
    glEnd()

    """Left leg"""
    glBegin(GL_POLYGON)
    glVertex2d(-.2, -.4)
    glVertex2d(-.2, -.7)
    glVertex2d(-.1, -.7)
    glVertex2d(-.1, -.4)
    glEnd()

    """head"""
    # glColor3d(0, 0, 0)
    glBegin(GL_POLYGON)
    r = .18
    resolution = 1
    for angle in range(0, 360, resolution):
        x = r * cos(angle * pi / 180)
        y = r * sin(angle * pi / 180) + .55
        glVertex2d(x, y)
    glEnd()

    """Right hand"""
    glLineWidth(2)
    glBegin(GL_LINE_STRIP)
    glVertex2d(.12, .3)
    glVertex2d(.4, .1)
    glEnd()

    """Left hand"""

    glBegin(GL_LINE_STRIP)
    glVertex2d(-.12, .3)
    glVertex2d(-.4, .1)
    glEnd()
    glFlush()


glutInit()
glutInitWindowSize(500, 500)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(1000, 100)
glutCreateWindow(b"White doll")
glutDisplayFunc(draw)
glutMainLoop()
