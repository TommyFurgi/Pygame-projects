import pygame, sys
from tertis_layout import print_screen
from moving_block import moving_block
from rotate import rotate
from random import randint
import time
from collections import deque
pygame.init()

WIDTH=800
HEIGHT=1020
BORDER_MAiN=7
square=50
screen= pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('TETRIS')


bg = pygame.image.load('bg.jpg')
bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))
screen.blit(bg,(0,0))

score = 0
tab_main=[[0 for _ in range(10)] for _ in range(20)]
tab_next=[[0 for _ in range(4)] for _ in range(4)]
tab_moving=[[0 for _ in range(10)] for _ in range(20)]
tab_shapes=['o','i','s','z','l','j','t']
shapes_number=len(tab_shapes)
game_running=False
block_moving=False
end_game=False
queue=deque()
bg = pygame.image.load('bg.jpg')
bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))
screen.blit(bg,(0,0))

def create_next(tab_shapes,tab_next):
    tab_next=[[0 for _ in range(4)] for _ in range(4)]
    shapes_number=len(tab_shapes)
    index=randint(0,shapes_number-1)
    shape=tab_shapes[index]
    left=4
    right=5
    match shape:
        case 'o':
            tab_next=[[1,1,0,0],
                      [1,1,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
            down=1
        case 'i':
            tab_next=[[1,0,0,0],
                      [1,0,0,0],
                      [1,0,0,0],
                      [1,0,0,0]]
            right=4
            down=3
        case 's':
            tab_next=[[0,1,1,0],
                      [1,1,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
            right=6
            down=1
        case 'z':
            tab_next=[[1,1,0,0],
                      [0,1,1,0],
                      [0,0,0,0],
                      [0,0,0,0]]
            right=6
            down=1
        case 'l':
            tab_next=[[1,0,0,0],
                      [1,0,0,0],
                      [1,1,0,0],
                      [0,0,0,0]]
            down=2
        case 'j':
            tab_next=[[0,1,0,0],
                      [0,1,0,0],
                      [1,1,0,0],
                      [0,0,0,0]]
            down=2
        case 't':
            tab_next=[[1,1,1,0],
                      [0,1,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
            down=1
            right=6
    return tab_next,left,right,down,shape


def set_next(tab_moving,next_left,next_right,next_down):
    left=next_left
    right=next_right
    down=next_down
    up=0
    for i in range(down+1):
        for j in range(left,right+1):
            if tab_next[i][j-left]:
                tab_moving[i][j]=1

    return tab_moving,left,right,down,up

def overlapping(tab_main,tab_moving,curr):
    left,right,down,up=curr

    for i in range(up,down+1):
        for j in range(left,right+1):
            if tab_main[i][j]==1 and tab_moving[i][j]==1:                
                return True
            
    return False

def change_moving_block(tab_moving,tab_next,next_left,next_right,next_down,right,down):
    for i in range(down+1):
        for j in range(right+1):
            tab_moving[i][j]=0

    tab_moving,left,right,down,up=set_next(tab_moving,next_left,next_right,next_down)
    curr=(left,right,down,up)

    return tab_moving,tab_next,curr
    
def add_score(tab_main,score,queue,down,up):
    count=0
    index=None
    for i in range(down,up-1,-1):
        cnt=0
        for j in range(10):
            if tab_main[i][j]==1:
                cnt+=1

        if cnt==10:
            score+=10
            queue.append(i+len(queue))
            tab_main[i]=[0 for _ in range(10)]
    return queue,tab_main,score

def check_end_game(tab_main):
    for i in range(10):
        if tab_main[0][i]==1:
            return True
    
    return False


tab_next,next_left,next_right,next_down,shape_next=create_next(tab_shapes,tab_next)
clock = pygame.time.Clock() 
screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 220)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame,quit()
            sys.exit()  

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_running and not end_game: # game start
                game_running=True
                        
                tab_moving,tab_next,curr=change_moving_block(tab_moving,tab_next,next_left,next_right,next_down,right=-1,down=-1)
                shape=shape_next
                pos=1
                left,right,down,up=curr

                tab_next,next_left,next_right,next_down,shape_next=create_next(tab_shapes,tab_next)

                block_moving=True


            if event.key == pygame.K_SPACE and not game_running and end_game: # restart
                tab_main=[[0 for _ in range(10)] for _ in range(20)]
                tab_moving=[[0 for _ in range(10)] for _ in range(20)]
                tab_next,next_left,next_right,next_down,shape_next=create_next(tab_shapes,tab_next)
                pos=1
                score=0
                end_game=False


            if game_running and event.key == pygame.K_LEFT and left!=0 and moving_block.can_move_left(tab_moving,tab_main,left,right,down,up): # move left
                tab_moving,left,right,down,up=moving_block.move_left(tab_moving,left,right,down,up)

            elif game_running and event.key == pygame.K_RIGHT and right!=9 and moving_block.can_move_right(tab_moving,tab_main,left,right,down,up): # move left
                tab_moving,left,right,down,up=moving_block.move_right(tab_moving,left,right,down,up)

            elif game_running and event.key == pygame.K_DOWN and down<19 and moving_block.can_move_down(tab_moving,tab_main,left,right,down,up): # move down
                tab_moving,left,right,down,up=moving_block.move_down(tab_moving,left,right,down,up)

            elif game_running and event.key == pygame.K_UP: # rotate 
                curr=(left,right,down,up)
                tab_moving,curr,pos=rotate.rotate(shape,tab_main,tab_moving,curr,pos)
                left,right,down,up=curr

        if event.type == screen_update:
            
            if not end_game and game_running and block_moving:
                if down<19 and moving_block.can_move_down(tab_moving,tab_main,left,right,down,up): # defult moving down

                    tab_moving,left,right,down,up=moving_block.move_down(tab_moving,left,right,down,up)


                else: # cant move down anymore
                    for i in range(down,up-1,-1):
                        for j in range(left,right+1):
                            if tab_moving[i][j]==1:
                                tab_moving[i][j]=0
                                tab_main[i][j]=1

                    block_moving=False
                


            if not end_game and game_running and not block_moving: # moving blocks after adding score
                if len(queue)!=0:
                    index=queue.popleft()
                    for i in range(index-1,-1,-1):
                        for j in range(10):
                            tab_main[i+1][j]=tab_main[i][j]

                

                if len(queue)==0 and check_end_game(tab_main): # end game checking
                    game_running=False
                    end_game=True
                    continue


                queue,tab_main,score=add_score(tab_main,score,queue,down,up)
                if len(queue)==0:

                    tab_moving,tab_next,curr=change_moving_block(tab_moving,tab_next,next_left,next_right,next_down,right,down)
                    shape=shape_next
                    pos=1
                    left,right,down,up=curr

                    if game_running and overlapping(tab_main,tab_moving,curr): # check overlapping
                        game_running=False
                        end_game=True
                        continue
                    else:     
                        tab_next,next_left,next_right,next_down,shape_next=create_next(tab_shapes,tab_next)
                        block_moving=True
                    


    print_screen.print_all(tab_main,tab_next,WIDTH,HEIGHT,screen,BORDER_MAiN,square,score,tab_moving)

      
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
