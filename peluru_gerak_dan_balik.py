from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

pos_x = 0

#warna
merah = 255
hijau = 0
biru = 0

#kecepatan saatperpindahan
gerakX = 10
gerakY = 5

#representasi variabel perubahan gl Translated
deltaX = 0
deltaY = 0
deltaYy = 0 #buat si peluru user
deltaYy1 = 0 #buat peluru alien

#buat arah geraknya
boolGerakX = False
boolGerakY = False

#collision
acollisionX1 = -250 #collision pesawat alien  
acollisionX2 = 250 #collision pesawat alien
acollisionY1 = 544 #collision peluru alien bawah
acollisionY2 = 523 #collision peluru alien atas

ucollisionX1 = -250 #collision pesawat  
ucollisionX2 = 250 #collision pesawat
ucollisionY1 = 244 #collision peluru user bawah
ucollisionY2 = 244 #collision peluru user atas

#nyawa user terkena tembakan alien
nyawa_user = 2

def pesawat_user():
    global pos_x
    global merah, hijau, biru
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3ub(merah, hijau, biru)
    glVertex2f(250 + pos_x, 150)
    glVertex2f(230 + pos_x, 130)
    glVertex2f(230 + pos_x, 100)
    glVertex2f(220 + pos_x, 100)
    glVertex2f(220 + pos_x, 120)
    glVertex2f(190 + pos_x, 80)
    glVertex2f(205 + pos_x, 65)
    glVertex2f(220 + pos_x, 80)
    glVertex2f(220 + pos_x, 50)
    glVertex2f(230 + pos_x, 50)
    glVertex2f(230 + pos_x, 60)
    glVertex2f(240 + pos_x, 70)
    glVertex2f(250 + pos_x, 60)
    glVertex2f(250 + pos_x, 50)
    glVertex2f(260 + pos_x, 50)
    glVertex2f(260 + pos_x, 60)
    glVertex2f(270 + pos_x, 70)
    glVertex2f(280 + pos_x, 60)
    glVertex2f(280 + pos_x, 50)
    glVertex2f(290 + pos_x, 50)
    glVertex2f(290 + pos_x, 80)
    glVertex2f(305 + pos_x, 65)
    glVertex2f(320 + pos_x, 80)
    glVertex2f(290 + pos_x, 120)
    glVertex2f(290 + pos_x, 100)
    glVertex2f(280 + pos_x, 100)
    glVertex2f(280 + pos_x, 130)
    glVertex2f(260 + pos_x, 150)
    glEnd()
    glPopMatrix()

    #kiri nos
    glPushMatrix()
    glBegin(GL_LINE_LOOP)
    glColor3ub(255, 81, 0)
    glVertex2f(234 + pos_x, 60)
    glVertex2f(234 + pos_x, 40)
    glVertex2f(236 + pos_x, 50)
    glVertex2f(238 + pos_x, 40)
    glVertex2f(240 + pos_x, 50)
    glVertex2f(242 + pos_x, 40)
    glVertex2f(244 + pos_x, 50)
    glVertex2f(246 + pos_x, 40)
    glVertex2f(246 + pos_x, 60)
    glEnd()
    glPopMatrix()

    #kanan nos
    glPushMatrix()
    glBegin(GL_LINE_LOOP)
    glColor3ub(255, 81, 0)
    glVertex2f(264 + pos_x, 60)
    glVertex2f(264 + pos_x, 40)
    glVertex2f(266 + pos_x, 50)
    glVertex2f(268 + pos_x, 40)
    glVertex2f(270 + pos_x, 50)
    glVertex2f(272 + pos_x, 40)
    glVertex2f(274 + pos_x, 50)
    glVertex2f(276 + pos_x, 40)
    glVertex2f(276 + pos_x, 60)
    glEnd()
    glPopMatrix()

    #desain kiri
    glPushMatrix()
    glBegin(GL_QUADS)
    glColor3ub(0, 0, 128)
    glVertex2f(230 + pos_x, 130)
    glVertex2f(230 + pos_x, 100)
    glVertex2f(220 + pos_x, 100)
    glVertex2f(220 + pos_x, 120)
    glEnd()
    glPopMatrix()

    #desain kanan
    glPushMatrix()
    glBegin(GL_QUADS)
    glColor3ub(0, 0, 128)
    glVertex2f(290 + pos_x, 120)
    glVertex2f(290 + pos_x, 100)
    glVertex2f(280 + pos_x, 100)
    glVertex2f(280 + pos_x, 130)
    glEnd()
    glPopMatrix()

    #jendela tengah
    glPushMatrix()
    glBegin(GL_QUADS)
    glColor3ub(biru, merah, hijau)
    glVertex2f(240 + pos_x, 130)
    glVertex2f(240 + pos_x, 90)
    glVertex2f(270 + pos_x, 90)
    glVertex2f(270 + pos_x, 130)
    glEnd()
    glPopMatrix()

