import pygame
import time
#设置
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode([800,600])
keep_going=True
pic=pygame.image.load("C:/shockley/我的/编程/游戏/CrazySmile.bmp")
colorkey=pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx=400
picy=100
picw=pic.get_width()
pich=pic.get_height()
speedx=5
speedy=5
paddlex=300
paddley=550
paddlew=200
paddleh=25
BLACK=(0,0,0)
WHITE=(255,255,255)
blood=100
pop=pygame.mixer.Sound("C:/shockley/我的/编程/游戏/pop.wav")
blip=pygame.mixer.Sound("C:/shockley/我的/编程/游戏/blip.wav")
font=pygame.font.SysFont("Times",24)
timer=pygame.time.Clock()

#游戏
while keep_going:
    #事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keep_going=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                blood=100
                picx=400
                picy=100
                speedx=5
                speedy=5
                paddlex=300
                paddley=550

    #条件
    if picx+picw>=800 or picx<=0:
        speedx=-speedx
    if picy<=0:
        speedy=-speedy
    if picy+pich>=600:
        blip.play()
        speedy=5
        blood-=10
        speedy=-speedy
    if picy+pich<=paddley+paddleh and picy+pich>=paddley and speedy>0:
        if picx+picw/2>=paddlex and picx+picw/2<=paddlex+paddlew:
            pop.play()
            blood+=1
            speedy=-speedy*1.1
    if blood<=0:
        speedx=speedy=0
        picy=10
        draw_string+="a"
    else:
        draw_string=" BLOOD:"+str(blood)

    screen.fill(BLACK)
    screen.blit(pic,(picx,picy))
    picx+=speedx
    picy+=speedy
    screen.blit(pic,(picx,picy))
    pygame.draw.rect(screen,WHITE,(paddlex,paddley,paddlew,paddleh))
    paddlex=pygame.mouse.get_pos()[0]
    paddley=pygame.mouse.get_pos()[1]
    paddlex-=paddlew/2
    paddley-=paddleh/2
    text=font.render(draw_string,True,WHITE)
    text_rect=text.get_rect()
    text_rect.centerx=screen.get_rect().centerx
    text_rect.y=10
    screen.blit(text,text_rect)
    pygame.display.update()
    timer.tick(60)

#退出
pygame.quit()
