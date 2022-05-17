import pygame
import random
import time
from pygame import mixer

#__________________________________
import sqlite3 as sq
db = sq.connect("DIFFICULTY.db")
fetc = """SELECT * FROM
    Data
    """
data = db.execute(fetc)
for row in data:
    level=row[0]                    #From External source

#___________________________________________________

score=0
pygame.init()
width,height=600,500 #SNAKE SCREEN SIZE
game_screen= pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game for Pfun by Qazi & Omer") 
gray = ((127,127,127))
game_screen.fill(gray)
clock= pygame.time.Clock()
x,y =200,200
delta_x,delta_y=10,0
food_x,food_y = random.randrange(0,width)//10*10, random.randrange(0,height)//10*10
pygame.display.flip()
body_list = [(x,y)]

RED=(0,0,255)
score_font=pygame.font.SysFont('arial',30)

game_over = False
mixer.music.load("soundsnake.wav")
mixer.music.play()
def snake():
    global x,y,food_x,food_y,game_over,score
    x=(x + delta_x)%width
    y=(y + delta_y)%height
    if ((x,y) in body_list):
        game_over = True
        return
    

    body_list.append((x,y))
    if(food_x==x and food_y==y):
        while((food_x,food_y) in body_list):
            food_x,food_y = random.randrange(0,500)//10*10,random.randrange(0,500)//10*10
            score+=10
            
    else:
        del body_list[0]
    bg = pygame.image.load("backgroundpic.jpg")
    game_screen.blit(bg,(0,0))
    pygame.draw.rect(game_screen,(255,0,0),[food_x,food_y,10,10])
    for (i,j) in body_list:
        pygame.draw.rect(game_screen,(0,0,0),[i,j,10,10])
    Score_text = score_font.render("SCORE: ",1,RED)
    game_screen.blit(Score_text,(10,20))
    Score_num = score_font.render(str(score),1,RED)
    game_screen.blit(Score_num,(130,20))
       
     
    pygame.display.update()
def move(keys_pressed):
    global x,y,delta_x,delta_y
    if keys_pressed[pygame.K_UP] :
        if (delta_y!=10):
            delta_y=-10
        delta_x=0
    elif keys_pressed[pygame.K_DOWN] :
        if(delta_y!=-10):
            delta_y=10
        delta_x=0
    elif keys_pressed[pygame.K_LEFT] :
        if(delta_x!=10):
            delta_x=-10
        delta_y=0
    elif keys_pressed[pygame.K_RIGHT] :
        if(delta_x!=-10):
            delta_x=10
        delta_y=0


while True:

    if(game_over):
        pygame.quit()
        quit()
    
    if level==1:
        if body_list[0][0]==590:
            pygame.quit()
            quit()
        elif body_list[0][0]==0:
            pygame.quit()
            quit()
        elif body_list[0][1]==590:
            pygame.quit()
            quit()
        elif body_list[0][1]==0:
            pygame.quit()
            quit()
    events = pygame.event.get()
    for event in events:
        if(event.type == pygame.QUIT):
            pygame.quit()
            quit()
        if (event.type==pygame.KEYDOWN):
            snake()
    keys_pressed=pygame.key.get_pressed()

    move(keys_pressed)
    
    if(not events):
        snake()
    clock.tick(20)
