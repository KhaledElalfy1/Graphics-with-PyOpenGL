from OpenGL.GL import *
from OpenGL.GLUT import *

RotationAngle = 40


def draw():
    global RotationAngle
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3d(0, .8, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()  # TODO: Tray comment this
    glRotate(RotationAngle, 0, 0, 1)
    glBegin(GL_POLYGON)
    glVertex2d(-.5, -.5)
    glVertex2d(.5, -.5)
    glVertex2d(.5, .5)
    glVertex2d(-.5, .5)
    glEnd()
    glutSwapBuffers()

    RotationAngle += .01


glutInit()
glutInitWindowSize(500, 500)
glutInitWindowPosition(1000, 100)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow(b"Square Motion")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
