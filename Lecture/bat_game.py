from OpenGL.GL import *
from OpenGL.GLUT import *
import pygame

# TODO define game constant
INTERVAL = 10
WINDOWS_WIDTH = 500
WINDOWS_HEIGHT = 600
texture_names = [0, 1, 2]


#TODO texture
def texture_setup(texture_image_binary, texture_name, width, height):
    # TODO step[5] active a cirtin image
    glBindTexture(GL_TEXTURE_2D, texture_name)
    # TODO step[6] set texture parameters
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T,  GL_REPEAT)  # GL_MIRRORED_REPEAT , GL_CLAMP_TO_EDGE, GL_CLAMP_TO_BORDER
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    # TODO step[7] texture init
    glTexImage2D(GL_TEXTURE_2D,
                 0,  # mipmap
                 3,  # Bytes per pixel
                 width, height,
                 0,  # Texture border
                 GL_RGBA,  # RGBA Exactly as in  pygame.image.tostring(image, "RGBA", True)
                 GL_UNSIGNED_BYTE,
                 texture_image_binary)


def loadTextures():
    # TODO Step[1] Enable Texture
    glEnable(GL_TEXTURE_2D)  # [1]
    images = []
    # TODO Step[2] load image to programme
    images.append(pygame.image.load("ball.jpg"))
    images.append(pygame.image.load("chess.png"))
    images.append(pygame.image.load("wood.jpg"))
    # TODO Step[3] convert images to string
    textures = [pygame.image.tostring(image, 'RGBA', True) for image in images]
    # TODO Step[4] make id for each image
    glGenTextures(len(images), texture_names)  # size of two lists should be the same

    for i in range(len(images)):
        texture_setup(textures[i],  # binary images
                      texture_names[i],  # identifiers
                      images[i].get_width(),
                      images[i].get_height())
# TODO class of objects
class Rectangle:
    def __init__(self, left, top, right, bottom):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom


# TODO function to draw Rectangle objects
def draw_rectangle(rectangle, i):
    glLoadIdentity()
    glBindTexture(GL_TEXTURE_2D, texture_names[i])
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex(rectangle.left, rectangle.bottom, 0)

    glTexCoord2f(1, 0)
    glVertex(rectangle.right, rectangle.bottom, 0)

    glTexCoord2f(1, 1)
    glVertex(rectangle.right, rectangle.top, 0)

    glTexCoord2f(0, 1)
    glVertex(rectangle.left, rectangle.top, 0)
    glEnd()


# TODO define state variables
ball = Rectangle(280, 300, 300, 280)
player = Rectangle(0, 25, 60, 0)
Secene = Rectangle(0, WINDOWS_HEIGHT, WINDOWS_WIDTH, 0)
current_mouse = 0
delta_x = 1.5
delta_y = 1.5
current_pc_result = 0
current_player_result = 0


def init():
    glClearColor(0, 0, 0, 0)
    loadTextures()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WINDOWS_WIDTH, 0, WINDOWS_HEIGHT, 0, 1)
    glMatrixMode(GL_MODELVIEW)


def keyboard(key, x, y):
    if key == b'q':
        sys.exit(0)


def mouse(x, y):
    global current_mouse
    current_mouse = x


def timer(v):
    draw()
    print(v)
    glutTimerFunc(INTERVAL, timer, 1)


def draw_text(string, x, y):
    glDisable(GL_BLEND)
    glLineWidth(1)
    glColor(0, 0, 1)
    glPushMatrix()
    glTranslate(x, y, 0)
    glScale(.13, .13, 1)
    string = string.encode()
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)

    glPopMatrix()
    glEnable(GL_BLEND)


def draw():
    global current_mouse, delta_x, delta_y, current_pc_result, current_player_result
    glClear(GL_COLOR_BUFFER_BIT)
    """string = 'pc: ' + str(current_pc_result)
    draw_text(string, 10, 540)
    string = 'player: ' + str(current_player_result)
    draw_text(string, 10, 500)"""
    # glColor3d(1, 1, 1)
    draw_rectangle(Secene, 1)
    string = 'pc: ' + str(current_pc_result)
    draw_text(string, 10, 540)
    string = 'player: ' + str(current_player_result)
    draw_text(string, 10, 500)
    glColor3d(1, 1, 1)
    # TODO move and create ball
    ball.left += delta_x
    ball.right += delta_x
    ball.top += delta_y
    ball.bottom += delta_y
    draw_rectangle(ball, 0)
    # TODO move and create player
    player.left = current_mouse - 60
    player.right = current_mouse + 60
    draw_rectangle(player, 2)
    glutSwapBuffers()
    if ball.left <= 0 or ball.right >= WINDOWS_WIDTH:
        delta_x = -delta_x
    if ball.top >= WINDOWS_HEIGHT or ball.bottom <= 0:
        if delta_y < 0:
            current_pc_result += 1

        delta_y = -delta_y
    if ball.bottom == player.top and player.left <= ball.left <= ball.right <= player.right:
        delta_y = -delta_y
        current_player_result += 1


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(WINDOWS_WIDTH, WINDOWS_HEIGHT)
    glutInitWindowPosition(500, 100)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow(b'bat ball')
    glutDisplayFunc(draw)
    glutTimerFunc(INTERVAL, timer, 1)
    init()
    glutKeyboardFunc(keyboard)
    glutPassiveMotionFunc(mouse)
    glutMainLoop()
