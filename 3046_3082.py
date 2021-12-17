#Dibuat Oleh :
#202410103046
#202410103082

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#variabel yang menyimpan nilai untuk mengubah mode tampilan jika kondisi yang ingin ditampilkan terpenuhi
mode_tampilan = 0

#variabel untuk pesawat
pos_x = 0 #gerak pesawat user & peluru user kekanan dan kekiri
pos_y = 0 #gerak peluru user keatas
pos_x_pesawat_kiri = 190 #colision pesawat min kiri
pos_x_pesawat_kanan = 320 #colision pesawat max kanan
nyawa_user = 3

#variabel untuk alien
y_peluru_alien_tengah = 0
y_peluru_alien_kanan = 0
y_peluru_alien_kiri = 0
point_kanan = 0
point_tengah = 0
point_kiri = 0
mode_alien_kanan = 0
mode_alien_kiri = 0
mode_alien_tengah = 0
alien_hancur = 100

#variabel yang menyimpan nilai untuk merubah warna pesawat user
merah = 255
hijau = 0
biru = 0

#variabel yang akan menggerakkan objek sesuai keperluan sesuai sumbu x atau sumbu y
gerak_koordinat_x = 10
gerak_koordinat_y = 5
boolGerakX = False
boolGerakY = False



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
    glVertex2f(190 + pos_x, 80) #nilai max kiri pesawat user
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
    glVertex2f(320 + pos_x, 80) #nilai max kanan pesawat user
    glVertex2f(290 + pos_x, 120)
    glVertex2f(290 + pos_x, 100)
    glVertex2f(280 + pos_x, 100)
    glVertex2f(280 + pos_x, 130)
    glVertex2f(260 + pos_x, 150)
    glEnd()

    #kiri nos
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

    #kanan nos
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

    #desain kiri
    glBegin(GL_QUADS)
    glColor3ub(0, 0, 128)
    glVertex2f(230 + pos_x, 130)
    glVertex2f(230 + pos_x, 100)
    glVertex2f(220 + pos_x, 100)
    glVertex2f(220 + pos_x, 120)
    glEnd()

    #desain kanan
    glBegin(GL_QUADS)
    glColor3ub(0, 0, 128)
    glVertex2f(290 + pos_x, 120)
    glVertex2f(290 + pos_x, 100)
    glVertex2f(280 + pos_x, 100)
    glVertex2f(280 + pos_x, 130)
    glEnd()

    #jendela tengah
    glBegin(GL_QUADS)
    glColor3ub(biru, merah, hijau)
    glVertex2f(240 + pos_x, 130)
    glVertex2f(240 + pos_x, 90)
    glVertex2f(270 + pos_x, 90)
    glVertex2f(270 + pos_x, 130)
    glEnd()
    glPopMatrix()

def kotak_pelindung_pesawat():
    glPushMatrix()
    glBegin(GL_LINE_LOOP)
    glColor3ub(0, 255, 0)
    glVertex2f(188 + pos_x, 159)
    glVertex2f(189 + pos_x, 38)
    glVertex2f(320 + pos_x, 40)
    glVertex2f(320 + pos_x, 160)
    glEnd()
    glPopMatrix()

def peluru():
    global pos_x, pos_y
    glPushMatrix()
    glTranslated(0, pos_y, 0)
    #pucuk
    glBegin(GL_TRIANGLES)
    glColor3ub(255, 26, 5)
    glVertex2f(258 + pos_x, 266)
    glVertex2f(244 + pos_x, 246)
    glVertex2f(269 + pos_x, 247)
    glEnd()

    # tengah
    glBegin(GL_QUADS)
    glColor3ub(255, 255, 255)
    glVertex2f(244 + pos_x, 246)
    glVertex2f(269 + pos_x, 247)
    glVertex2f(269 + pos_x, 206)
    glVertex2f(244 + pos_x, 206)
    glEnd()

    #api
    glBegin(GL_POLYGON)
    glColor3ub(255, 113, 5)
    glVertex2f(269 + pos_x, 206)
    glVertex2f(265 + pos_x, 193)
    glVertex2f(257 + pos_x, 182)
    glVertex2f(249 + pos_x, 193)
    glVertex2f(244 + pos_x, 206)
    glEnd()

    #loreng1
    glBegin(GL_QUADS)
    glColor3ub(255, 26, 5)
    glVertex2f(269 + pos_x, 247)
    glVertex2f(244 + pos_x, 238)
    glVertex2f(244 + pos_x, 231)
    glVertex2f(269 + pos_x, 240)
    glEnd()

    #loreng2
    glBegin(GL_QUADS)
    glColor3ub(255, 26, 5)
    glVertex2f(269 + pos_x, 232)
    glVertex2f(244 + pos_x, 225)
    glVertex2f(244 + pos_x, 218)
    glVertex2f(269 + pos_x, 225)
    glEnd()

    #loreng3
    glBegin(GL_QUADS)
    glColor3ub(255, 26, 5)
    glVertex2f(269 + pos_x, 219)
    glVertex2f(244 + pos_x, 212)
    glVertex2f(244 + pos_x, 206)
    glVertex2f(269 + pos_x, 213)
    glEnd()
    glPopMatrix()

