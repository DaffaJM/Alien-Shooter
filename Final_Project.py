from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

pos_x = 0
pos_y = 0

merah = 255
hijau = 0
biru = 0


def pesawat_user():
    global pos_x, pos_y
    global merah, hijau, biru
    glBegin(GL_POLYGON)
    glColor3ub(merah, hijau, biru)
    glVertex2f(200 + pos_x, 50 + pos_y)
    glVertex2f(300 + pos_x, 50 + pos_y)
    glVertex2f(250 + pos_x, 150 + pos_y)
    glEnd()

def pesawat_alien1():
    glBegin(GL_POLYGON)
    glColor3ub(255, 255, 255)
    glVertex2f(100, 600)
    glVertex2f(150, 550)
    glVertex2f(200, 600)
    glEnd()

def pesawat_alien2():
    glBegin(GL_POLYGON)
    glColor3ub(255, 255, 255)
    glVertex2f(200, 550)
    glVertex2f(250, 500)
    glVertex2f(300, 550)
    glEnd()

def pesawat_alien3():
    glBegin(GL_POLYGON)
    glColor3ub(255, 255, 255)
    glVertex2f(300, 600)
    glVertex2f(350, 550)
    glVertex2f(400, 600)
    glEnd()

# inputan yang pake mouse dihapus aja diganti input make keyboard
# def input_mouse(button, state, x, y):
#     global merah, hijau, biru

#     if button == GLUT_RIGHT_BUTTON:
#         if merah < 255:
#             merah = 255
#             hijau = 0
#             biru = 0
#         elif hijau < 255:
#             merah = 0
#             hijau = 255
#             biru = 0
#     elif button == GLUT_LEFT_BUTTON:
#         if biru < 255:
#             merah = 0
#             hijau = 0
#             biru = 255
#         else:
#             merah = 0
#             hijau = 0
#             biru = 0

def input_keyboard(key, x, y):
    global pos_x, pos_y
    global merah, hijau, biru

    if key == GLUT_KEY_RIGHT:
        pos_x += 10
    elif key == GLUT_KEY_LEFT:
        pos_x -= 10
    elif key == GLUT_KEY_UP:
        if merah < 255:
            merah = 255
            hijau = 0
            biru = 0
        elif hijau < 255:
            merah = 0
            hijau = 255
            biru = 0
    elif key == GLUT_KEY_DOWN:
        if biru < 255:
            merah = 0
            hijau = 0
            biru = 255
        else:
            merah = 255
            hijau = 0
            biru = 0


def iterate():
    glViewport(0, 0, 500, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 700, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    pesawat_user()
    pesawat_alien1()
    pesawat_alien2()
    pesawat_alien3()
    glutSwapBuffers()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 650)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("Alien Shooter")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutSpecialFunc(input_keyboard)
# glutMouseFunc(input_mouse)

glutMainLoop()