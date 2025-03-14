import pygame
import random
pygame.init()
win_door=random.randint(1, 3)
print(win_door)
door_removed=0
#win_door=1
SW, SH = 1000,1000
screen = pygame.display.set_mode((SW, SH), pygame.RESIZABLE)
pygame.display.set_caption(" pygame mounte hall problem")
BLUE=(0,0,255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
picked_door=0

def draw_rect(x, y, width, height):
  hitbox =  pygame.Rect(x,y,width,height)
  return hitbox
running = True
print("choose one door")
first_door_choosen=False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            SW, SH = event.w, event.h
            screen = pygame.display.set_mode((SW, SH), pygame.RESIZABLE)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and quit_button.collidepoint(event.pos):
                print("quiting")
                running=False     
            elif first_door_choosen == False:
                #print(first_door_choosen)
                if event.button == 1 and door1.collidepoint(event.pos):  
                        print("you picked door1")
                        picked_door=1
                elif event.button == 1 and door2.collidepoint(event.pos):
                        print("you picked door2")
                        picked_door=2 
                elif  event.button == 1 and door3.collidepoint(event.pos):
                        print("you picked door3")
                        picked_door=3
                if picked_door!=0:        
                    first_door_choosen=True        
            else:
                if event.button == 1 and door_removed!=1 and door1.collidepoint(event.pos):  
                    if 1==win_door:
                         print("YOU WIN")
                    else:
                         print("YOU LOST LMAO 1")
                    running=False      
                elif event.button == 1 and door_removed!=2 and door2.collidepoint(event.pos):
                    if 2==win_door:
                        print("YOU WIN")
                    else:
                         print("YOU LOST LMAO 2") 
                    running=False     
                elif  event.button == 1 and door_removed!=3 and door3.collidepoint(event.pos):
                    if 3==win_door:
                         print("YOU WIN")
                    else:
                         print("YOU LOST LMAO 3")
                    running=False
    vg=100
    g=50
    dh=500
    dw=( SW-4*g)/3
    p1=[g,vg]
    p2=[p1[0]+dw+g,vg]
    p3=[p2[0]+dw+g,vg]
    door1 = draw_rect(p1[0],p1[1],dw,dh)
    door2 = draw_rect(p2[0],p2[1],dw,dh)
    door3=draw_rect(p3[0],p3[1],dw,dh)
    quit_button=draw_rect(SW//2,vg//4,50,50)
   # print("door removed:" +str(door_removed))
    if door_removed==1:
        pygame.draw.rect(screen, BLACK, door1)
    else:
        pygame.draw.rect(screen, RED, door1)
    if door_removed==2:
       pygame.draw.rect(screen, BLACK, door2)      
    else:
        pygame.draw.rect(screen, RED, door2)
    if door_removed==3:
        pygame.draw.rect(screen, BLACK, door3)
    else:
        pygame.draw.rect(screen, RED, door3)
    pygame.draw.rect(screen,BLUE,quit_button)                
    if door_removed==0:                                         
        if picked_door==1 and picked_door!=win_door:
            if win_door==2:
                print("door 3 is empty 1")
                door_removed=3
            else:
                print("door 2 is empty 2")
                door_removed=2             
        elif picked_door==1 and picked_door==win_door:
            print("door 2 is empty 3")
            door_removed=2
        elif picked_door==2 and picked_door!=win_door:
            if win_door==1:
                print("door 3 is empty")
                door_removed=3
            else:
                print("door 1 is empty")
                door_removed=1
        elif picked_door==2 and picked_door==win_door:
            print("door 1 is empty")
            door_removed=1
        elif picked_door==3 and picked_door!=win_door:
            if win_door==1:
                print("door 2 is empty")
                door_removed=2
            else:
                print("door 1 is empty")
                door_removed=1
        elif picked_door==3 and picked_door==win_door:
            print("door 2 is empty")
            door_removed=2
    pygame.display.flip()