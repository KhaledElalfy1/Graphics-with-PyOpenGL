from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import Q2
import Q1

def initprojection_Q3():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -10, 10, -10, 10)
    glMatrixMode(GL_MODELVIEW)


def reposition_camera_Q3():
    gluLookAt(
        2, 2, 2,
        0, 0, 0,
        0, 1, 0

    )


def draw_animated_wheel_Q3(x_loc, y_loc, z_loc, angle):
    glLoadIdentity()
    reposition_camera_Q3()
    glTranslate(shift, 0, 0)
    glTranslatef(x_loc, y_loc, z_loc)
    glRotate(angle, 0, 0, -1)
    glutWireTorus(.15, .35, 10, 12)

def draw_bulbs_Q3(x_loc, y_loc, z_loc):
    glLoadIdentity()
    reposition_camera_Q3()
    glTranslate(shift, 0, 0)
    glTranslate(x_loc, y_loc, z_loc)
    glScale(.2, 3, 3)
    glutWireSphere(.1, 20, 20)


angle = 0
forward = True
shift = 0


def draw():
    global angle, forward, shift
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    reposition_camera_Q3()
    Q1.drawaxis()

    # TODO draw and translate top cube
    glTranslate(shift, 0, 0)
    glScale(4, 1, 2)
    glColor3d(1, 0, 0)
    glutWireCube(1)
    glLoadIdentity()
    reposition_camera_Q3()
    # TODO draw and translate lower cube
    glTranslate(shift, 0, 0)
    glTranslatef(0, .85, 0)  # to put the cube above of the lower cube
    glScale(3, 1, 2)
    glutWireCube(.7)

    # TODO draw and rotate wheels

    glColor3d(0, 0, 1)
    draw_animated_wheel_Q3(2, -.5, 1, angle)  # TODO the front left wheel
    draw_animated_wheel_Q3(2, -.5, -1, angle)  # TODO the front right wheel
    draw_animated_wheel_Q3(-2, -.5, -1, angle)  # TODO the back right wheel
    draw_animated_wheel_Q3(-2, -.5, 1, angle)  # TODO the back right wheel

    # TODO draw bulbs
    glColor3d(1, 1, 0)
    draw_bulbs_Q3(2, 0.05, .5)  # TODO left bulb
    draw_bulbs_Q3(2, 0.05, -.5)  # TODO right bulb

    glutSwapBuffers()

    shift = shift + (.01 if forward else -.01)
    angle = angle + (.01 if forward else -.01)
    if shift >= 3:
      forward = False

    if shift <= -3:
        forward = True


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(500, 50)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow(b"3D Car")
    initprojection_Q3()
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()
