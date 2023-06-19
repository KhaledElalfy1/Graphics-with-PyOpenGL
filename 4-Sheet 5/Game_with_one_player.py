from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# constant of the program
WINDOWS_WIDTH = 800
WINDOWS_HEIGHT = 500
INTERVAL = 10
current_pc_result = 0
current_player_result = 0
FONT_DOWNSCALE = 0.13
##################################################
# ######### keyboard and mouse###########
##################################################


def keyboard_callback(key, x, y):
    if key == b"q":
        sys.exit(0)


def mouse_callback(x, y):
    global current_mouse_x
    current_mouse_x = x
##################################################
##################################################
# ### TIMER ####


def game_timer(v):
    draw()
    print(v)
    glutTimerFunc(INTERVAL, game_timer, 1)
##################################################
##################################################
# initialise windows


def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WINDOWS_WIDTH, 0, WINDOWS_HEIGHT, 0, 1)
    glMatrixMode(GL_MODELVIEW)
##################################################
##################################################


def draw_text(String, x, y):
    glLineWidth(1)
    glColor(1, 0, 1)
    glPushMatrix()
    glTranslate(x, y, 0)
    glScale(FONT_DOWNSCALE, FONT_DOWNSCALE, 1)
    String = String.encode()
    for c in String:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)
    glPopMatrix()


class Rectangle:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom


def draw_rectangle(rect):
    glLoadIdentity()
    glBegin(GL_QUADS)
    glVertex(rect.left, rect.bottom, 0)
    glVertex(rect.right, rect.bottom, 0)
    glVertex(rect.right, rect.top, 0)
    glVertex(rect.left, rect.top, 0)
    glEnd()
############################################


current_delta_x = 1
current_delta_y = 1
currentball = Rectangle(140, 140, 160, 160)
current_player = Rectangle(0, 0, 60, 10)
current_mouse_x = 0
#############################################


def draw():
    global current_delta_y, current_delta_x, current_pc_result, current_player_result
    glClear(GL_COLOR_BUFFER_BIT)
    String = 'pc: ' + str(current_pc_result)
    draw_text(String, 10, 440)
    String = 'player: ' + str(current_player_result)
    draw_text(String, 10, 400)
    currentball.left += current_delta_x
    currentball.right += current_delta_x
    currentball.bottom += current_delta_y
    currentball.top += current_delta_y
    glColor(1, 1, 1)
    draw_rectangle(currentball)

    if currentball.top == WINDOWS_HEIGHT:
        current_delta_y = -1
    if currentball.bottom == 0:
        current_delta_y = 1
        current_pc_result += 1
    if currentball.right == WINDOWS_WIDTH:
        current_delta_x = -1
    if currentball.left == 0:
        current_delta_x = 1
    current_player.left = current_mouse_x - 50
    current_player.right = current_mouse_x + 50
    draw_rectangle(current_player)
    if currentball.bottom == current_player.top and \
            current_player.left <= currentball.left <= currentball.right <= current_player.right:
        current_delta_y = 1
        current_player_result += 1
    # if current_player_result ==2:
    #     current_delta_y += 1
    #     current_delta_x += 1
    ########################
    glutSwapBuffers()


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(WINDOWS_WIDTH, WINDOWS_HEIGHT)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow(b"Game with one player")
    glutDisplayFunc(draw)
    glutTimerFunc(INTERVAL, game_timer, 1)
    init()
    glutKeyboardFunc(keyboard_callback)
    glutPassiveMotionFunc(mouse_callback)

    glutMainLoop()
