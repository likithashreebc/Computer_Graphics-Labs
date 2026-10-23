from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Line coordinates
x1, y1 = 100, 100
x2, y2 = 400, 300

# Draw a single pixel
def setPixel(x, y):
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()

# Bresenham Line Drawing Algorithm
def bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    err = dx - dy

    while True:
        setPixel(x1, y1)

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x1 += sx

        if e2 < dx:
            err += dx
            y1 += sy

# Display callback
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)
    glPointSize(4)

    bresenham(x1, y1, x2, y2)

    glFlush()

# Initialization
def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(1.0, 0.0, 0.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 500, 0, 500)

# Main
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Bresenham Line Drawing")

init()

glutDisplayFunc(display)

glutMainLoop()