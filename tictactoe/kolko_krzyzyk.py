import pygame, sys
import numpy as np
from random import randint

pygame.init()
imp = pygame.image.load('ticatactoe_png/bg.png')

WIDTH = 600
HEIGHT = 600
BG_COLOR=(39, 186, 171)
LINE_COLOR=(42, 64, 59)
SIGN_COLOR=(79, 87, 168)
RED=(179, 61, 74)

screen= pygame.display.set_mode( (WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Kolko - Krzyzyk')

def draw_line():
    global WIDTH, HEIGHT
    p=(WIDTH+HEIGHT)//120
    if p==0:
        p=1
    pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT//3), (WIDTH, HEIGHT//3), p)
    pygame.draw.line(screen, LINE_COLOR, (0, 2*HEIGHT//3), (WIDTH, 2*HEIGHT//3), p)
    pygame.draw.line(screen, LINE_COLOR, (WIDTH//3, 0), (WIDTH//3, HEIGHT), p)
    pygame.draw.line(screen, LINE_COLOR, (2*WIDTH//3, 0), (2*WIDTH//3, HEIGHT), p)

tablica = np.zeros((3, 3))
def zaznacz_na_tablicy(row, col, player):
    tablica[row][col] = player

def sprawdz_zapelnienie():
    for row in range(3):
        for col in range(3):
            if tablica[row][col]==0: return False
    return True 

def sprawdz_czy_wolne(row,col):
    if tablica[row][col]==0: return True
    else: return False

def sprawdz_wygrana():
    global HEIGHT,WIDTH
    grubosc=(HEIGHT+WIDTH)//60
    if grubosc==0:
        grubosc=1
    for x in range(3):
        if(tablica[x][0]==tablica[x][1]==tablica[x][2] and tablica[x][1]!=0): 
            pygame.draw.line(screen, RED, (WIDTH//40, (HEIGHT//6)+x*(HEIGHT//3)), ((WIDTH-WIDTH//40), (HEIGHT//6)+x*(HEIGHT//3)), grubosc)
            return True
        if(tablica[0][x]==tablica[1][x]==tablica[2][x] and tablica[1][x]!=0): 
            pygame.draw.line(screen, RED, ((WIDTH//6)+x*(WIDTH//3), HEIGHT//40), ((WIDTH//6)+x*(WIDTH//3), (HEIGHT-HEIGHT//40)), grubosc)
            return True
    if(tablica[0][0]==tablica[1][1]==tablica[2][2] and tablica[1][1]!=0): 
        pygame.draw.line(screen, RED, (WIDTH//40, HEIGHT//40), ((WIDTH-WIDTH//40), (HEIGHT-HEIGHT//40)), grubosc)
        return True
    if(tablica[0][2]==tablica[1][1]==tablica[2][0] and tablica[1][1]!=0): 
        pygame.draw.line(screen, RED, (WIDTH//40, (HEIGHT-HEIGHT//40)), ((WIDTH-WIDTH//40), HEIGHT//40), grubosc)   
        return True
    return False

def sprawdz_remis():
    for x in 3:
        for y in 3:
            if tablica[x][y]==0: return False
    return True


def restart():
    global BG_COLOR, WIDTH, HEIGHT
    # WIDTH=600
    # HEIGHT=600
    screen=pygame.display.set_mode( (WIDTH, HEIGHT), pygame.RESIZABLE)
    screen.fill(BG_COLOR)
    draw_line()
    global moves,koniec_gry,player
    moves=0
    koniec_gry=False
    player=randint(1,2)
    for row in range(3):
        for col in range(3):
            tablica[row][col]=0
    
def plansza():
    global BG_COLOR, WIDTH, HEIGHT, SIGN_COLOR, player, koniec_gry
    grubosc_czcionki=(WIDTH+HEIGHT)//40
    czcionka = pygame.font.SysFont("monospace", grubosc_czcionki)
    gracz=czcionka.render("Wygrales!!!", 3, (0, 0, 0))
    komputer=czcionka.render("Przegrales", 3, (0, 0, 0))
    remis=czcionka.render("Remis", 3, (0, 0, 0))
    
    screen=pygame.display.set_mode( (WIDTH, HEIGHT), pygame.RESIZABLE)
    screen.fill(BG_COLOR)
    draw_line()  
    grubosc=(WIDTH+HEIGHT)//40
    promien=min(WIDTH,HEIGHT)//8
    if grubosc==0:
        grubosc=1
    if promien==0:
        promien=1

    for i in range(3):
        for j in range(3):
            if tablica[i][j]==1:
                pygame.draw.line(screen, SIGN_COLOR, (WIDTH//15+j*(WIDTH//3), HEIGHT//15+i*(HEIGHT//3)), (int(WIDTH//3.75)+j*(WIDTH//3), int(HEIGHT//3.75)+i*(HEIGHT//3)), grubosc)
                pygame.draw.line(screen, SIGN_COLOR, (WIDTH//15+j*(WIDTH//3), int(HEIGHT//3.75)+i*(HEIGHT//3)), (int(WIDTH//3.75)+j*(WIDTH//3), HEIGHT//15+i*(HEIGHT//3)), grubosc)
            elif tablica[i][j]==2:
                pygame.draw.circle(screen, SIGN_COLOR, ((WIDTH//6)+j*(WIDTH//3), (HEIGHT//6)+i*(HEIGHT//3)), promien, grubosc)
    
    if sprawdz_wygrana()==True: 
        pygame.draw.rect(screen, (189, 180, 85), (WIDTH//3.33,HEIGHT//2.3,WIDTH//2.5,HEIGHT//7.5))
        if player==1:
            screen.blit(gracz, (WIDTH//2.8, HEIGHT//2.14))
        else:
            screen.blit(komputer, (WIDTH//2.8, HEIGHT//2.14))
        koniec_gry=True

    if sprawdz_zapelnienie() and koniec_gry==False:
        pygame.draw.rect(screen, (189, 180, 85), (WIDTH//3.33,HEIGHT//2.3,WIDTH//2.5,HEIGHT//7.5))
        screen.blit(remis, (WIDTH//2.35, HEIGHT//2.14))
        koniec_gry=True



def menu():
    def colory():
        pygame.draw.rect(screen, (0, 0, 0), (530,400,50,50))
        pygame.draw.rect(screen, (0, 0, 0), (530,470,50,50))
        pygame.draw.rect(screen, (0, 0, 0), (530,540,50,50))
        pygame.draw.rect(screen, (39, 186, 171), (535,405,40,40))
        pygame.draw.rect(screen, (170, 87, 189), (535,475,40,40))
        pygame.draw.rect(screen, (230, 80, 88), (535,545,40,40))
    screen= pygame.display.set_mode( (WIDTH, HEIGHT) )
    screen.blit(imp, (0, 0))
    pygame.display.flip()
    #screen.fill((204, 169, 73))
    colory()
    czcionka_menu=pygame.font.SysFont("monospace", 80)
    menu1=czcionka_menu.render("Witaj!", 3, (0 , 0, 0))


    pygame.draw.rect(screen, (88, 191, 219), (130,120,340,110))
    pygame.draw.rect(screen, (63, 235, 100), (150,127.5,300,95))
    text_menu = menu1.get_rect(center=(600/2, 175))
    screen.blit(menu1,text_menu)

    pygame.draw.rect(screen, BG_COLOR, (150,300,300,90))
    pygame.draw.rect(screen, BG_COLOR, (150,400,300,90))
    pygame.draw.rect(screen, (201, 222, 16), (200,500,200,90))

    czcionka_spis=pygame.font.SysFont("monospace", 55)
    latwy=czcionka_spis.render("Łatwy", 3 ,(133, 15, 38))
    text_latwy = latwy.get_rect(center=(600/2, 345))
    screen.blit(latwy,text_latwy)
    trudny=czcionka_spis.render("Trudny", 3 ,(133, 15, 38))
    text_trudny = trudny.get_rect(center=(600/2, 445))
    screen.blit(trudny,text_trudny)
    graj=czcionka_spis.render("GRAJ", 3 ,(133, 15, 38))
    text_graj = graj.get_rect(center=(600/2, 545))
    screen.blit(graj,text_graj)

def mozliwa_wygrana(t,x,y):
    x1,y1=None,None
    for a,b,c,d in [(0,1,0,2),(0,2,0,1),(1,0,2,0),(2,0,1,0)]:
        if t[(x+a)%3][(y+b)%3]==2 and sprawdz_czy_wolne((c+x)%3,(d+y)%3):
            return (c+x)%3,(d+y)%3
    if x==y:
        for a,b,c,d in [(1,1,2,2),(2,2,1,1)]:
            if t[(x+a)%3][(y+b)%3]==2 and sprawdz_czy_wolne((c+x)%3,(d+y)%3):
                return (c+x)%3,(d+y)%3
    if (x==1 and y==1) or (x%2==0 and y%2==0 and x!=y):
        for a,b,c,d in [(1,2,2,1),(2,1,1,2)]:
            if t[(x+a)%3][(y+b)%3]==2 and sprawdz_czy_wolne((c+x)%3,(d+y)%3):
                return (c+x)%3,(d+y)%3

    return x1,y1

def wymuszony(t,x,y):
    x1=None
    y1=None
    for a,b,c,d in [(0,1,0,2),(0,2,0,1),(1,0,2,0),(2,0,1,0)]:
        if t[(x+a)%3][(y+b)%3]==1 and sprawdz_czy_wolne((c+x)%3,(d+y)%3):
            return (c+x)%3,(d+y)%3
    
    if x==y:
        for a,b,c,d in [(1,1,2,2),(2,2,1,1)]:
            if t[(x+a)%3][(y+b)%3]==1 and sprawdz_czy_wolne((c+x)%3,(d+y)%3):
                return (c+x)%3,(d+y)%3
    if (x==1 and y==1) or (x%2==0 and y%2==0 and x!=y):
        for a,b,c,d in [(1,2,2,1),(2,1,1,2)]:
            if t[(x+a)%3][(y+b)%3]==1 and sprawdz_czy_wolne((c+x)%3,(d+y)%3):
                return (c+x)%3,(d+y)%3

    return x1,y1
    
moves=0
menu_bool=True
poziom=""
menu()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  
        if menu_bool==True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicX = event.pos[0] #x
                clicY = event.pos[1] #y
                if 150<clicX<450 and 300<clicY<390:
                    poziom="latwy"
                elif 150<clicX<450 and 400<clicY<490:
                    poziom="trudny"
                elif 200<clicX<400 and 500<clicY<590 and poziom!="":
                    menu_bool=False
                    restart()
                elif 535<clicX<575 and 405<clicY<445:
                    BG_COLOR=(39, 186, 171)
                    menu()
                elif 535<clicX<575 and 475<clicY<515:
                    BG_COLOR=(170, 87, 189)
                    menu()
                elif 535<clicX<575 and 545<clicY<585:
                    BG_COLOR=(230, 80, 88)
                    menu()
        else:
            if player==1 and koniec_gry==False: #player
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicX = event.pos[0] #x
                    clicY = event.pos[1] #y

                    clicked_col=int(clicX//(WIDTH//3))
                    clicked_row=int(clicY//(HEIGHT//3))
                    moves+=1
                    if sprawdz_czy_wolne(clicked_row, clicked_col):
                        zaznacz_na_tablicy(clicked_row, clicked_col, player)

                        plansza()
                        if koniec_gry==False:
                            player=2
                    x=clicked_row
                    y=clicked_col
                    
            elif player==2 and koniec_gry==False and sprawdz_zapelnienie: #computer
                x1=None
                if moves>=2 and poziom=="trudny":
                    x1,y1=mozliwa_wygrana(tablica,lastX,lastY)
                    if x1==None:
                        x1,y1=wymuszony(tablica,x,y)
        
                if x1!=None:
                    positionX=x1
                    positionY=y1
                else:
                    while True:
                        positionX=randint(0,2)
                        positionY=randint(0,2)
                        if sprawdz_czy_wolne(positionX, positionY):
                            break
                #time.sleep(1)
                moves+=1
                zaznacz_na_tablicy(positionX, positionY, player)
                lastX,lastY=positionX,positionY
                plansza()

                if koniec_gry==False:
                    player=1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: #restart
                    restart()

                if event.key == pygame.K_m: #powrót do menu
                    menu_bool=True
                    poziom=""
                    WIDTH,HEIGHT=600,600
                    menu()
            if event.type==pygame.VIDEORESIZE:
                WIDTH=event.w
                HEIGHT=event.h
                koniec_gry=False
                plansza()
        pygame.display.update()