def peluru():
    #pucuk
    global pos_x
    glPushMatrix()
    glTranslated(0, deltaYy, 0)
    glBegin(GL_TRIANGLES)
    glColor3ub(255, 26, 5)
    glVertex2f(258 + pos_x, 266)
    glVertex2f(244 + pos_x, 246)
    glVertex2f(269 + pos_x, 247)
    glEnd()
    # glPopMatrix()

    # tengah
    # glPushMatrix()
    # glTranslated(0, deltaYy, 0)
    glBegin(GL_QUADS)
    glColor3ub(255, 255, 255)
    glVertex2f(244 + pos_x, 246)
    glVertex2f(269 + pos_x, 247)
    glVertex2f(269 + pos_x, 206)
    glVertex2f(244 + pos_x, 206)
    glEnd()
    # glPopMatrix()

    #api
    # glPushMatrix()
    glBegin(GL_POLYGON)
    # glTranslated(0, deltaYy, 0)
    glColor3ub(255, 113, 5)
    glVertex2f(269 + pos_x, 206)
    glVertex2f(265 + pos_x, 193)
    glVertex2f(257 + pos_x, 182)
    glVertex2f(249 + pos_x, 193)
    glVertex2f(244 + pos_x, 206)
    glEnd()
    # glPopMatrix()

    #loreng1
    # glPushMatrix()
    # glTranslated(0, deltaYy, 0)
    glBegin(GL_QUADS)
    glColor3ub(255, 26, 5)
    glVertex2f(269 + pos_x, 247)
    glVertex2f(244 + pos_x, 238)
    glVertex2f(244 + pos_x, 231)
    glVertex2f(269 + pos_x, 240)
    glEnd()
    # glPopMatrix()

    #loreng2
    # glPushMatrix()
    # glTranslated(0, deltaYy, 0)
    glBegin(GL_QUADS)
    glColor3ub(255, 26, 5)
    glVertex2f(269 + pos_x, 232)
    glVertex2f(244 + pos_x, 225)
    glVertex2f(244 + pos_x, 218)
    glVertex2f(269 + pos_x, 225)
    glEnd()
    # glPopMatrix()

    #loreng3
    # glPushMatrix()
    # glTranslated(0, deltaYy, 0)
    glBegin(GL_QUADS)
    glColor3ub(255, 26, 5)
    glVertex2f(269 + pos_x, 219)
    glVertex2f(244 + pos_x, 212)
    glVertex2f(244 + pos_x, 206)
    glVertex2f(269 + pos_x, 213)
    glEnd()
    glPopMatrix()

def peluru_alien():
    #pesawat kiri
    glPushMatrix()
    glTranslated(0, deltaYy1, 0)
    glBegin(GL_QUADS)
    glColor3ub(255, 26, 5)
    glVertex2f(120, 544)
    glVertex2f(120, 523)
    glVertex2f(128, 523)
    glVertex2f(128, 544)
    glEnd()
    glPopMatrix()

    #pesawat tengah
    glPushMatrix()
    glTranslated(0, deltaYy1, 0)
    glBegin(GL_QUADS)
    glColor3ub(255, 26, 5)
    glVertex2f(265, 450)
    glVertex2f(265, 430)
    glVertex2f(273, 430)
    glVertex2f(273, 450)
    glEnd()
    glPopMatrix()

    #pesawat kanan
    glPushMatrix()
    glTranslated(0, deltaYy1, 0)
    glBegin(GL_QUADS)
    glColor3ub(255, 26, 5)
    glVertex2f(393, 547)
    glVertex2f(393, 525)
    glVertex2f(401, 525)
    glVertex2f(401, 547)
    glEnd()
    glPopMatrix()

