import pygame, sys

pygame.init()
b_king = pygame.image.load('imgs_chess/b_king.png')
b_queen = pygame.image.load('imgs_chess/b_queen.png')
b_bishop = pygame.image.load('imgs_chess/b_bishop.png')
b_knight = pygame.image.load('imgs_chess/b_knight.png')
b_pawn = pygame.image.load('imgs_chess/b_pawn.png')
b_rook = pygame.image.load('imgs_chess/b_rook.png')
w_king = pygame.image.load('imgs_chess/w_king.png')
w_queen = pygame.image.load('imgs_chess/w_queen.png')
w_bishop = pygame.image.load('imgs_chess/w_bishop.png')
w_knight = pygame.image.load('imgs_chess/w_knight.png')
w_pawn = pygame.image.load('imgs_chess/w_pawn.png')
w_rook = pygame.image.load('imgs_chess/w_rook.png')
b_king = pygame.transform.scale(b_king, (70, 70))
b_queen = pygame.transform.scale(b_queen, (70, 70))
b_bishop = pygame.transform.scale(b_bishop, (70, 70))
b_knight = pygame.transform.scale(b_knight, (70, 70))
b_pawn = pygame.transform.scale(b_pawn, (70, 70))
b_rook = pygame.transform.scale(b_rook, (70, 70))
w_king = pygame.transform.scale(w_king, (70, 70))
w_queen = pygame.transform.scale(w_queen, (70, 70))
w_bishop = pygame.transform.scale(w_bishop, (70, 70))
w_knight = pygame.transform.scale(w_knight, (70, 70))
w_pawn = pygame.transform.scale(w_pawn, (70, 70))
w_rook = pygame.transform.scale(w_rook, (70, 70))

tablica=[["br","bk","bb","bq","bi","bb","bk","br"],
        ["bp","bp","bp","bp","bp","bp","bp","bp"],
        ["","","","","","","",""],
        ["","","","","","","",""],
        ["","","","","","","",""],
        ["","","","","","","",""],
        ["wp","wp","wp","wp","wp","wp","wp","wp"],
        ["wr","wk","wb","wq","wi","wb","wk","wr"]]
tab=[[tablica[i][j] for j in range(8)] for i in range(8)]
WIDTH = 600
HEIGHT = 600
GREEN=(6, 89, 35)
WHITE=(150, 158, 171)
YELLOW=(148, 144, 44)
RED=(168, 39, 32)

screen= pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('CHESS')


def plansza():
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0:
                pygame.draw.rect(screen,WHITE,(i*75,j*75,75,75))
            else:
                pygame.draw.rect(screen,GREEN,(i*75,j*75,75,75))
            match tablica[j][i]:
                case "br":
                    screen.blit(b_rook,(i*75,j*75))
                case "bk":
                    screen.blit(b_knight,(i*75,j*75))
                case "bb":
                    screen.blit(b_bishop,(i*75,j*75))
                case "bi":
                    if czy_szach(i,j,"w"):
                        pygame.draw.rect(screen,RED,(i*75,j*75,75,75))
                    screen.blit(b_king,(i*75,j*75))
                case "bq":
                    screen.blit(b_queen,(i*75,j*75))
                case "bp":
                    screen.blit(b_pawn,(i*75,j*75))
                case "wp":
                    screen.blit(w_pawn,(i*75,j*75))
                case "wr":
                    screen.blit(w_rook,(i*75,j*75))
                case "wk":
                    screen.blit(w_knight,(i*75,j*75))    
                case "wb":
                    screen.blit(w_bishop,(i*75,j*75))
                case "wi":
                    if czy_szach(i,j,"b"):
                        pygame.draw.rect(screen,RED,(i*75,j*75,75,75))
                    screen.blit(w_king,(i*75,j*75))
                case "wq":
                    screen.blit(w_queen,(i*75,j*75))

