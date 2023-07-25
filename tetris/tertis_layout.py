import pygame

class print_screen(): # kwadrat 50 pix , 10x14
    def main(tab_main,WIDTH,HEIGHT,screen,BORDER_MAIN,square,tab_moving):
        w=0.625*WIDTH # 500
        h=20*square
        start_x=WIDTH//20
        start_y=HEIGHT//100
        pygame.draw.rect(screen,(50, 168, 82),(WIDTH//20-BORDER_MAIN,HEIGHT//100-BORDER_MAIN,w+2*BORDER_MAIN,h+2*BORDER_MAIN),BORDER_MAIN)
        pygame.draw.rect(screen,(0,0,0),(start_x,start_y,w,h))

        n=10
        m=20
        line=2
        for i in range(n+1):
            pygame.draw.line(screen,(55,51,111),(i*square+start_x-line//2,start_y),(i*square+start_x-line//2,start_y+h-line//2),line)

        for i in range(m+1):
            pygame.draw.line(screen,(55,51,111),(start_x,i*square+start_y-line//2),(w+start_x-line//2,i*square+start_y-line//2),line)

        for i in range(m):
            for j in range(n):
                if tab_moving[i][j]==1:
                    pygame.draw.rect(screen,(245, 66, 81),(start_x+line//2+j*square,start_y+line//2+i*square,square-line,square-line))

        for i in range(m):
            for j in range(n):
                if tab_main[i][j]==1:
                    pygame.draw.rect(screen,(58, 133, 119),(start_x+line//2+j*square,start_y+line//2+i*square,square-line,square-line))

    def menu(tab_next,WIDTH,HEIGHT,BORDER_MAIN,screen,score):
        start_x=0.625*WIDTH+BORDER_MAIN+40
        start_y=0
        # score
        pygame.draw.rect(screen,(135, 89, 73),(start_x+0.12*(WIDTH-start_x),0.215*HEIGHT,200,80))
        font_score = pygame.font.SysFont("monospace", 35, True)
        score_spec = font_score.render("Score: "+str(score),500,(145, 158, 25))
        score_pos = score_spec.get_rect(center=((start_x+WIDTH)//2, 0.25*HEIGHT))
        screen.blit(score_spec,score_pos)


        # next block
        w=WIDTH-start_x
        square_next=40

        font_next = pygame.font.SysFont("monospace", 30)
        next_spec = font_next.render("Next: ",500,(0,0,0))
        next_pos = next_spec.get_rect(center=(w*0.4+start_x, 0.4*HEIGHT))
        screen.blit(next_spec,next_pos)

        pygame.draw.rect(screen,(0,0,0),(start_x+w//2-2*square_next,HEIGHT*0.42,4*square_next,4*square_next))
        line=2
        for i in range(5):
            pygame.draw.line(screen,(55,51,111),(i*square_next+start_x+w//2-2*square_next,HEIGHT*0.42),(i*square_next+start_x+w//2-2*square_next,HEIGHT*0.42+4*square_next),line)

        for i in range(5):
            pygame.draw.line(screen,(55,51,111),(start_x+w//2-2*square_next,i*square_next+HEIGHT*0.42),(start_x+w//2+2*square_next,i*square_next+HEIGHT*0.42),line)
        
        for i in range(4):
            for j in range(4):
                if tab_next[i][j]==1:
                    pygame.draw.rect(screen,(58, 133, 119),(start_x+w//2-2*square_next+j*square_next+line,HEIGHT*0.42+line+i*square_next,square_next-line,square_next-line))


        # key
        key=["Controls: ",
        "Press space to start", 
        "UP - Rotate block ",
        "LEFT - Move left ",
        "RIGHT - Move right ",
        "DOWN - Move down"]
        n=len(key)
        space=20
        font_key = pygame.font.SysFont("monospace", 20)
        for i in range(n):
            key_spec = font_key.render(key[i],500,(145, 158, 25))
            # key_pos = key_spec.get_rect((WIDTH-start_x)*0.3+start_x, i*space+0.8*HEIGHT)
            screen.blit(key_spec,((WIDTH-start_x)*0.05+start_x, i*space+0.7*HEIGHT))
        # pygame.draw(key, (10, 10), (0,0,0))  

    
    def print_all(tab_main,tab_next,WIDTH,HEIGHT,screen,BORDER_MAIN,square,score,tab_moving):
        print_screen.main(tab_main,WIDTH,HEIGHT,screen,BORDER_MAIN,square,tab_moving)
        print_screen.menu(tab_next,WIDTH,HEIGHT,BORDER_MAIN,screen,score)