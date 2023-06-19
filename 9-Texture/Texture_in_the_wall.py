"""
Texture steps (init)
1) glEnable(GL_TEXTURE_2D)
2) pygame.image.load("1.png")
3) pygame.image.tostring(image, "RGBA", True)
4) glGenTextures(len(images), texture_names) # create identifiers for textures
5) glBindTexture(GL_TEXTURE_2D, texture_name) # modify THIS IDENTIFIER
6) glTexParameterf (many of those) # set the parameters
7) glTexImage2D # feed the binary image to opengl
              (Usage)
1) glBindTexture(GL_TEXTURE_2D, texture_name) # use THIS IDENTIFIER
2) glTexCoord(0, 0) repeat this
"""
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLUT import *
import pygame


def init():
    glClearColor(1, 1, 1, 1)
    loadTextures()


texture_names = [0, 1]


def texture_setup(texture_image_binary, texture_name, width, height):
    # TODO step[5] active a certain image
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
                 width,
                 height,
                 0,  # Texture border
                 GL_RGBA,  # RGBA Exactly as in  pygame.image.tostring(image, "RGBA", True)
                 GL_UNSIGNED_BYTE,
                 texture_image_binary)


def loadTextures():
    # TODO Step[1] Enable Texture
    glEnable(GL_TEXTURE_2D)  # [1]
    images = []
    # TODO Step[2] load image to programme
    images.append(pygame.image.load("wall.png"))
    images.append(pygame.image.load("chess.png"))
    # TODO Step[3] convert images to string
    textures = [pygame.image.tostring(image, 'RGBA', True) for image in images]
    # TODO Step[4] make id for each image
    glGenTextures(len(images), texture_names)  # size of two lists should be the same

    for i in range(len(images)):
        texture_setup(textures[i],  # binary images
                      texture_names[i],  # identifiers
                      images[i].get_width(),
                      images[i].get_height())


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(1, 1, 1)
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture_names[1])
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex2d(-1, -1)

    glTexCoord2f(0, 1)
    glVertex2d(-1, 1)

    glTexCoord2f(1, 1)
    glVertex2d(1, 1)

    glTexCoord2f(1, 0)
    glVertex2d(1, -1)

    glEnd()
    glPopMatrix()
    glFlush()


if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b'wall with texture')
    init()
    glutDisplayFunc(draw)
    glutMainLoop()
