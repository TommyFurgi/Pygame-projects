import pygame

# ['o','i','s','z','l','j','t']
class rotate():
    def rotate(shape,tab_main,tab_moving,curr,pos):
        tab_rotate=[[0 for _ in range(10)] for _ in range(20)]
        left,right,down,up=curr

        match shape:
            case 'o':
                return tab_moving,curr,pos
            
            case 'i':
                if pos==1: # pion
                    if left+3>9:
                        return tab_moving,curr,pos
                    
                    if tab_main[up][left]==1 or tab_main[up][left+1]==1 or tab_main[up][left+2]==1 or tab_main[up][left+3]==1:
                        return tab_moving,curr,pos
                    
                    tab_rotate[up][left]=1
                    tab_rotate[up][left+1]=1
                    tab_rotate[up][left+2]=1
                    tab_rotate[up][left+3]=1

                    return tab_rotate,(left,left+3,up,up),0         
                
                else: # poziom
                    if up+3>19:
                        return tab_moving,curr,pos
                    
                    if tab_main[up][left]==1 or tab_main[up+1][left]==1 or tab_main[up+2][left]==1 or tab_main[up+3][left]==1:
                        return tab_moving,curr,pos
                    
                    tab_rotate[up][left]=1
                    tab_rotate[up+1][left]=1
                    tab_rotate[up+2][left]=1
                    tab_rotate[up+3][left]=1

                    return tab_rotate,(left,left,up+3,up),1
        
            case 's':
                if pos==1: 
                    if up+2>19:
                        return tab_moving,curr,pos
                    
                    if tab_main[up][left]==1 or tab_main[up+1][left]==1 or tab_main[up+1][left+1]==1 or tab_main[up+2][left+1]==1:
                        return tab_moving,curr,pos
                    tab_rotate[up][left]=1
                    tab_rotate[up+1][left]=1
                    tab_rotate[up+1][left+1]=1
                    tab_rotate[up+2][left+1]=1
                    
                    return tab_rotate,(left,left+1,up+2,up),0
                
                else:
                    if left+2>9:
                        return tab_moving,curr,pos
                    
                    if tab_main[up][left+1]==1 or tab_main[up][left+2]==1 or tab_main[up+1][left]==1 or tab_main[up+1][left+1]==1:
                        return tab_moving,curr,pos
                    
                    tab_rotate[up][left+1]=1
                    tab_rotate[up][left+2]=1
                    tab_rotate[up+1][left]=1
                    tab_rotate[up+1][left+1]=1
                    
                    return tab_rotate,(left,left+2,up+1,up),1
            
            case 'z':
                if pos==1: 
                    if up+2>19:
                        return tab_moving,curr,pos
                    
                    if tab_main[up][left+1]==1 or tab_main[up+1][left]==1 or tab_main[up+1][left+1]==1 or tab_main[up+2][left]==1:
                        return tab_moving,curr,pos
                    
                    tab_rotate[up][left+1]=1
                    tab_rotate[up+1][left]=1
                    tab_rotate[up+1][left+1]=1
                    tab_rotate[up+2][left]=1
                    
                    return tab_rotate,(left,left+1,up+2,up),0
                else:
                    if left+2>9:
                        return tab_moving,curr,pos
                    
                    if tab_main[up][left]==1 or tab_main[up][left+1]==1 or tab_main[up+1][left+1]==1 or tab_main[up+1][left+2]==1:
                        return tab_moving,curr,pos
                    
                    tab_rotate[up][left]=1
                    tab_rotate[up][left+1]=1
                    tab_rotate[up+1][left+1]=1
                    tab_rotate[up+1][left+2]=1
                    
                    return tab_rotate,(left,left+2,up+1,up),1
                
            case 'l':
                if pos==1: 
                    if left+2>9 or up==0:
                        return tab_moving,curr,pos
                    
                    if tab_main[up-1][left+2]==1 or tab_main[up][left]==1 or tab_main[up][left+1]==1 or tab_main[up][left+2]==1:
                        return tab_moving,curr,pos
                    
                    tab_rotate[up][left]=1
                    tab_rotate[up][left+1]=1
                    tab_rotate[up][left+2]=1
                    tab_rotate[up-1][left+2]=1
                    
                    return tab_rotate,(left,left+2,up,up-1),2
                
                elif pos==2:
                    if up+1>9 or up==0:
                        return tab_moving,curr,pos
                    
                    if tab_main[up-1][left]==1 or tab_main[up-1][left+1]==1 or tab_main[up][left+1]==1 or tab_main[up+1][left+1]==1:
                        return tab_moving,curr,pos
                    
                    tab_rotate[up-1][left]=1
                    tab_rotate[up-1][left+1]=1
                    tab_rotate[up][left+1]=1
                    tab_rotate[up+1][left+1]=1
                    
                    return tab_rotate,(left,left+1,up+1,up-1),3

                elif pos==3:
                    if left+2>9:
                        return tab_moving,curr,pos
                    
                    if tab_main[up][left]==1 or tab_main[up][left+1]==1 or tab_main[up][left+2]==1 or tab_main[up+1][left]==1:
                        return tab_moving,curr,pos
                    
                    tab_rotate[up][left]=1
                    tab_rotate[up][left+1]=1
                    tab_rotate[up][left+2]=1
                    tab_rotate[up+1][left]=1
                    
                    return tab_rotate,(left,left+2,up+1,up),0
                
                else:
                    if up+2>19 or up==0:
                        return tab_moving,curr,pos
                    
                    if tab_main[up-1][left]==1 or tab_main[up][left]==1 or tab_main[up+1][left]==1 or tab_main[up+1][left+1]==1:
                        return tab_moving,curr,pos
                    
                    tab_rotate[up-1][left]=1
                    tab_rotate[up][left]=1
                    tab_rotate[up+1][left]=1
                    tab_rotate[up+1][left+1]=1
                    
                    return tab_rotate,(left,left+1,up+1,up-1),1
                
            case 'j':
                if pos==1: 
                    if left+2>9:
                        return tab_moving,curr,pos
                    
                    if tab_main[up][left]==1 or tab_main[up][left+1]==1 or tab_main[up][left+2]==1 or tab_main[up+1][left+2]==1:
                        return tab_moving,curr,pos
                    
                    tab_rotate[up][left]=1
                    tab_rotate[up][left+1]=1
                    tab_rotate[up][left+2]=1
                    tab_rotate[up+1][left+2]=1
                    
                    return tab_rotate,(left,left+2,up+1,up),2
                elif pos==2:
                    if up+1>19 or up==0:
                        return tab_moving,curr,pos
                    
                    if tab_main[up-1][left]==1 or tab_main[up-1][left+1]==1 or tab_main[up][left]==1 or tab_main[up+1][left]==1:
                        return tab_moving,curr,pos
                    
                    tab_rotate[up-1][left]=1
                    tab_rotate[up-1][left+1]=1
                    tab_rotate[up][left]=1
                    tab_rotate[up+1][left]=1
                    
                    return tab_rotate,(left,left+1,up+1,up-1),3
                elif pos==3:
                    if left+2>9 or up==0:
                        return tab_moving,curr,pos
                    
                    if tab_main[up][left]==1 or tab_main[up][left+1]==1 or tab_main[up][left+2]==1 or tab_main[up-1][left]==1:
                        return tab_moving,curr,pos
                    
                    tab_rotate[up-1][left]=1
                    tab_rotate[up][left]=1
                    tab_rotate[up][left+1]=1
                    tab_rotate[up][left+2]=1
                    
                    return tab_rotate,(left,left+2,up,up-1),0
                else:
                    if up+1>19 or up==0:
                        return tab_moving,curr,pos
                    
                    if tab_main[up-1][left+1]==1 or tab_main[up][left+1]==1 or tab_main[up+1][left+1]==1 or tab_main[up+1][left]==1:
                        return tab_moving,curr,pos
                    
                    tab_rotate[up-1][left+1]=1
                    tab_rotate[up][left+1]=1
                    tab_rotate[up+1][left+1]=1
                    tab_rotate[up+1][left]=1
                    
                    return tab_rotate,(left,left+1,up+1,up-1),1

            case 't':
                if pos==1:
                    if up+2>19:
                        return tab_moving,curr,pos

                    if tab_main[up][left]==1 or tab_main[up+1][left]==1 or tab_main[up+2][left]==1 or tab_main[up+1][left+1]==1:
                        return tab_moving,curr,pos

                    tab_rotate[up][left]=1
                    tab_rotate[up+1][left]=1
                    tab_rotate[up+2][left]=1
                    tab_rotate[up+1][left+1]=1

                    return tab_rotate,(left,left+1,up+2,up),2

                elif pos==2:
                    if left+2>9 or up==0:
                        return tab_moving,curr,pos

                    if tab_main[up][left]==1 or tab_main[up][left+1]==1 or tab_main[up][left+2]==1 or tab_main[up-1][left+1]==1:
                        return tab_moving,curr,pos

                    tab_rotate[up][left]=1
                    tab_rotate[up][left+1]=1
                    tab_rotate[up][left+2]=1
                    tab_rotate[up-1][left+1]=1

                    return tab_rotate,(left,left+2,up,up-1),3
                
                elif pos==3:
                    if up+2>19:
                        return tab_moving,curr,pos

                    if tab_main[up][left+1]==1 or tab_main[up+1][left+1]==1 or tab_main[up+2][left+1]==1 or tab_main[up+1][left]==1:
                        return tab_moving,curr,pos

                    tab_rotate[up][left+1]=1
                    tab_rotate[up+1][left+1]=1
                    tab_rotate[up+2][left+1]=1
                    tab_rotate[up+1][left]=1

                    return tab_rotate,(left,left+1,up+2,up),0

                else:
                    if left+2>9:
                        return tab_moving,curr,pos

                    if tab_main[up][left]==1 or tab_main[up][left+1]==1 or tab_main[up][left+2]==1 or tab_main[up+1][left+1]==1:
                        return tab_moving,curr,pos

                    tab_rotate[up][left]=1
                    tab_rotate[up][left+1]=1
                    tab_rotate[up][left+2]=1
                    tab_rotate[up+1][left+1]=1

                    return tab_rotate,(left,left+2,up+1,up),1
            
            case other:
                return tab_moving,curr,pos