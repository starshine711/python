import pygame,sys
pygame.init()
class man(pygame.sprite.Sprite):
    def __init__(self,image,xy,x2):
        pygame.sprite.Sprite.__init__(self) #载入动画精灵        
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = xy
        self.xy = xy
        self.leftx = x2
        self.set ='land'
        self.pos = 'right'
        self.type = 'man'
class ghost(pygame.sprite.Sprite):
    def __init__(self,image,xy,x2):
        pygame.sprite.Sprite.__init__(self) #载入动画精灵        
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = xy
        self.xy = xy
        self.leftx = x2
        self.pos = 'right'
        self.set ='land'
        self.type= 'ghost'
class ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #载入动画精灵        
        self.image = pygame.image.load('ship.png')
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top =650,350
        self.xy = 650,350
        self.pos = 'right'
        self.leftset ='empty'
        self.rightset ='empty'
    def check(self):
        self.leftset ='empty'
        self.rightset ='empty'
        for i in all:
            if i.rect.left == self.rect.left+10:
                self.leftset ='full'
            if i.rect.left == self.rect.left+100:
                self.rightset ='full'
class button():
    def __init__(self,image,xy):
        self.image =pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = xy

if 1:
    man1=man('man.png',[870,300],316)
    man2=man('man.png',[930,300],256)
    man3=man('man.png',[990,300],196)
    ghost1 =ghost('ghost1.png',[1050,300],136)
    ghost2 =ghost('ghost1.png',[1110,300],76)
    ghost3 =ghost('ghost1.png',[1170,300],16)
    ship =ship()
    men =[]
    ghosts =[]
    men.append(man1)
    men.append(man2)
    men.append(man3)
    ghosts.append(ghost1)
    ghosts.append(ghost2)
    ghosts.append(ghost3)
    all = list(set(men) ^ set(ghosts))
    global MENU
    global GAME
    global a
    MENU = True
    GAME=False
    a=0
def draw():
    screen.blit(back,[0,0])
    for i in all:
        if i.set =='boat1':
            i.rect.left=ship.rect.left+10
        if i.set =='boat2':
            i.rect.left=ship.rect.left+100
        screen.blit(i.image,i.rect)
    screen.blit(ship.image,ship.rect)
    screen.blit(go.image,go.rect)  
    pygame.display.flip()#画图    
GO =False
def cheshi():
    screen.blit(start.image,[1,1])
    pygame.display.flip()
    
def check():#检查位置
    LG = 0#左鬼
    LM = 0#左人数
    RG =0#右鬼
    RM =0#右人
    global MENU
    global GAME
    global a    
    for i in all:
        if i.rect.left < 600:
            i.pos = 'left'
        elif i.rect.left >600:
            i.pos='right'
    for i in men:
        if i.rect.left < 600:
            i.pos = 'left'
            LM +=1
        else:
            i.pos='right'
            RM +=1
    for i in ghosts:
        if i.rect.left < 600:
            i.pos = 'left'
            LG +=1
        else:
            i.pos='right'
            RG +=1
    if ship.rect.left < 600:
        ship.pos = 'left'
    else:
        ship.pos='right'
    if LM!=0 and RM!=0:
        if LG > LM or RG > RM:
            lost =pygame.image.load('lost.png')
            screen.blit(lost,[600,250])
            pygame.display.flip()
            pygame.time.delay(2000)
            for i in all:
                if i.set:
                    i.set='land'
                i.rect.left,i.rect.top = i.xy
            ship.rect.left,ship.rect.top=ship.xy
            GAME= False
            MENU = True
            a = 0
    if LM==LG==3:
        win =pygame.image.load('win.png')
        screen.blit(win,[600,250])
        pygame.display.flip()
        pygame.time.delay(2000)
        ship.rect.left,ship.rect.top=ship.xy
        for i in all:
            if i.set:
                i.set='land'
            i.rect.left,i.rect.top = i.xy
        GAME = False
        MENU = True
        a = 0
def txt():
    font = pygame.font.Font(None,35)
    time = font.render('times:%d'%a,1,(255,255,255))
    screen.blit(time,[600,15])
    pygame.display.flip()    
go =button('go.png',[550,20])#创建按钮
start =button('start.png',[500,400])
screen =pygame.display.set_mode([1224,506])
back =pygame.image.load('back.png')
while True:
    if MENU == True:
        back1=pygame.image.load('back1.png')
        screen.blit(back1,[0,0])
        screen.blit(start.image,start.rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start.rect.left<= event.pos[0] <= start.rect.left+ start.image.get_rect().width and go.rect.top<=event.pos[1]<= start.image.get_rect().height+start.rect.top:
                    GAME = True
                    MENU = False
    if GAME == True:
        ship.check()
        check()
        GO =False
        for i in all:
            if i.rect.left==ship.rect.left+10 or i.rect.left==ship.rect.left+100 :
                GO = True     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                a+=1
            for i in all:
                if event.type == pygame.MOUSEBUTTONDOWN:
        
                    if i.rect.left<= event.pos[0] <= i.rect.left+ i.image.get_rect().width and i.rect.top<=event.pos[1]<= i.image.get_rect().height+i.rect.top:
                        if i.pos ==ship.pos:
                            if i.set == 'land':
                                    if ship.leftset == 'empty':
                                        i.set = 'boat1'
                                        i.rect.left = ship.rect.left+10
                                    elif ship.rightset == 'empty':
                                        i.set = 'boat2'
                                        i.rect.left = ship.rect.left+100
                            elif i.set == 'boat1' or i.set == 'boat2':
                                if i.pos=='right':
                                    i.set ='land'
                                    i.rect.left,i.rect.top = i.xy
                                if i.pos=='left':
                                    i.set ='land'
                                    i.rect.left = i.leftx
            if GO:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if go.rect.left<= event.pos[0] <= go.rect.left+ go.image.get_rect().width and go.rect.top<=event.pos[1]<= go.image.get_rect().height+go.rect.top:
                        if ship.pos =='left':
                            for i in range(0,4):
                                ship.rect.left+=70
                                draw()
                                pygame.time.delay(300)
                        if ship.pos =='right':
                            for i in range(0,4):
                                ship.rect.left-=70
                                draw()
                                pygame.time.delay(300)
        draw()
        txt()