from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *

def init():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # gluPerspective(45, 1, 1, 100)
    glMatrixMode(GL_MODELVIEW)
    # gluLookAt(
    #     10, 10, 10,
    #     0, 0, 0,
    #     0, 1, 0
    # )


scale = 1
touch = 1


# def draw_circle(r1):
#     global scale, touch
#
#     resolution = 1
#     glBegin(GL_LINE_LOOP)
#     for angle in range(0, 360, resolution):
#         x = r1 * cos(angle * pi / 180)
#         y = r1 * sin(angle * pi / 180)
#         glVertex2d(x, y)
#     glEnd()


def draw():
    global scale, touch
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glColor3d(1, 0, 1)
    glScale(scale, scale, scale)
    glutSolidSphere(.1, 100, 100)
    glutSwapBuffers()
    if scale < 1:
        touch = 1
    if scale > 10:
        touch = 0
    if touch:
        scale += .001
    else:
        scale -= .001


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(500, 50)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow(b"ball motion")
    init()
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()