def alien_kanan(mode_alien_kanan):
    if mode_alien_kanan == False:
        glPushMatrix()
        ##PESAWAT 1 KANAN
        #bag bawah
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
    
    elif mode_alien_kanan == True:
        glPushMatrix()
        glTranslated(0, alien_hancur, 0)
        ##PESAWAT 1 KANAN
        #bag bawah
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

def peluru_alien_kanan():
    glPushMatrix()
    glTranslated(0, y_peluru_alien_kanan, 0)
    #pesawat kanan
    glBegin(GL_QUADS)
    glColor3ub(255, 26, 5)
    glVertex2f(393, 547)
    glVertex2f(393, 525)
    glVertex2f(401, 525)
    glVertex2f(401, 547)
    glEnd()
    glPopMatrix()

def alien_tengah(mode_alien_tengah):
    if mode_alien_tengah == False:
        glPushMatrix()
        ##PESAWAT 2 TENGAH
        #bag bawah p. TENGAH
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
        glPopMatrix()

    elif mode_alien_tengah == True:
        glPushMatrix()
        glTranslated(0, alien_hancur, 0)
        ##PESAWAT 2 TENGAH
        #bag bawah p. TENGAH
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
        glPopMatrix()

def peluru_alien_tengah():
    glPushMatrix()
    glTranslated(0, y_peluru_alien_tengah, 0)
    #pesawat tengah
    glBegin(GL_QUADS)
    glColor3ub(255, 26, 5)
    glVertex2f(265, 450)
    glVertex2f(265, 430)
    glVertex2f(273, 430)
    glVertex2f(273, 450)
    glEnd()
    glPopMatrix()

def alien_kiri(mode_alien_kiri):
    if mode_alien_kiri == False:
        ##PESAWAT 3 KIRI
        ##bag bawah p. KIRI
        glPushMatrix()
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
        glPopMatrix()
    
    elif mode_alien_kiri == True:
        glPushMatrix()
        glTranslated(0, alien_hancur, 0)
        ##PESAWAT 3 KIRI
        ##bag bawah p. KIRI
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
        glPopMatrix()

def peluru_alien_kiri():
    glPushMatrix()
    glTranslated(0, y_peluru_alien_kiri, 0)
    #pesawat kiri
    glBegin(GL_QUADS)
    glColor3ub(255, 26, 5)
    glVertex2f(120, 544)
    glVertex2f(120, 523)
    glVertex2f(128, 523)
    glVertex2f(128, 544)
    glEnd()
    glPopMatrix()

