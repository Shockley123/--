import pygame
import random
#设置
pygame.init()
screen=pygame.display.set_mode([800,600])
RGB=(0,255,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
radiu=15
keep_going=True
keep=False

#游戏循环
while keep_going:
    #监听事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keep_going=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            keep=True
        if event.type==pygame.MOUSEBUTTONUP:
            keep=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                radiu += 1
            if event.key==pygame.K_DOWN:
                radiu -= 1
            if event.key==pygame.K_r:
                RGB=(255,0,0)
            if event.key==pygame.K_w:
                RGB=(255,255,255)
            if event.key==pygame.K_g:
                RGB=(0,255,0)
            if event.key==pygame.K_b:
                RGB=(0,0,255)
            if event.key==pygame.K_e:
                RGB=(0,0,0)
            if event.key==pygame.K_y:
                RGB=(255,255,0)
            if event.key==pygame.K_f:
                screen.fill(BLACK)
            if event.key==pygame.K_p:
                RGB=(255,0,255)
            if event.key==pygame.K_l:
                RGB=(0,255,255)
            if event.key == pygame.K_a:
                RGB = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    #条件
    if keep:
        spot=event.pos
        pygame.draw.circle(screen,RGB,spot,radiu)

    drawstring="up=wide+,down=wide-,r=red,w=white,g=green,b=blue,y=yellow,e=black,p=purple,f=fill,wide="+str(radiu)
    font=pygame.font.SysFont("Times",18)
    text=font.render(drawstring,True,WHITE)
    text_rect=text.get_rect()
    text_rect.centerx=screen.get_rect().centerx
    text_rect.y=7
    screen.blit(text,text_rect)
    pygame.display.update()

#游戏结束，退出
pygame.quit()
