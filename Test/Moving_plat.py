from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
##############################################
                # game Constant
##############################################
WINDOWS_WIDTH = 600
WINDOWS_HEIGHT = 800
INTERVAL = 200
###############################################
###############################################


##############################################
                # game states
##############################################
mouse_x = 0
###############################################
###############################################


def init():
    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WINDOWS_WIDTH, 0, WINDOWS_HEIGHT, 0, 1)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)


def game_timer(v):
    draw()
    print(v)
    glutTimerFunc(INTERVAL, game_timer, v+1)


def mouse_callback(x, y):
    pass


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3d(1, 0, 1)
    glScale(1, .4, 1)
    glRotate(90, 1, 0, 0)
    glutWireSphere(.2, 20, 20)
    glutSwapBuffers()


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(WINDOWS_WIDTH, WINDOWS_HEIGHT)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow(b"chess")
    glutDisplayFunc(draw)
    # glutTimerFunc(INTERVAL, game_timer, 1)
    init()
    # glutSpecialFunc(keyboard_callback)
    glutPassiveMotionFunc(mouse_callback)
    glutMainLoop()
