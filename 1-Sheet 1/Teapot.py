from OpenGL.GL import *
from OpenGL.GLUT import *


def draw():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3d(1, 0, 1)
    glutWireTeapot(.5)
    glFlush()


glutInit()
glutInitWindowSize(500, 500)
glutInitWindowPosition(1000, 100)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"Teapot")
glutDisplayFunc(draw)
glutMainLoop()
