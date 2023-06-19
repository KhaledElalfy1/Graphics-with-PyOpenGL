from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def initprojection_and_camera():
    x = 9
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 1, 30)
    # glOrtho(-20, 20, -20, 20, -20, 20)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(
        9, 9, 9,
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


angle = 0
shift = 3
unshift = 1
down = True
up = True
teapotangle = 0


def draw():
    global angle, shift, unshift, down, up, teapotangle
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glRotate(angle, 0, 1, 0)
    glPushMatrix()
    glColor3d(1, 1, 1)
    glRotate(90, 1, 0, 0)
    glutSolidCylinder(6, 7, 16, 8)
    glPopMatrix()
    ##################################

    # TODO draw teapot
    drawteapot(4, shift, 0, teapotangle)
    drawteapot(1.2, unshift, 3.8, teapotangle + 15)
    drawteapot(-3.2, shift, 2.3, teapotangle + 25)
    drawteapot(-3.2, unshift, -2.3, teapotangle + 35)
    drawteapot(1.2, shift, -3.8, teapotangle + 45)
    # TODO draw stick
    glColor3d(1, 0, 1)
    glPushMatrix()
    glTranslatef(4, shift / 2, 0)
    glRotatef(90, 0, 1, 0)
    # glutSolidCylinder(0.5, shift, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1.2, unshift / 2, 3.8)
    # glRotatef(90, 0, 1, 0)
    glutSolidCylinder(0.5, unshift, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-3.2, shift / 2, 2.3)
    # glRotatef(90, 0, 1, 0)
    glutSolidCylinder(0.5, shift, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-3.2, unshift / 2, -2.3)
    # glRotatef(90, 0, 1, 0)
    glutSolidCylinder(0.5, unshift, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1.2, shift / 2, -3.8)
    # glRotatef(90, 0, 1, 0)
    glutSolidCylinder(0.5, shift, 20, 20)
    glPopMatrix()

    glutSwapBuffers()
    angle += .00005
    teapotangle += 1
    shift = shift + (- .001 if down else +.001)
    if shift <= 1:
        down = False
    if shift >= 3:
        down = True
    unshift = unshift + (+.001 if up else -.001)
    if unshift >= 3:
        up = False
    if unshift <= 1:
        up = True



if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(500, 40)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow(b"Dancing teapot")
    initprojection_and_camera()
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()
