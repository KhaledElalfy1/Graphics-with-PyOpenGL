from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def init_my_sence(width, height):
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, float(width) / float(height), .1, 100)  # gluPerspective(Fovy,aspect ratio,zNear,zFar)
    glMatrixMode(GL_MODELVIEW)  # to draw and do what ever I want


def drawcube(x, y, z, l):
    #  TODO: draw the lower level 1,2,3,4
    glColor3d(1, 0, 0)
    glLineWidth(2)
    glBegin(GL_LINE_LOOP)
    glVertex3f(x, y, z)
    glVertex3f(x, y+l, z)
    glVertex3f(x+l, y+l, z)
    glVertex3f(x+l, y, z)
    glEnd()
    #  TODO: draw the upper level 5,6,7,8
    glColor3d(0, 0, 1)
    glLineWidth(2)
    glBegin(GL_LINE_LOOP)
    glVertex3f(x, y, z+l)
    glVertex3f(x, y + l, z+l)
    glVertex3f(x + l, y + l, z+l)
    glVertex3f(x + l, y, z+l)
    glEnd()
    #  TODO: draw lines connect (1,5), (2,6), (3,7), (4,8)
    glColor3d(1, 1, 0)
    glBegin(GL_LINES)
    glVertex3f(x, y, z)
    glVertex3f(x, y, z + l)
    glEnd()
    #######
    glColor3d(1, 0, 1)
    glBegin(GL_LINES)
    glVertex3f(x, y+l, z)
    glVertex3f(x, y+l, z+l)
    glEnd()
    ########
    glColor3d(0, 1, 1)
    glBegin(GL_LINES)
    glVertex3f(x + l, y + l, z)
    glVertex3f(x + l, y + l, z+l)
    glEnd()
    ########
    glColor3d(0, 1, 0)
    glBegin(GL_LINES)
    glVertex3f(x+l, y, z)
    glVertex3f(x+l, y, z + l)
    glEnd()


angle = 0


def draw():
    global angle
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    # TODO: draw and rotate first cube around x-axis
    glTranslatef(0, 0, -5)
    glRotate(angle, 1, 0, 0)  # Rotate around x-axis
    drawcube(-1, -1, -1, 2)

    # TODO: draw and rotate second cube around y-axis
    glLoadIdentity()
    glTranslatef(0, 0, -5)
    glRotate(angle, 0, 1, 0)  # Rotate around y-axis
    drawcube(-.9, -.9, -.9, 1.8)
    # TODO: draw and rotate second cube around y-axis
    glLoadIdentity()
    glTranslatef(0, 0, -5)
    glRotate(angle, 0, 0, 1)  # Rotate around x-axis
    drawcube(-.8, -.8, -.8, 1.6)
    ########################
    angle += .1
    glutSwapBuffers()


glutInit()
glutInitWindowSize(700, 700)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowPosition(500, 50)
glutCreateWindow(b"rotation of cube")
glutDisplayFunc(draw)
glutIdleFunc(draw)
init_my_sence(1000, 1000)  # this for make aspect reatio in prespective projection
glutMainLoop()
