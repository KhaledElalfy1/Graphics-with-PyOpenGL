from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
rangle=0.0

def init():
    glClearColor(1,1,1,1)
    glLineWidth(5.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-.5,.5,-.5,.5,-.5,.5)
    glMatrixMode(GL_MODELVIEW)

def display_1():
    global rangle
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(0,0,0)
    glLoadIdentity()
    glutSolidSphere(.07,50,50)
    glRotate(rangle,0,0,1)
    glBegin(GL_LINES)
    glVertex(.08,0,0)
    glVertex(.26,0,0)
    glEnd()
    glTranslate(.3,0,0)
    glRotate(rangle,0,0,1)
    glutSolidCube(.05)
    glBegin(GL_LINES)
    glVertex(-.1, 0, 0)
    glVertex(.1, 0, 0)
    glEnd()
    rangle=rangle+.1
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500,500)
glutCreateWindow(b'gg')
glutDisplayFunc(display_1)
glutIdleFunc(display_1)
init()
glutMainLoop()

