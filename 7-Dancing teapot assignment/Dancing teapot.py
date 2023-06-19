from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def initprojection_and_camera():
    x = 9
    # NOTE: (9,9,9) to make cylinder be good
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 1, 30)
    # glOrtho(-20, 20, -20, 20, -20, 20)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(
        x, x, x,
        0, 0, 0,
        0, 1, 0
    )


def drawteapot(x_loc, y_loc, z_loc, rotation):
    glLineWidth(1)
    glPushMatrix()
    glColor3d(1, 0, 1)

    glTranslate(x_loc, y_loc, z_loc)
    glRotate(rotation, 0, 1, 0)
    glutWireTeapot(1.3)
    glPopMatrix()


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


angle = 0
shift = 3
down = True
teapotangle = 0


def draw():
    global angle, shift, down, teapotangle
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    drawaxis()
    glRotate(angle, 0, 1, 0)
    glPushMatrix()
    glColor3d(1, 1, 1)
    glRotate(90, 1, 0, 0)
    glutSolidCylinder(6, 7, 16, 8)
    glPopMatrix()
    ##################################

    # TODO first teapot and stick
    # glRotate(teapotangle, 0, 1, 0)
    glPushMatrix()
    # glRotate(teapotangle, 0, 1, 0)
    drawteapot(4, shift, 0, teapotangle)
    glLineWidth(40)
    glBegin(GL_LINES)
    glColor3d(1, 0, 1)
    glVertex3f(4, 0, 0)
    glVertex3f(4, shift, 0)
    glEnd()

    # TODO Second teapot and stick

    # glRotate(teapotangle, 0, 1, 0)
    drawteapot(-4, shift, 0, teapotangle)
    glLineWidth(40)
    glBegin(GL_LINES)
    glColor3d(1, 0, 1)
    glVertex3f(-4, 0, 0)
    glVertex3f(-4, shift, 0)
    glEnd()

    # TODO third teapot and stick
    # glRotate(teapotangle, 0, 1, 0)
    drawteapot(-.5, shift, 5, teapotangle)
    glLineWidth(40)
    glBegin(GL_LINES)
    glColor3d(1, 0, 1)
    glVertex3f(-.5, 0, 5)
    glVertex3f(-.5, shift, 5)
    glEnd()

    # TODO fourth teapot and stick
    # glRotate(teapotangle, 0, 1, 0)
    drawteapot(.5, shift, -5, teapotangle)
    glLineWidth(40)
    glBegin(GL_LINES)
    glColor3d(1, 0, 1)
    glVertex3f(.5, 0, -5)
    glVertex3f(.5, shift, -5)
    glEnd()

    # TODO fifth teapot and stick
    # glRotate(teapotangle, 0, 1, 0)
    drawteapot(3, shift, 4, teapotangle)
    glLineWidth(40)
    glBegin(GL_LINES)
    glColor3d(1, 0, 1)
    glVertex3f(3, 0, 4)
    glVertex3f(3, shift, 4)
    glEnd()
    glPopMatrix()

    ###################
    glutSwapBuffers()
    angle += .00001
    teapotangle += .00001
    shift = shift + (- .001 if down else +.001)
    if shift <= 1:
        down = False
    if shift >= 3:
        down = True


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(500, 40)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow(b"cylinder")
    initprojection_and_camera()
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()
