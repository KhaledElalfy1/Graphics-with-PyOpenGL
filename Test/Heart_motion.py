from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *

INTERVAL = 1


def draw_heart():
    resolution = 1
    glBegin(GL_LINE_LOOP)
    for i in range(0, 360, resolution):
        x = .5 * sin(i * pi / 180)**3
        y = 0.40625*cos(i * pi / 180) - 0.15625*cos((2*i) * pi / 180) - 0.0625 * cos((3*i) * pi / 180) - 0.03125 * cos((4 * i) * pi / 180)
        glVertex2d(x, y)
    glEnd()


rotate = 45


def game_timer(v):
    draw()
    print(v)
    glutTimerFunc(INTERVAL, game_timer, 1)


def draw():
    global rotate
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3d(0, 0, 0)
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2d(.25, .2)
    glEnd()
    glColor3d(1, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslate(.25, .2, 0)
    glRotate(rotate, 0, 0, 1)
    glTranslate(-.25, -.2, 0)
    draw_heart()
    glutSwapBuffers()
    rotate += .1


glutInit()
glutInitWindowSize(800, 800)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow(b"heart")
glutDisplayFunc(draw)
glutTimerFunc(INTERVAL, game_timer, 1)
glutMainLoop()