def menu():
    glPushMatrix()
    # kotak start
    glBegin(GL_QUADS)
    glColor3ub(252, 214, 20)
    glVertex2f(115, 390)
    glVertex2f(117, 315)
    glVertex2f(378, 312)
    glVertex2f(377, 400)
    glEnd()

    #huruf S
    glBegin(GL_LINE_LOOP)
    glColor3ub(0, 0, 0)
    glVertex2f(137, 376)
    glVertex2f(173, 376)
    glVertex2f(175, 364)
    glVertex2f(147, 364)
    glVertex2f(147, 352)
    glVertex2f(177, 351)
    glVertex2f(177, 328)
    glVertex2f(137, 329)
    glVertex2f(137, 340)
    glVertex2f(170, 337)
    glVertex2f(167, 345)
    glVertex2f(138, 346)
    glEnd()

    #huruf T
    glBegin(GL_LINE_LOOP)
    glColor3ub(0, 0, 0)
    glVertex2f(189, 376)
    glVertex2f(225, 376)
    glVertex2f(228, 367)
    glVertex2f(213, 367)
    glVertex2f(213, 328)
    glVertex2f(200, 329)
    glVertex2f(199, 367)
    glVertex2f(184, 368)
    glEnd()

    #huruf A
    glBegin(GL_LINE_LOOP)
    glColor3ub(0, 0, 0)
    glVertex2f(246, 376)
    glVertex2f(232, 329)
    glVertex2f(271, 331)
    glVertex2f(259, 375)
    glEnd()

    #huruf A2
    glBegin(GL_LINE_LOOP)
    glColor3ub(0, 0, 0)
    glVertex2f(252, 360)
    glVertex2f(244, 340)
    glVertex2f(260, 339)
    glEnd()

    #huruf R
    glBegin(GL_LINE_LOOP)
    glColor3ub(0, 0, 0)
    glVertex2f(278, 376)
    glVertex2f(280, 330)
    glVertex2f(292, 330)
    glVertex2f(292, 345)
    glVertex2f(298, 347)
    glVertex2f(316, 327)
    glVertex2f(327, 330)
    glVertex2f(310, 350)
    glVertex2f(310, 350)
    glVertex2f(313, 358)
    glVertex2f(313, 372)
    glVertex2f(306, 376)
    glEnd()

    #R2
    glBegin(GL_LINE_LOOP)
    glColor3ub(0, 0, 0)
    glVertex2f(288, 369)
    glVertex2f(302, 368)
    glVertex2f(303, 358)
    glVertex2f(289, 354)
    glEnd()

    #huruf T2
    glBegin(GL_LINE_LOOP)
    glColor3ub(0, 0, 0)
    glVertex2f(324, 377)
    glVertex2f(360, 377)
    glVertex2f(364, 368)
    glVertex2f(348, 368)
    glVertex2f(347, 331)
    glVertex2f(335, 329)
    glVertex2f(335, 368)
    glVertex2f(319, 369)
    glEnd()
    glPopMatrix()

def tampilan_menang():
    glPushMatrix()
    #kotak start
    glBegin(GL_QUADS)
    glColor3ub(252, 214, 20)
    glVertex2f(115, 390)
    glVertex2f(117, 265)
    glVertex2f(378, 262)
    glVertex2f(377, 400)
    glEnd()

    #huruf W
    glBegin(GL_LINE_LOOP)
    glColor3ub(0, 0, 0)
    glVertex2f(140, 370)
    glVertex2f(160, 277)
    glVertex2f(180, 277)
    glVertex2f(190, 340)
    glVertex2f(200, 277)
    glVertex2f(220, 277)
    glVertex2f(240, 370)
    glVertex2f(220, 370)
    glVertex2f(211, 310)
    glVertex2f(200, 370)
    glVertex2f(180, 370)
    glVertex2f(169, 310)
    glVertex2f(160, 370)
    glVertex2f(140, 370)
    glEnd()

    #huruf I
    glBegin(GL_LINE_LOOP)
    glColor3ub(0, 0, 0)
    glVertex2f(260, 370)
    glVertex2f(260, 280)
    glVertex2f(280, 280)
    glVertex2f(280, 370)
    glEnd()

    #huruf N
    glBegin(GL_LINE_LOOP)
    glColor3ub(0, 0, 0)
    glVertex2f(300, 370)
    glVertex2f(300, 278)
    glVertex2f(320, 278)
    glVertex2f(320, 330)
    glVertex2f(337, 278)
    glVertex2f(360, 278)
    glVertex2f(360, 370)
    glVertex2f(340, 370)
    glVertex2f(340, 310)
    glVertex2f(320, 370)
    glVertex2f(300, 370)
    glEnd()
    glPopMatrix()

