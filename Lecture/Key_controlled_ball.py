from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


arange = 1
x = -.6
y = .4
radius = .1
anim = 0
delta_x = .001
delta_y = .001


def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-arange, arange, -arange, arange, -arange, arange)
    glMatrixMode(GL_MODELVIEW)


def draw():
    global x, y, anim, delta_y, delta_x
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glColor3d(0, 0, 1)
    glTranslate(x, y, -1)
    glutSolidSphere(radius, 100, 100)
    glutSwapBuffers()
    if anim:
        x += delta_x
        y += delta_y
        if radius + x > arange or x - radius < -arange:
            delta_x = -delta_x
        if y + radius > arange or y - radius < -arange:
            delta_y = -delta_y


def keyboard(key, x, y):
    global anim
    if key == b's':
        anim = 1
    if key == b'e':
        anim = 0
    if key == b'q':
        sys.exit(0)


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(1000, 100)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow(b'ball')
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    init()
    glutKeyboardFunc(keyboard)
    glutMainLoop()
