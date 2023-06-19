from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import Q1


def initprojection_and_cam():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -10, 10, -10, 10)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(
        2, 2, 2,
        0, 0, 0,
        0, 1, 0

    )


def draw_animated_wheel_Q4(x_loc, y_loc, z_loc, angle):
    glPushMatrix()
    glTranslatef(x_loc, y_loc, z_loc)
    glRotate(angle, 0, 0, -1)
    glutWireTorus(.15, .35, 10, 12)
    glPopMatrix()


def draw_bulbs_Q4(x_loc, y_loc, z_loc):
    glPushMatrix()
    glTranslate(x_loc, y_loc, z_loc)
    glScale(.2, 3, 3)
    glutWireSphere(.1, 20, 20)
    glPopMatrix()


def draw_car(angle):
    # TODO draw lower cube
    glColor3d(1, 0, 0)
    glPushMatrix()
    glScale(4, 1, 2)
    glutWireCube(1)
    glPopMatrix()
    # TODO draw upper cube
    glPushMatrix()
    glTranslatef(0, .85, 0)  # to put the cube above of the lower cube
    glScale(3, 1, 2)
    glutWireCube(.7)
    glPopMatrix()
    # TODO draw wheels
    glColor3d(0, 0, 1)
    draw_animated_wheel_Q4(2, -.5, 1, angle)  # TODO the front left wheel
    draw_animated_wheel_Q4(2, -.5, -1, angle)  # TODO the front right wheel
    draw_animated_wheel_Q4(-2, -.5, -1, angle)  # TODO the back right wheel
    draw_animated_wheel_Q4(-2, -.5, 1, angle)  # TODO the back right wheel
    # TODO draw bulbs
    glColor3d(1, 1, 0)
    draw_bulbs_Q4(2, 0.05, .5)  # TODO left bulb
    draw_bulbs_Q4(2, 0.05, -.5)  # TODO right bulb
    

angle = 0
forward = True
shift = 0


def draw():
    global angle, forward, shift
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    Q1.drawaxis()
    # TODO move forward and backward in x-axis
    glPushMatrix()
    glTranslate(shift, 0, 0)
    draw_car(angle)
    glPopMatrix()
    # TODO move forward and backward in y-axis
    glPushMatrix()
    glTranslate(0, shift, 0)
    glRotate(-90, 0, 0, -1)
    draw_car(angle)
    glPopMatrix()
    # TODO move forward and backward in z-axis
    glPushMatrix()
    glTranslate(0, 0, shift)
    glRotate(-90, 0, 1, 0)
    draw_car(angle)
    glPopMatrix()
    ###################
    glutSwapBuffers()
    shift = shift + (.01 if forward else -.01)
    angle = angle + (.01 if forward else -.01)
    if shift >= 9:
      forward = False

    if shift <= -9:
        forward = True


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(500, 50)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow(b"3D Car")
    initprojection_and_cam()
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()
