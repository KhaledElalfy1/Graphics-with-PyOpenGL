from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import randint
##############################
######### Game Costants ######
WINDOWS_WIDTH = 800
WINDOWS_HEIGHT = 800
INTERVAL = 200
cell = 15
TOP = (0, 1)
BOTTOM = (0, -1)
RIGHT = (1, 0)
LEFT = (-1, 0)
##############################
##############################
######### Game States ########
current_apple = randint(0, cell - 1), randint(0, cell - 1)
current_x = cell // 2
current_y = cell // 2
tail = [(current_x-2, current_y), (current_x-1, current_y), (current_x, current_y)]
current_delta = RIGHT
##############################
##############################


def init():
    glClearColor(1, 1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WINDOWS_WIDTH, 0, WINDOWS_HEIGHT, 0, 1)
    glMatrixMode(GL_MODELVIEW)


def draw_cell(x, y):
    cell_width = WINDOWS_WIDTH / cell
    cell_height = WINDOWS_HEIGHT / cell
    glBegin(GL_QUADS)
    glVertex2f(cell_width * x, cell_height * y)
    glVertex2f(cell_width * x, cell_height * (y + 1))
    glVertex2f(cell_width * (x + 1), cell_height * (y + 1))
    glVertex2f(cell_width * (x + 1), cell_height * y)
    glEnd()


def draw_apple():
    glColor(1, 0, 1)
    draw_cell(current_apple[0], current_apple[1])


def draw_snake():
    glColor(0, 1, 1)
    for cell_x, cell_y in tail:
        draw_cell(cell_x, cell_y)


def move_snake(_tail):
    current_x, current_y = _tail[-1]
    new_head = (current_x + current_delta[0]) % cell, (current_y + current_delta[1]) % cell
    _tail.append(new_head)
    _tail.pop(0)
    return _tail


def game_timer(v):
    draw()
    # print(v)
    glutTimerFunc(INTERVAL, game_timer, 1)


def keyboard_callback(key, x, y):
    global current_delta
    if key == GLUT_KEY_LEFT and current_delta != RIGHT:
        current_delta = LEFT
    elif key == GLUT_KEY_RIGHT and current_delta != LEFT:
        current_delta = RIGHT
    elif key == GLUT_KEY_UP and current_delta != BOTTOM:
        current_delta = TOP
    elif key == GLUT_KEY_DOWN and current_delta != TOP:
        current_delta = BOTTOM


def draw():
    global tail
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3d(1, 0, 1)
    draw_apple()
    draw_snake()
    tail = move_snake(tail)
    glutSwapBuffers()


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(WINDOWS_WIDTH, WINDOWS_HEIGHT)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow(b"Snake")
    glutDisplayFunc(draw)
    glutTimerFunc(INTERVAL, game_timer, 1)
    init()
    glutSpecialFunc(keyboard_callback)
    # glutPassiveMotionFunc(mouse_callback)
    glutMainLoop()
