import pygame as pg
import sys
import random


pg.init()
pg.mouse.set_visible(False)
ekran = pg.display.set_mode((1366,720))
zaman = pg.time.Clock()
mario = pg.image.load("mario.png")
arkaplan = pg.image.load("göküyüzü.png")
çimen = pg.image.load("çim.png")
su = pg.image.load("su.png")
bulut1 = pg.image.load("bulut1.png")
bulut2 = pg.image.load("bulut2.png")
agac1 = pg.image.load("ağaç1.png")
agac2 = pg.image.load("ağaç2.png")
su_yuksekligi =600
su_hizi = 0.3
bulut_mesafesi = 400
bulut_mesafesi2 =700
bulut_hizi= 0.4
bulut_hizi2 = 0.41
hedef = pg.image.load("hedef.png")
imlec = pg.image.load("crosshair.png")
imlec_dortgeni = imlec.get_rect()


hedefler =[]
for i in range(15):
    x =random.randint(150, 1200)
    y= random.randint(100, 600)
    hedef_dörtgeni = hedef.get_rect(center = (x,y))
    hedefler.append(hedef_dörtgeni)


while True:
    for olay in pg.event.get():
        if olay.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if olay.type == pg.MOUSEMOTION:
            imlec_dortgeni = imlec.get_rect(center=olay.pos)
    

    ekran.blit(arkaplan,(0,0))
    ekran.blit(agac1,(30,315))
    ekran.blit(agac2,(1150,310))
    ekran.blit(çimen,(0,500))
    
    su_yuksekligi = su_yuksekligi - su_hizi
    if su_yuksekligi > 620 or su_yuksekligi < 600:
        su_hizi *= -1

    for i in hedefler:
            ekran.blit(hedef,i)

    
    ekran.blit(bulut2,(bulut_mesafesi,150))
    bulut_mesafesi = bulut_mesafesi - bulut_hizi
    if bulut_mesafesi > 500 or bulut_mesafesi < 400:
        bulut_hizi *= -1

    ekran.blit(bulut1,(bulut_mesafesi2,150))
    bulut_mesafesi2 = bulut_mesafesi2 - bulut_hizi2
    if bulut_mesafesi2 > 800 or bulut_mesafesi2 < 700:
        bulut_hizi2 *= -1

    ekran.blit(su,(0,su_yuksekligi))
    
    ekran.blit(imlec,imlec_dortgeni)

    pg.display.update()
    zaman.tick(120)