def musuh():
    ##PESAWAT 1 KANAN
    #bag bawah
    glPushMatrix()
    # glTranslated(deltaX, deltaY, 0)
    glBegin(GL_QUADS)
    glColor3ub(130, 56, 0)
    glVertex2f(369, 564)
    glVertex2f(421, 564)
    glVertex2f(425, 572)
    glVertex2f(365, 572)
    glEnd()

    #bag tengah p. kanan
    glBegin(GL_POLYGON)
    glColor3ub(158, 75, 11)
    glVertex2f(357, 572)
    glVertex2f(352, 576)
    glVertex2f(355, 583)
    glVertex2f(435, 583)
    glVertex2f(439, 577)
    glVertex2f(434, 572)
    glEnd()

    #bag atas p. kanan
    glBegin(GL_POLYGON)
    glColor3ub(158, 75, 11)
    glVertex2f(365, 583)
    glVertex2f(368, 590)
    glVertex2f(395, 598)
    glVertex2f(423, 590)
    glVertex2f(439, 577)
    glVertex2f(428, 583)
    glEnd()

    #jendela1 p. kanan
    glBegin(GL_QUADS)
    glColor3ub(252, 214, 20)
    glVertex2f(371, 580)
    glVertex2f(365, 580)
    glVertex2f(365, 575)
    glVertex2f(371, 575)
    glEnd()

    #jendela2 p. kanan
    glBegin(GL_QUADS)
    glColor3ub(252, 214, 20)
    glVertex2f(392, 580)
    glVertex2f(398, 580)
    glVertex2f(398, 575)
    glVertex2f(392, 575)
    glEnd()

    #jendela3 p. kanan
    glBegin(GL_QUADS)
    glColor3ub(252, 214, 20)
    glVertex2f(427, 580)
    glVertex2f(420, 580)
    glVertex2f(420, 575)
    glVertex2f(427, 575)
    glEnd()
    glPopMatrix()

    ##PESAWAT 2 TENGAH
    ##bag bawah p. TENGAH
    # glPushMatrix()
    # glTranslated(deltaX, deltaY, 0)
    glBegin(GL_QUADS)
    glColor3ub(130, 56, 0)
    glVertex2f(240, 569)
    glVertex2f(244, 561)
    glVertex2f(296, 561)
    glVertex2f(300, 569)
    glEnd()

    #bag tengah p. TENGAH
    glBegin(GL_POLYGON)
    glColor3ub(158, 75, 11)
    glVertex2f(230, 580)
    glVertex2f(227, 574)
    glVertex2f(231, 569)
    glVertex2f(309, 569)
    glVertex2f(313, 575)
    glVertex2f(310, 580)
    glEnd()

    #bag atas p. TENGAH
    glBegin(GL_POLYGON)
    glColor3ub(158, 75, 11)
    glVertex2f(239, 580)
    glVertex2f(243, 587)
    glVertex2f(270, 595)
    glVertex2f(298, 587)
    glVertex2f(303, 580)
    glEnd()

    #jendela1 p. TENGAH
    glBegin(GL_QUADS)
    glColor3ub(252, 214, 20)
    glVertex2f(240, 577)
    glVertex2f(240, 572)
    glVertex2f(246, 572)
    glVertex2f(246, 577)
    glEnd()

    #jendela2 p. TENGAH
    glBegin(GL_QUADS)
    glColor3ub(252, 214, 20)
    glVertex2f(267, 577)
    glVertex2f(273, 577)
    glVertex2f(273, 573)
    glVertex2f(267, 573)
    glEnd()

    #jendela3 p. TENGAH
    glBegin(GL_QUADS)
    glColor3ub(252, 214, 20)
    glVertex2f(295, 577)
    glVertex2f(301, 577)
    glVertex2f(301, 573)
    glVertex2f(295, 573)
    glEnd()
    # glPopMatrix()

    ##PESAWAT 3 KIRI
    ##bag bawah p. KIRI
    # glPushMatrix()
    # glTranslated(deltaX, deltaY, 0)
    glBegin(GL_QUADS)
    glColor3ub(130, 56, 0)
    glVertex2f(97, 570)
    glVertex2f(101, 562)
    glVertex2f(153, 562)
    glVertex2f(157, 570)
    glEnd()

    #bag tengah p. KIRI
    glBegin(GL_POLYGON)
    glColor3ub(158, 75, 11)
    glVertex2f(87, 581)
    glVertex2f(84, 575)
    glVertex2f(88, 570)
    glVertex2f(166, 570)
    glVertex2f(170, 576)
    glVertex2f(167, 581)
    glEnd()

    #bag atas p. KIRI
    glBegin(GL_POLYGON)
    glColor3ub(158, 75, 11)
    glVertex2f(96, 581)
    glVertex2f(100, 588)
    glVertex2f(127, 596)
    glVertex2f(155, 588)
    glVertex2f(160, 581)
    glEnd()

    #jendela1 p. KIRI
    glBegin(GL_QUADS)
    glColor3ub(252, 214, 20)
    glVertex2f(97, 578)
    glVertex2f(97, 574)
    glVertex2f(103, 574)
    glVertex2f(103, 578)
    glEnd()

    #jendela2 p. KIRI
    glBegin(GL_QUADS)
    glColor3ub(252, 214, 20)
    glVertex2f(124, 578)
    glVertex2f(124, 574)
    glVertex2f(130, 574)
    glVertex2f(130, 578)
    glEnd()

    #jendela3 p. KIRI
    glBegin(GL_QUADS)
    glColor3ub(252, 214, 20)
    glVertex2f(152, 578)
    glVertex2f(152, 574)
    glVertex2f(158, 574)
    glVertex2f(158, 578)
    glEnd()

