import pygame as pg
import sys
import random

# Initialize Pygame
pg.init()
pg.mouse.set_visible(False)
ekran = pg.display.set_mode((1366, 720))
zaman = pg.time.Clock()

yazi_fontu= pg.font.Font(None, 60)
yazi_yuzeyi=yazi_fontu.render("Kazandın",True,(255,255,255))

# Load images
mario = pg.image.load("mario.png")
arkaplan = pg.image.load("göküyüzü.png")
çimen = pg.image.load("çim.png")
su = pg.image.load("su.png")
bulut1 = pg.image.load("bulut1.png")
bulut2 = pg.image.load("bulut2.png")
agac1 = pg.image.load("ağaç1.png")
agac2 = pg.image.load("ağaç2.png")
hedef = pg.image.load("hedef.png")
imlec = pg.image.load("crosshair.png")
imlec_dortgeni = imlec.get_rect()

# Initialize variables
su_yuksekligi = 600
su_hizi = 0.3
bulut_mesafesi = 400
bulut_mesafesi2 = 700
bulut_hizi = 0.4
bulut_hizi2 = 0.41

# Hedef Yarat
hedefler = []
for i in range(5):
    x = random.randint(150, 1200)
    y = random.randint(100, 600)
    hedef_dortgeni = hedef.get_rect(center=(x, y))
    hedefler.append(hedef_dortgeni)

# Oyun Döngüsü
while True:
    for olay in pg.event.get():
        if olay.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if olay.type == pg.MOUSEMOTION:
            imlec_dortgeni.center = olay.pos
        if olay.type == pg.MOUSEBUTTONDOWN:
            for index, hedef_dortgeni in enumerate(hedefler):
                if hedef_dortgeni.collidepoint(olay.pos):
                    del hedefler[index]
                    break  # Exit the loop once a target is hit

    # Arkaplan ve nesnelerin çizimi
    ekran.blit(arkaplan, (0, 0))
    ekran.blit(agac1, (30, 315))
    ekran.blit(agac2, (1150, 310))
    ekran.blit(çimen, (0, 500))

    # Su Animasyonu
    su_yuksekligi -= su_hizi
    if su_yuksekligi > 620 or su_yuksekligi < 600:
        su_hizi *= -1
    ekran.blit(su, (0, su_yuksekligi))

    # Hedef çizimi
    for hedef_dortgeni in hedefler:
        ekran.blit(hedef, hedef_dortgeni)

    # Bulut Hareketkleri
    bulut_mesafesi -= bulut_hizi
    if bulut_mesafesi < 400 or bulut_mesafesi > 500:
        bulut_hizi *= -1
    ekran.blit(bulut2, (bulut_mesafesi, 150))

    bulut_mesafesi2 -= bulut_hizi2
    if bulut_mesafesi2 < 700 or bulut_mesafesi2 > 800:
        bulut_hizi2 *= -1
    ekran.blit(bulut1, (bulut_mesafesi2, 150))

    # Draw crosshair
    ekran.blit(imlec, imlec_dortgeni)
    if len(hedefler)==0:
        ekran.blit(yazi_yuzeyi,(600,300))

    # Update display and tick clock
    pg.display.update()
    zaman.tick(120)