def czy_mozna(x,y,x1,y1):
    global tablica
    if tablica[y1][x1]!="" and tablica[y][x][0]==tablica[y1][x1][0]:
        return False

    if tablica[y][x][1]=="r":
        if x!=x1 and y!=y1:
            return False
        znak=1
        if x<x1 or y<y1:
            znak=-1
        if y==y1:
            for i in range(0,x-x1,znak):
                if tablica[y][x1+i]!="" and x1!=x+i and x!=x+i:
                    return False
        else:
            for i in range(0,y-y1,znak):
                if tablica[y1+i][x]!="" and y1!=y+i and y!=y+i:
                    return False  
        return True

    if tablica[y][x][1]=="b":
        if abs(x-x1)!=abs(y-y1):
            return False
        
        znakx=1
        znaky=1
        if x1>x:
            znakx=-1
        if (y1>y and znakx==1) or (y1<y and znakx==-1):
            znaky=-1
       
        for i in range(0,(x-x1)-1,znakx):
            if tablica[y1+(i)*znaky][x1+i]!="" and x1+i!=x and x1!=x1+i:
                return False
        
        return True
        
    if tablica[y][x][1]=="k":
        for i,j in[(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]:
            if x+i==x1 and y+j==y1:
                return True
        return False
    
    if tablica[y][x][1]=="i":
        if y==y1 and abs(x1-x)==2 and (y==0 or y==7): # roszada
            for i in last_moves:
                if i[0]==x and i[1]==y:
                    return False

            przeciwny="w"
            if tablica[y][x][0]=="w":
                przeciwny="b"

            if x1<x:
                for i in last_moves:
                    if i[0]==0 and i[1]==y:
                        return False
                if czy_szach(1,y,przeciwny):
                    return False
            else:
                for i in last_moves:
                    if i[0]==7 and i[1]==y:
                        return False

            if tablica[y1][x1]!="" or tablica[y1][(x1+x)//2]!="":
                return False
                
            if czy_szach(x,y,przeciwny) or czy_szach(x1,y1,przeciwny) or czy_szach((x+x1)//2,y1,przeciwny):
                return False

            return True

        if abs(x-x1)>1 or abs(y-y1)>1:
            return False
        return True
    
    if tablica[y][x][1]=="q":
        if x==x1 or y==y1:      
            znak=1
            if x<x1 or y<y1:
                znak=-1
            if y==y1:
                for i in range(0,x-x1,znak):
                    if tablica[y][x1+i]!="" and x1!=x+i and x!=x+i:
                        return False
            else:
                for i in range(0,y-y1,znak):
                    if tablica[y1+i][x]!="" and y1!=y+i and y!=y+i:
                        return False  
            return True
        elif abs(x-x1)==abs(y-y1):
            znakx=1
            znaky=1
            if x1>x:
                znakx=-1
            if (y1>y and znakx==1) or (y1<y and znakx==-1):
                znaky=-1
        
            for i in range(0,(x-x1),znakx):
                if tablica[y1+(i)*znaky][x1+i]!="" and x1+i!=x and x1!=x1+i:
                    return False
            
            return True
        else:
            return False
        
    if tablica[y][x][1]=="p": 
        if tablica[y][x][0]=="w":
            kolor=1
        else:
            kolor=-1
        if abs(x-x1)==1 and y-kolor==y1 and tablica[y1][x1]!="" and tablica[y1][x1][0]!=tablica[y][x][0]:
            return True
        elif x==x1 and tablica[y1][x1]=="":
            if y-kolor==y1:
                return True
            if y-2*kolor==y1 and (y==1 or y==6) and tablica[y-kolor][x1]=="":
                return True

        n=len(last_moves)
        if n>1:
            s=last_moves[n-1]
            if abs(x-x1)==1 and y-kolor==y1 and tablica[y1][x1]=="":
                if tablica[s[3]][s[2]][1]=="p" and s[0]==x1 and s[3]==y1+kolor and abs(s[1]-s[3])==2:
                    return True

        return False 

def pole_przemiany(x,y):
    pygame.draw.rect(screen,YELLOW,(x*75,abs(y)*75,75,75))
    pygame.draw.rect(screen,YELLOW,(x*75,abs(y-1)*75,75,75))
    pygame.draw.rect(screen,YELLOW,(x*75,abs(y-2)*75,75,75))
    pygame.draw.rect(screen,YELLOW,(x*75,abs(y-3)*75,75,75))
    if tablica[y][x][0]=="w":
        screen.blit(w_queen,(x*75,abs(y)*75))
        screen.blit(w_rook,(x*75,abs(y-1)*75))
        screen.blit(w_bishop,(x*75,abs(y-2)*75))
        screen.blit(w_knight,(x*75,abs(y-3)*75))
    else:
        screen.blit(b_queen,(x*75,abs(y)*75))
        screen.blit(b_rook,(x*75,abs(y-1)*75))
        screen.blit(b_bishop,(x*75,abs(y-2)*75))
        screen.blit(b_knight,(x*75,abs(y-3)*75))
    x1=10
    y1=10
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()   
            if event.type == pygame.MOUSEBUTTONDOWN: 
                X=event.pos[0]
                Y=event.pos[1]
                x1=X//75
                y1=Y//75
                wynik=tablica[y][x][0]
                if x==x1 and y1==y:
                    tablica[y][x]=wynik+"q"
                if x==x1 and y1==abs(y-1):
                    tablica[y][x]=wynik+"r"
                if x==x1 and y1==abs(y-2):
                    tablica[y][x]=wynik+"b"
                if x==x1 and y1==abs(y-3):
                    tablica[y][x]=wynik+"k"
        if x1==x and (y1==abs(y) or y1==abs(y-1) or y1==abs(y-2) or y1==abs(y-3)):
            break
        pygame.display.update()


def czy_szach(x,y,kolor):
    for i in range(8):
        for j in range(8):
            if tablica[i][j]!="" and tablica[i][j][0]==kolor:
                s=tablica[i][j][1]
                if czy_mozna(j,i,x,y) and s!="i":
                    if s!="p" or j!=x:
                        return True
    return False

def king_pos(kolor):
    for i in range(8):
        for j in range(8):
            if tablica[i][j]!="" and tablica[i][j][1]=="i" and tablica[i][j][0]==kolor:
                return j,i
        
def koniec(kolor=None):
    if kolor==None:
        n="Remis"
    elif kolor=="w":
        n="Biały wygrał!"
    else:
        n="Czarny wygrał!"
    pygame.draw.rect(screen,YELLOW,(150,250,300,105))
    czcionka=pygame.font.SysFont("monospace", 36)
    napis=czcionka.render(n, 3 ,(133, 15, 38))
    text = napis.get_rect(center=(600/2, 300))
    screen.blit(napis,text)

def pat(obecny_kolor,przeciwny_kolor):
    n=len(last_moves)
    if n>=10: # pat z powtorzenia
        if last_moves[n-1]==last_moves[n-5]==last_moves[n-9] and last_moves[n-2]==last_moves[n-6]==last_moves[n-10] and last_moves[n-3]==last_moves[n-7] and last_moves[n-4]==last_moves[n-8]:
            return True


    ile_figur_obecny_kolor=0
    ile_figur_lekkich_obecny_kolor=0
    ile_figur_przeciwny_kolor=0

    figura=przeciwny_kolor+"i"
    king_x,king_y=king_pos(przeciwny_kolor)
    tablica[king_y][king_x]=""
    for i,j in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]:
        if 0<=(king_x+i)<8 and 0<=(king_y+j)<8 and (tablica[king_y+j][king_x+i]=="" or tablica[king_y+j][king_x+i][0]==obecny_kolor):
            tmp=tablica[king_y+j][king_x+i]
            tablica[king_y+j][king_x+i]=figura
            if not czy_szach(king_x+i,king_y+j,obecny_kolor):
                tablica[king_y+j][king_x+i]=tmp
                tablica[king_y][king_x]=figura
                return False
            tablica[king_y+j][king_x+i]=tmp
    tablica[king_y][king_x]=figura

    for i in range(8):
        for j in range(8):    
            if tablica[i][j]!="":
                if tablica[i][j][0]==przeciwny_kolor:
                    ile_figur_przeciwny_kolor+=1
                if tablica[i][j][0]==obecny_kolor:
                    ile_figur_obecny_kolor+=1
                    if tablica[i][j][1]=="k" or tablica[i][j][1]=="b":
                        ile_figur_lekkich_obecny_kolor+=1
                
                if tablica[i][j][1]!="i" and tablica[i][j][0]==przeciwny_kolor:
                    for a,b in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]:
                        if czy_mozna(j,i,j+a,i+b):
                            tmp=tablica[i+b][j+a]
                            tablica[i+b][j+a]=tablica[i][j]
                            tablica[i][j]=""
                            if not czy_szach(king_x,king_y,obecny_kolor):
                                tablica[i][j]=tablica[i+b][j+a]
                                tablica[i+b][j+a]=tmp
                                return False
                            tablica[i][j]=tablica[i+b][j+a]
                            tablica[i+b][j+a]=tmp
                    

    if ile_figur_przeciwny_kolor==1 and (ile_figur_obecny_kolor==1 or (ile_figur_obecny_kolor==2 and ile_figur_lekkich_obecny_kolor==1)):
        return True
    
    
    return True


def mat(king_x,king_y,obecny_kolor,przeciwny_kolor):    
    figura=przeciwny_kolor+"i"
    tablica[king_y][king_x]=""
    for i,j in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]:
        if 0<=(king_x+i)<8 and 0<=(king_y+j)<8 and (tablica[king_y+j][king_x+i]=="" or tablica[king_y+j][king_x+i][0]==obecny_kolor):
            tmp=tablica[king_y+j][king_x+i]
            tablica[king_y+j][king_x+i]=figura
            if not czy_szach(king_x+i,king_y+j,obecny_kolor):
                tablica[king_y+j][king_x+i]=tmp
                tablica[king_y][king_x]=figura
                return False
            tablica[king_y+j][king_x+i]=tmp
    tablica[king_y][king_x]=figura
    tab_szach=[]
    for i in range(8):
        for j in range(8):
            if tablica[i][j]!="" and tablica[i][j][0]==obecny_kolor:
                s=tablica[i][j][1]
                if czy_mozna(j,i,king_x,king_y) and s!="i":
                    if s!="p" or j!=king_x:
                        tab_szach.append((j,i))

    if len(tab_szach)>1:
        return True

    szach_x,szach_y=tab_szach[0]
    
    if tablica[szach_y][szach_x][1]=="k" or tablica[szach_y][szach_x][1]=="p":
        return False

    if szach_x==king_x or szach_y==king_y:
        znak=1
        if szach_x<king_x or szach_y<king_y:
            znak=-1
        if szach_y==king_y:
            for i in range(0,szach_x-king_x+znak,znak):
                for a in range(8):
                    for b in range(8):
                        if tablica[a][b]!="" and tablica[a][b][0]==przeciwny_kolor:
                            if czy_mozna(b,a,king_x+i,king_y) and not czy_szach(king_x,king_y,obecny_kolor):
                                print(b,a,king_x+i,king_y)
                                return False
        else:
            for i in range(0,szach_y-king_y+znak,znak):
                for a in range(8):
                    for b in range(8):
                        if tablica[a][b]!="" and tablica[a][b][0]==przeciwny_kolor:
                            if czy_mozna(b,a,king_x,king_y+i) and not czy_szach(king_x,king_y,obecny_kolor):
                                return False

    if abs(king_x-szach_x)==abs(king_y-szach_y):
        znakx=1
        znaky=1
        if king_x>szach_x:
            znakx=-1
        if (king_y>szach_y and znakx==1) or (king_y<szach_y and znakx==-1):
            znaky=-1
       
        for i in range(0,szach_x-king_x+znakx,znakx):
            for a in range(8):
                    for b in range(8):
                        if tablica[a][b]!="" and tablica[a][b][0]==przeciwny_kolor and tablica[a][b][1]!="i":
                            if czy_mozna(b,a,king_x+i,king_y+(i)*znaky) and not czy_szach(king_x,king_y,obecny_kolor):
                                return False                

    return True

