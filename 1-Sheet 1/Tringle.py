from OpenGL.GL import *
from OpenGL.GLUT import *


def draw():
    glColor3d(1, 1, 0)
    glBegin(GL_POLYGON)
    glVertex2d(-.5, -.5)
    glVertex2d(.5, -.5)
    glVertex2d(.5, .5)
    glEnd()
    glColor3d(0, 0, 1)
    glBegin(GL_POLYGON)
    glVertex2d(0.5, 0.5)
    glVertex2d(-0.5, 0.5)
    glVertex2d(-.5, -.5)
    glEnd()
    glFlush()
    print("Hi حمزه")


glutInit()
glutInitWindowSize(500, 500)
glutInitWindowPosition(1000, 100)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"My frist draw")
glutDisplayFunc(draw)
glutMainLoop()
