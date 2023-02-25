import pygame,sys
import time
from random import randint

# r - restart gry
# s - zapisuje stan gry
# t - przywraca zapis
# strzła w lewo - zmiana koloru
# strzała w dół - zmiana wartosci na planszy 

pygame.init()
font = pygame.font.Font('freesansbold.ttf', 40)
WIDTH = 630
HEIGHT = 630 
screen= pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Sudoku')
Line_Color=(8,8,8)
Screen_Color=(199, 48, 48)
Fields_Color=(166, 40, 86)
def draw_line():
    pygame.draw.line(screen, Line_Color, (0, 210), (630, 210), 10)
    pygame.draw.line(screen, Line_Color, (0, 420), (630, 420), 10)
    pygame.draw.line(screen, Line_Color, (210, 0), (210, 630), 10)
    pygame.draw.line(screen, Line_Color, (420, 0), (420, 630), 10)
    for i in range(10):
        pygame.draw.line(screen, Line_Color, (0, i*70), (630, 70*i), 5)
        pygame.draw.line(screen, Line_Color, (70*i, 0), (70*i, 630), 5)


# tablica=[[0,0,0,2,6,0,7,0,1],
#         [6,8,0,0,7,0,0,9,0],
#         [1,9,0,0,0,4,5,0,0],
#         [8,2,0,1,0,0,0,4,0],
#         [0,0,4,6,0,2,9,0,0],
#         [0,5,0,0,0,3,0,2,8],
#         [0,0,9,3,0,0,0,7,4],
#         [0,4,0,0,5,0,0,3,6],
#         [7,0,3,0,1,8,0,0,0]]
# tab=[[tablica[j][i] for i in range(9)] for j in range(9)]

colors=[[(199, 48, 48),(166, 40, 86)],
        [(9, 102, 35),(31, 173, 71)],
        [(145, 56, 17),(204, 100, 55)],
        [(50, 13, 115),(93, 31, 204)]]    

pos_colors=0
def ekran():
    global pos_colors
    screen.fill(colors[pos_colors][0])
    for i in range(9):
        for j in range(9):
            if tablica[i][j]==0:
                pygame.draw.rect(screen, colors[pos_colors][1], (j*70+3,i*70+3,65,65))
    draw_line()
    for i in range(9):
        for j in range(9):
            if not tab[i][j]==0:
                number=tab[i][j]
                text = font.render(str(number), True, ((91, 135, 166)))
                screen.blit(text, pygame.Vector2((j*70+25),(i*70+20)))

pos_values=0
def czy_mozna(x,y,num):
    for i in range(9):
        if tab[y][i]==num or tab[i][x]==num:
            return False
    x1=x//3
    y1=y//3
    for i in range(3):
        for j in range(3):
            if tab[y1*3+i][x1*3+j]==num:
                return False
    return True

def getCode(i):
    with open('sudoku_data.txt', 'r') as f:
             for index, line in enumerate(f):
                     if index == i:
                             code = line.strip()
                             return code
def stworz(n):
    t=[[0 for i in range(9)] for j in range(9)]
    p=81
    tmp=n
    for i in range(9):
        for j in range(9):
            n=tmp%10**p
            tmp=n//10**(p-1)
            t[i][j]=tmp
            p-=1
            tmp=n
    return t

def return_ze_zmiana():
    global pos_values
    n=int(getCode(pos_values))
    tablica=stworz(int(getCode(pos_values)))
    tab=[[tablica[j][i] for i in range(9)] for j in range(9)]
    return tablica,tab
tablica=[[0 for _ in range(9)] for _ in range(9)]
tab=[[0 for _ in range(9)] for _ in range(9)]
tablica,tab=return_ze_zmiana()
ekran()
last_x=None
cnt=36

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  

        if event.type == pygame.MOUSEBUTTONDOWN: #zaznaczneie pola
            X=event.pos[0]
            Y=event.pos[1]
            x=X//70
            y=Y//70
            if tablica[y][x]==0:
                if last_x!=None: 
                    pygame.draw.rect(screen, Fields_Color, (last_x*70+3,last_y*70+3,65,65))
                    ekran()
                pygame.draw.rect(screen, (166, 179, 71), (x*70+3,y*70+3,65,65))
                if tab[y][x]!=0:
                    text = font.render(str(tab[y][x]), True, ((91, 135, 166)))
                    screen.blit(text, pygame.Vector2((x*70+25),(y*70+20)))
                last_x=x
                last_y=y

        if event.type == pygame.KEYDOWN and last_x!=None:
            if 47<=event.key<=58: #event.key to znaki z klawiatury w kodzie ascii
                num=int(chr(event.key))
                if czy_mozna(last_x,last_y,num) or num==0:
                    if num==0 and tab[last_y][last_x]!=0:
                        cnt-=1
                    if num!=0 and tab[last_y][last_x]==0:
                        cnt+=1
                    tab[last_y][last_x]=num                    
                    ekran()
                else: #blad
                    pygame.draw.rect(screen, (150, 136, 26), (200,260,230,80))
                    text = font.render("BŁĄD", True, ((91, 135, 166)))
                    screen.blit(text, pygame.Vector2((260),(280)))
                    pygame.display.update()
                    time.sleep(2)
                    ekran()

        if cnt==81: #koniec gry
            pygame.draw.rect(screen, (150, 136, 26), (150,260,330,80))
            text = font.render("Brawo wygrałeś!", True, ((91, 135, 166)))
            screen.blit(text, pygame.Vector2((158),(278)))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r: #restart
                tab=[[tablica[j][i] for i in range(9)] for j in range(9)]
                sub=False
                cnt=36
            elif event.key==pygame.K_s: #zapisz stan planszy
                t=[[tab[j][i] for i in range(9)] for j in range(9)]
                sub=True
                cnt_sub=cnt
            elif event.key==pygame.K_t and sub==True: # pokaz zapis
                tab=[[t[j][i] for i in range(9)] for j in range(9)]
                cnt=cnt_sub
            if event.key==pygame.K_RIGHT: #zmiana koloru
                pos_colors+=1
                if pos_colors == 4:
                    pos_colors=0
                    
            if event.key==pygame.K_DOWN: #zmien wartosci na planszy
                pos_values+=1
                sub=False
                if pos_values==3:
                    pos_values=0
                tablica,tab=return_ze_zmiana()

                
            ekran()
        pygame.display.update()