def tampilan_kalah():
    glPushMatrix()
    #kotak start
    glBegin(GL_QUADS)
    glColor3ub(252, 214, 20)
    glVertex2f(115, 390)
    glVertex2f(117, 315)
    glVertex2f(378, 312)
    glVertex2f(377, 400)
    glEnd()

    #L
    glBegin(GL_LINE_LOOP)
    glColor3ub(0, 0, 0)
    glVertex2f(173, 382)
    glVertex2f(161, 374)
    glVertex2f(160, 334)
    glVertex2f(194, 334)
    glVertex2f(205, 345)
    glVertex2f(171, 343)
    glEnd()

    #O besar
    glBegin(GL_LINE_LOOP)
    glColor3ub(0, 0, 0)
    glVertex2f(214, 371)
    glVertex2f(214, 341)
    glVertex2f(218, 337)
    glVertex2f(248, 337)
    glVertex2f(252, 340)
    glVertex2f(252, 374)
    glVertex2f(249, 377)
    glVertex2f(217, 377)
    # glVertex2f(252, 374)
    glEnd()

    #O tengah
    glBegin(GL_LINE_LOOP)
    glColor3ub(0, 0, 0)
    glVertex2f(225, 365)
    glVertex2f(225, 350)
    glVertex2f(242, 350)
    glVertex2f(242, 364)
    glEnd()

    #S
    glBegin(GL_LINE_LOOP)
    glColor3ub(0, 0, 0)
    glVertex2f(264, 378)
    glVertex2f(265, 350)
    glVertex2f(288, 354)
    glVertex2f(288, 345)
    glVertex2f(264, 344)
    glVertex2f(264, 336)
    glVertex2f(294, 338)
    glVertex2f(295, 360)
    glVertex2f(274, 358)
    glVertex2f(274, 368)
    glVertex2f(291, 368)
    glVertex2f(294, 378)
    glEnd()

    #E
    glBegin(GL_LINE_LOOP)
    glColor3ub(0, 0, 0)
    glVertex2f(305, 379)
    glVertex2f(305, 338)
    glVertex2f(336, 338)
    glVertex2f(335, 347)
    glVertex2f(315, 346)
    glVertex2f(315, 354)
    glVertex2f(335, 357)
    glVertex2f(334, 363)
    glVertex2f(316, 362)
    glVertex2f(316, 372)
    glVertex2f(333, 373)
    glVertex2f(334, 379)
    glEnd()
    glPopMatrix()

def lintang_wengi1():
    glPushMatrix()
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
    glPopMatrix()

def input_keyboard(key, x, y):
    global pos_x, pos_x_pesawat_kanan, pos_x_pesawat_kiri
    global merah, hijau, biru

    #menggeser pesawat user dan peluru user ke kanan setelah keyboard -> diklick
    if key == GLUT_KEY_RIGHT:
        pos_x_pesawat_kiri += 10
        pos_x_pesawat_kanan += 10
        pos_x += 10

    #menggeser pesawat user dan peluru user ke kiri setelah keyboard <- diklick
    elif key == GLUT_KEY_LEFT:
        pos_x_pesawat_kiri -= 10
        pos_x_pesawat_kanan -= 10
        pos_x -= 10

    #mengubah warna ke warna merah dan warna hijau
    elif key == GLUT_KEY_UP:
        if merah < 255:
            merah = 255
            hijau = 0
            biru = 0
        elif hijau < 255:
            merah = 0
            hijau = 255
            biru = 0

    #mengubah warna ke warna merah dan warna biru
    elif key == GLUT_KEY_DOWN:
        if biru < 255:
            merah = 0
            hijau = 0
            biru = 255
        else:
            merah = 255
            hijau = 0
            biru = 0

