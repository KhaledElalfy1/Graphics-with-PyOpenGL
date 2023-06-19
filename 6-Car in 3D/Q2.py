from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import Q1


def draw_animated_wheel(x_loc, y_loc, z_loc, angle):
    glLoadIdentity()
    Q1.reposition_camera()
    glTranslatef(x_loc, y_loc, z_loc)
    glRotate(angle, 0, 0, -1)
    glutWireTorus(.15, .35, 10, 12)


angle = 0
forward = True


def draw():
    global angle
    global forward
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    Q1.reposition_camera()
    Q1.drawaxis()
    # TODO draw the bottom cube
    glColor3f(1, 0, 0)
    glLoadIdentity()
    Q1.reposition_camera()
    glScale(4, 1, 2)
    glutWireCube(1)
    # TODO draw the upper cube
    glLoadIdentity()
    Q1.reposition_camera()
    glTranslatef(0, .85, 0)  # to put the cube above of the lower cube
    glScale(3, 1, 2)
    glutWireCube(.7)

    glColor3d(0, 0, 1)
    draw_animated_wheel(2, -.5, 1, angle)  # TODO the front left wheel
    draw_animated_wheel(2, -.5, -1, angle)  # TODO the front right wheel
    draw_animated_wheel(-2, -.5, -1, angle)  # TODO the back right wheel
    draw_animated_wheel(-2, -.5, 1, angle)  # TODO the back right wheel
    # glutWireTeapot(.2)
    # TODO draw bulbs
    glColor3d(1, 1, 0)
    Q1.draw_bulbs(2, 0.05, .5)  # TODO left bulb
    Q1.draw_bulbs(2, 0.05, -.5)  # TODO right bulb
    ############
    glutSwapBuffers()
    angle = angle + (.5 if forward else -.5)


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(500, 50)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow(b"My C00l Car")
    Q1.initprojection()
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()
