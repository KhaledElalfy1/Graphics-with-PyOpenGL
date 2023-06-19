from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *
def draw():
    glColor3d(1, 1, 1)

    """ Face """
    glBegin(GL_LINE_LOOP)
    r1 = .8
    resolution=1
    for angle in range(0,360,resolution):
        x = r1 * cos(angle * pi / 180)
        y = r1 * sin(angle * pi / 180)
        glVertex2d(x, y)
    glEnd()
    """ nose"""
    glBegin(GL_LINE_LOOP)
    r1 = .05
    resolution = 1
    for angle in range(0, 360, resolution):
        x = r1 * cos(angle * pi / 180)
        y = r1 * sin(angle * pi / 180) - .2
        glVertex2d(x, y)
    glEnd()
    """muse"""
    glBegin(GL_LINE_STRIP)
    r1 = .15
    resolution = 1
    for angle in range(180, 360, resolution):
        x = r1 * cos(angle * pi / 180)
        y = r1 * sin(angle * pi / 180) - .4
        glVertex2d(x, y)
    glEnd()

    """Right eye"""
    glBegin(GL_LINE_LOOP)
    r1 = .05
    resolution = 1
    for angle in range(0, 360, resolution):
        x = r1 * cos(angle * pi / 180) + .27
        y = r1 * sin(angle * pi / 180) + .3
        glVertex2d(x, y)
    glEnd()

    """Left eye"""
    glBegin(GL_LINE_LOOP)
    r1 = .05
    resolution = 1
    for angle in range(0, 360, resolution):
        x = r1 * cos(angle * pi / 180) - .27
        y = r1 * sin(angle * pi / 180) + .3
        glVertex2d(x, y)
    glEnd()
    glFlush()


glutInit()
glutInitWindowSize(500, 500)
glutInitWindowPosition(1000, 100)
glutCreateWindow(b"Face")
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutDisplayFunc(draw)
glutMainLoop()