def timer(value):
    global pos_x, pos_y, pos_x_pesawat_kiri, pos_x_pesawat_kanan, nyawa_user, mode_tampilan
    global y_peluru_alien_tengah, y_peluru_alien_kanan, y_peluru_alien_kiri, mode_alien_tengah, mode_alien_kanan, mode_alien_kiri, point_kanan, point_tengah, point_kiri
    global boolGerakX, boolGerakY
    glutTimerFunc(1000//30, timer, 0)
    if mode_tampilan == 1:

        #untuk menggerakkan secara otomatis peluru user sesuai koordinat y
        if boolGerakY == False:
            pos_y += gerak_koordinat_y

        #mengembalikan nilai peluru user setelah keluar dari window menjadi 0
        if pos_y == 460:
            pos_y = 0

        #mengembalikan nilai peluru alien kanan setelah keluar dari window menjadi 0
        if y_peluru_alien_kanan == -600 and point_kanan == 0:
            y_peluru_alien_kanan = 0
        #mengembalikan nilai peluru alien tengah setelah keluar dari window menjadi 0
        if y_peluru_alien_tengah == -550 and point_tengah == 0:
            y_peluru_alien_tengah = 0
        #mengembalikan nilai peluru alien kiri setelah keluar dari window menjadi 0
        if y_peluru_alien_kiri == -600 and point_kiri == 0:
            y_peluru_alien_kiri = 0

        #kondisi pesawat alien kanan jika terkena peluru user
        if pos_y == 295 and (pos_x >= 90 and pos_x <= 190) and point_kanan == 0:
            mode_alien_kanan = True
            point_kanan = 1 
            print("pesawat alien kanan berhasil dihancurkan")

        #kondisi pesawat alien tengah jika terkena peluru user
        if pos_y == 295 and (pos_x >= -30 and pos_x <= 60) and point_tengah == 0:
            mode_alien_tengah = True
            point_tengah = 1
            print("pesawat alien tengah berhasil dihancurkan")

        #kondisi pesawat alien kiri jika terkena peluru user
        if pos_y == 295 and (pos_x <= -80 and pos_x >= -180) and point_kiri == 0:
            mode_alien_kiri = True
            point_kiri = 1
            print("pesawat alien kiri berhasil dihancurkan")

        #untuk menggerakkan secara otomatis peluru alien kanan sesuai koordinat y
        if boolGerakY == False:
            y_peluru_alien_kanan -= gerak_koordinat_y

        #kondisi jika peluru alien kanan mengenai colision pesawat user
        if (y_peluru_alien_kanan == -365) and ((pos_x_pesawat_kanan >= 400 and pos_x_pesawat_kanan <= 530) or (pos_x_pesawat_kiri >= 270 and pos_x_pesawat_kiri <= 400)):
            nyawa_user -= 1
            print('pesawat terkena peluru alien kanan')
            print("sisa nyawa anda adalah {}".format(nyawa_user))

        #untuk menggerakkan secara otomatis peluru alien tengah sesuai koordinat y
        if boolGerakY == False:
            y_peluru_alien_tengah -= gerak_koordinat_y

        #kondisi jika peluru alien tengah mengenai colision pesawat user
        if (y_peluru_alien_tengah == -280) and ((pos_x_pesawat_kanan >= 270 and pos_x_pesawat_kanan <= 400) or (pos_x_pesawat_kiri >= 140 and pos_x_pesawat_kiri <= 270)):
            nyawa_user -= 1
            print('pesawat terkena peluru alien tengah')
            print("sisa nyawa anda adalah {}".format(nyawa_user))

        #untuk menggerakkan secara otomatis peluru alien kiri sesuai koordinat y
        if boolGerakY == False:
            y_peluru_alien_kiri -= gerak_koordinat_y

        #kondisi jika peluru alien kiri mengenai colision pesawat user
        if (y_peluru_alien_kiri == -365) and ((pos_x_pesawat_kanan >= 130 and pos_x_pesawat_kanan <= 250) or (pos_x_pesawat_kiri >= 0 and pos_x_pesawat_kiri <= 120)):
            nyawa_user -= 1
            print('pesawat terkena peluru alien kiri')
            print("sisa nyawa anda adalah {}".format(nyawa_user))

        #kondisi jika pesawat alien kanan dan pesawat alien tengah dan pesawat alien kiri hancur, kemudian tampilan akan berubah menjadi tampilan menang
        if point_kanan == 1 and point_tengah == 1 and point_kiri == 1:
            print("\U0001F600---YOU WIN---\U0001F600")
            mode_tampilan = 3

        #kondisi jika nyawa user = 0, kemudian tampilan akan berubah menjadi tampilan kalah
        if nyawa_user == 0:
            print("GAME OVER !")
            mode_tampilan = 4

def on_click(button, state, x, y):
    global mode_tampilan
    if mode_tampilan == 0:
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            if (x >= 114 and x <= 379) and (y >= 248 and y <= 336):
                mode_tampilan = 1
            else:
                print("silahkan klik pada bagian start")
            # print("Klik Kiri ditekan ", "(", x, ",", y, ")")

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10, update, 0)

def iterate():
    glViewport(0, 0, 500, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 700, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    global mode_tampilan
    glClearColor(0, 0, 0.3, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glPushMatrix()
    if mode_tampilan == 0:
        lintang_wengi1()
        menu()
    elif mode_tampilan == 1:
        alien_kanan(mode_alien_kanan)
        peluru_alien_kanan()
        alien_tengah(mode_alien_tengah)
        peluru_alien_tengah()
        alien_kiri(mode_alien_kiri)
        peluru_alien_kiri()
        pesawat_user()
        peluru()
        # kotak_pelindung_pesawat()
        lintang_wengi1()
    elif mode_tampilan == 3:
        tampilan_menang()
    elif mode_tampilan == 4:
        tampilan_kalah()
    glPopMatrix()
    glFlush()

def display():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 650)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Alien Shooter")
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutSpecialFunc(input_keyboard)
    glutMouseFunc(on_click)
    glutTimerFunc(50, update, 0)
    glutTimerFunc(0,timer,0)
    glutMainLoop()

display()

