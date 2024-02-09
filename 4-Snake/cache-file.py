#  -*- coding: UTF-8 -*-
# unihiker.com

import pygame 
import random 
import time   

print("Snake")
print("Start...")
time.sleep(2)

pygame.init() 
W=240 
H=320 
size=(240,320) 
window = pygame.display.set_mode(size) 
bg_color=(255,255,255)  
font = pygame.font.SysFont('Arial', 20) 

ROW=24 
COL=18 
cell_width=W/COL 
cell_height=H/ROW 

class Point:
    row=0 
    col=0 
    def __init__(self,row,col): 
        self.row=row 
        self.col=col
    def copy(self): 
        return Point(row=self.row,col=self.col)


head = Point(row=int(ROW/2),col=int(COL/2)) 
snakes=[                                
    Point(row=head.row,col=head.col+1), 
    Point(row=head.row,col=head.col+2), 
    Point(row=head.row,col=head.col+3)  
]

def gen_food():
    pos = Point(row=random.randint(0,ROW-1),col=random.randint(0,COL-1)) 
    return pos
food = gen_food() 
head_color=(65,105,225) 
snake_color=(204,204,204) 
food_color=(255,10,10) 


def rect(point,color):
    left=point.col*cell_width 
    top=point.row*cell_height 
    pygame.draw.rect(window,color,(left,top,cell_width,cell_height)) 



def detect():
    global direction
    global run
    for event in pygame.event.get(): 
        if (event.type == pygame.QUIT):    
            pygame.quit()
            run = 0
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_a): 
                if (direction == 'up'):   
                    direction = 'left'    
                elif (direction == 'left'):
                    direction = 'down'
                elif (direction == 'down'):
                    direction = 'right'
                elif (direction == 'right'):
                    direction = 'up'
                print(direction)

            elif (event.key == pygame.K_b): 
                if (direction == 'up'):     
                    direction = 'right'     
                elif (direction == 'right'):
                    direction = 'down'
                elif (direction == 'down'):
                    direction = 'left'
                elif (direction == 'left'):
                    direction = 'up'
                print(direction)


def move():
    global direction
    if direction == 'left': 
        head.col-=1         
    elif direction == 'right':
        head.col+=1
    elif direction == 'up':
        head.row-=1        
    elif direction == 'down':
        head.row+=1



def eat():
    global food
    eating = (head.row == food.row and head.col == food.col) 
    if eating :
        food = Point(row=random.randint(0,ROW-1),col=random.randint(0,COL-1)) 
    snakes.insert(0,head.copy()) 
    if not eating: 
        snakes.pop() 



def game_over():
    global run
    dead=False 
    if head.col<0 or head.row<0 or head.col>=COL or head.row>=ROW: 
        dead = True 
    for snake in snakes:
        if head.col==snake.col and head.row==snake.row: 
            dead = True
            break 
    if dead: 
        score = font.render('Your Score is ' + str(10*len(snakes)-30), False, 'pink') 
        window.blit(score, (40,250)) 
        pygame.display.flip() 
        print("GG") 
        time.sleep(5) 
        run=False 


direction = 'left'
run = True 
while run: 
    window.fill(bg_color) 
    for snake in snakes:
        rect(snake,snake_color) 
    rect(head,head_color) 
    rect(food,food_color) 

    eat()        
    detect()     
    move()       
    game_over()  

    pygame.display.flip()
    time.sleep(0.25) 