from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def initprojection():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(20, 1, 1, 30)
    glMatrixMode(GL_MODELVIEW)


def reposition_camera():
    # gluLookAt(
    #     0, 0, 20,  # Eye
    #     0, 0, 0,   # center
    #     0, 1, 0
    # )
    ######################
    gluLookAt(
        15, 15, 15,  # Eye
        0, 0, 0,  # center
        0, 1, 0
    )


def drawaxis():

    glBegin(GL_LINES)
    # TODO: to draw x-axis
    glColor3d(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(100, 0, 0)

    # TODO: to draw y-axis
    glColor3d(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 100, 0)

    # TODO: to draw z-axis
    glColor3d(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 100)
    glEnd()


def draw_wheel(x_loc, y_loc, z_loc):
    glLoadIdentity()
    reposition_camera()
    glTranslatef(x_loc, y_loc, z_loc)
    glutWireTorus(.15, .35, 10, 12)


def draw_bulbs(x_loc, y_loc, z_loc):
    glLoadIdentity()
    reposition_camera()
    glTranslate(x_loc, y_loc, z_loc)
    glScale(.2, 3, 3)
    glutWireSphere(.1, 20, 20)


def draw():
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    reposition_camera()
    drawaxis()
    # TODO draw the bottom cube
    glColor3f(1, 0, 0)
    glLoadIdentity()
    reposition_camera()
    glScale(4, 1, 2)
    glutWireCube(1)
    # TODO draw the upper cube
    glLoadIdentity()
    reposition_camera()
    glTranslatef(0, .85, 0)  # to put the cube above of the lower cube
    glScale(3, 1, 2)
    glutWireCube(.7)

    glColor3d(0, 0, 1)
    draw_wheel(2, -.5, 1)  # TODO the front left wheel
    draw_wheel(2, -.5, -1)  # TODO the front right wheel
    draw_wheel(-2, -.5, -1)  # TODO the back right wheel
    draw_wheel(-2, -.5, 1)  # TODO the back right wheel
    # glutWireTeapot(.2)
    # TODO draw bulbs
    glColor3d(1, 1, 0)
    draw_bulbs(2, 0.05, .5)  # TODO left bulb
    draw_bulbs(2, 0.05, -.5)  # TODO right bulb
    ############
    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(500, 50)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow(b"3D Car")
    initprojection()
    glutDisplayFunc(draw)
    glutMainLoop()