szach=False
player="w"
kolor_przeciwny="b"
last_x,last_y,x=None,None,None
koniec_gry=False
last_moves=[]
plansza()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  
        if event.type == pygame.MOUSEBUTTONDOWN and not koniec_gry: 
            if x!=None:
                last_x,last_y=x,y
            X=event.pos[0]
            Y=event.pos[1]
            x=X//75
            y=Y//75
            if last_x!=None and tablica[last_y][last_x]!="" and player==tablica[last_y][last_x][0]:
                if czy_mozna(last_x,last_y,x,y):
                    tmp_piece=tablica[y][x]
                    tablica[y][x]=tablica[last_y][last_x]
                    tablica[last_y][last_x]=""
                    kingX,kingY=king_pos(player)
                    if czy_szach(kingX,kingY,kolor_przeciwny):
                        tablica[last_y][last_x]=tablica[y][x]
                        tablica[y][x]=tmp_piece
                    else:
                        dzialanie=""
                        if  tablica[y][x][1]=="p" and tmp_piece=="" and abs(x-last_x)==1: # bicie w przelocie
                            tablica[y-1][x]=""
                            tablica[y+1][x]=""
                            dzialanie="bicie_w_przelocie"
                        if tablica[y][x][1]=="i" and abs(last_x-x)==2: #roszada
                            if last_x>x:
                                tmp=tablica[y][0]
                                tablica[y][0]=""
                            else:
                                tmp=tablica[y][7]
                                tablica[y][7]=""
                            tablica[y][(x+last_x)//2]=tmp
                            dzialanie="roszada"
                        if tablica[y][x][1]=="p" and (y==0 or y==7): #pole przemiany
                            pole_przemiany(x,y)
                            dzialanie="przemiana"
                        last_moves.append((last_x,last_y,x,y,tmp_piece,dzialanie))
                        plansza()
                        kingX,kingY=king_pos(kolor_przeciwny)
                        if czy_szach(kingX,kingY,player):
                            if mat(kingX,kingY,player,kolor_przeciwny):
                                koniec(player)
                                koniec_gry=True
                        elif pat(player,kolor_przeciwny):
                            koniec_gry=True
                            koniec()

                        player,kolor_przeciwny=kolor_przeciwny,player

        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_r: #restart
                tablica=[[tab[j][i] for i in range(8)] for j in range(8)]
                player="w"
                kolor_przeciwny="b"
                last_x,last_y,x=None,None,None
                koniec_gry=False
                last_moves=[]
                plansza()
            if event.key==pygame.K_RIGHT and len(last_moves)>0: #cofnij ruch
                n=len(last_moves)
                s=last_moves[n-1]
                tablica[s[1]][s[0]]=tablica[s[3]][s[2]]
                tablica[s[3]][s[2]]=s[4]
                if s[5]=="przemiana":
                    tablica[s[1]][s[0]]=tablica[s[1]][s[0]][0]+"p"
                elif s[5]=="bicie_w_przelocie":
                    tablica[s[1]][s[2]]=player+"p"
                elif s[5]=="roszada":
                    if s[0]>s[2]:
                        tablica[s[1]][0]=tablica[s[1]][(s[0]+s[2])//2]
                    else:
                        tablica[s[1]][7]=tablica[s[1]][(s[0]+s[2])//2]
                    tablica[s[1]][(s[0]+s[2])//2]=""
                last_moves.pop()
                player,kolor_przeciwny=kolor_przeciwny,player 
                plansza()
        pygame.display.update()