def lintang_wengi1():
    glColor3ub(255, 255, 255)
    glPointSize(2.0)
    glBegin(GL_POINTS)
    glVertex2f(102, 324)
    glVertex2f(126, 371)
    glVertex2f(139, 358)
    glVertex2f(131, 335)
    glVertex2f(95, 365)
    glVertex2f(90, 477)
    glVertex2f(77, 452)
    glVertex2f(146, 462)
    glVertex2f(355, 533)
    glVertex2f(357, 521)
    glVertex2f(391, 515)
    glVertex2f(389, 528)
    glVertex2f(374, 549)
    glVertex2f(380, 584)
    glVertex2f(274, 589)
    glVertex2f(318, 568)
    glVertex2f(308, 376)
    glVertex2f(334, 375)
    glVertex2f(321, 356)
    glVertex2f(335, 352)
    glVertex2f(366, 352)
    glVertex2f(366, 374)
    glVertex2f(371, 421)
    glVertex2f(317, 429)
    glVertex2f(274, 468)
    glVertex2f(150, 50)
    glVertex2f(112, 28)
    glVertex2f(39, 72)
    glVertex2f(111, 89)
    glVertex2f(390, 223)
    glVertex2f(455, 236)
    glVertex2f(484, 214)
    glVertex2f(474, 111)
    glVertex2f(495, 65)
    glVertex2f(398, 75)
    glVertex2f(425, 112)
    glVertex2f(157, 255)
    glVertex2f(171, 198)
    glVertex2f(126, 162)
    glVertex2f(72, 177)
    glEnd()

def timer(value):
    global ucollisionX1
    global ucollisionX2
    global ucollisionY1
    global ucollisionY2
    global acollisionX1
    global acollisionX2
    global acollisionY1
    global acollisionY2
    global gerakX
    global gerakY
    global boolGerakX
    global boolGerakY
    glutTimerFunc(1000//30, timer, 0)
    global deltaX #panggil variabel global kedalam fungsi timer
    global deltaYy
    global deltaY
    global deltaYy1
    global pos_x

    # if boolGerakX == False:
    #     pos_x -= gerakX
    #     collisionX1 -= gerakX
    #     collisionX2 -= gerakX
    # else:
    #     collisionX1 += gerakX
    #     collisionX2 += gerakX
    #     pos_x += gerakX
    #gerak peluru user ke atas
    if boolGerakY == False:
        deltaYy += gerakY
        ucollisionY1 += gerakY
        ucollisionY2 += gerakY

    #gerak peluru alien ke bawah
    if boolGerakY == False:
        deltaYy1 -= gerakY
        acollisionY1 -= gerakY
        acollisionY2 -= gerakY
    
    #jika peluru alien mentok balik posisi semula
    if acollisionY2 == 100:
        deltaYy1 = 0
        acollisionY2 = 244
    
    #jika peluru user mentok balik posisi semula
    if ucollisionY2 == 100:
        deltaYy = 0
        ucollisionY2 = 244

    if deltaYy == 450:
        deltaYy = 0
    
    if deltaYy1 == -700:
        deltaYy1 = 0

# def input_mouse()

def input_keyboard(key, x, y):
    global pos_x
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
    glClearColor(0, 0, 0.3, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    peluru()
    peluru_alien()
    pesawat_user()
    lintang_wengi1()
    musuh()
    glutSwapBuffers()

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10, update, 0)

def display():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 650)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Alien Shooter")
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutSpecialFunc(input_keyboard)
    # glutMouseFunc(input_mouse)
    glutTimerFunc(50, update, 0)
    glutTimerFunc(0,timer,0)
    glutMainLoop()

display()