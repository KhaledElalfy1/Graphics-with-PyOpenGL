from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#####################################
#####################################
#############gameconstant############
WINDOWS_WIDTH = 800
WINDOWS_HEIGHT = 800
cell = 64
INTERVAL = 200
#####################################
#####################################


def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WINDOWS_WIDTH, 0, WINDOWS_HEIGHT, 0, 1)
    glMatrixMode(GL_MODELVIEW)


def game_timer(v):
    draw()
    print(v)
    glutTimerFunc(INTERVAL, game_timer, 1)


i = 100
j = 100
k = 0
w = 0
flag = True


def draw_board():
    global i, j, k, w, flag
    for _ in range(78):
        glBegin(GL_QUADS)
        if flag:
            glColor(1, 1, 1)
        else:
            glColor(0, 0, 0)
        glVertex2f(k * i, w * j)
        glVertex2f((k+1) * i, w * j)
        glVertex2f((k + 1) * i, (w + 1) * j)
        glVertex2f(k * i, (w + 1) * j)
        glEnd()
        if k > 8:
            k = 0
            w += 1
        else:
            k += 1
            flag = not flag

    i = 100
    j = 100
    k = 0
    w = 0
    flag = True


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_board()
    glutSwapBuffers()


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(WINDOWS_WIDTH, WINDOWS_HEIGHT)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow(b"chess")
    glutDisplayFunc(draw)
    glutTimerFunc(INTERVAL, game_timer, 1)
    init()
    # glutSpecialFunc(keyboard_callback)
    # glutPassiveMotionFunc(mouse_callback)
    glutMainLoop()
