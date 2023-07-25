import pygame


class moving_block():
    def can_move_down(tab_moving,tab_main,left,right,down,up):
        for i in range(left,right+1):
            for j in range(down,up-1,-1):
                if tab_moving[j][i]==1:
                    if tab_main[j+1][i]==0:
                        break
                    else:
                        return False
                    
        return True

    def move_down(tab_moving,left,right,down,up):
        for i in range(down,up-1,-1):
            for j in range(left,right+1):
                if tab_moving[i][j]==1:
                    tab_moving[i][j]=0
                    tab_moving[i+1][j]=1
        down+=1
        up+=1
        return tab_moving,left,right,down,up

    def can_move_left(tab_moving,tab_main,left,right,down,up):
        for i in range(up,down+1):
            for j in range(left,right+1):
                if tab_moving[i][j]==1:
                    if tab_main[i][j-1]==0:
                        break
                    else:
                        return False
        return True

    def move_left(tab_moving,left,right,down,up):
        for i in range(down,up-1,-1):
            for j in range(left,right+1):
                if tab_moving[i][j]==1:
                    tab_moving[i][j]=0
                    tab_moving[i][j-1]=1
            
        left-=1
        right-=1
        return tab_moving,left,right,down,up


    def can_move_right(tab_moving,tab_main,left,right,down,up):
        for i in range(up,down+1):
            for j in range(right,left-1,-1):
                if tab_moving[i][j]==1:
                    if tab_main[i][j+1]==0:
                        break
                    else:
                        return False
        return True
    
    def move_right(tab_moving,left,right,down,up):
        for i in range(down,up-1,-1):
            for j in range(right,left-1,-1):
                if tab_moving[i][j]==1:
                    tab_moving[i][j]=0
                    tab_moving[i][j+1]=1
            
        left+=1
        right+=1
        return tab_moving,left,right,down,up
    