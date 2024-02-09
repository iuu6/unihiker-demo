import random 
import pygame 
from pygame.locals import * 
from sys import exit  
import time

print("Code Rain")
print("Start...")
time.sleep(2)

# set screen resolution
screen_width=240 
screen_height=320 

# set the number of rain columns and font size
rain_num = 30  
font_num = 16  

pygame.init()  # initialize pygame

# create a new window
screen=pygame.display.set_mode([screen_width, screen_height], RESIZABLE)

pygame.display.set_caption("Code Rain")  

# set the font
font = pygame.font.SysFont("Consolas", font_num)

# create a surface object with an alpha channel
bg_surface = pygame.Surface((screen_width, screen_height), flags=pygame.SRCALPHA)

# fill the surface with a semi-transparent color
bg_surface.fill(pygame.Color(0, 0, 0, 16))

# fill the window with black color
screen.fill((0, 0, 0))

# calculate the coordinates of the columns based on screen width and generate a list
drops = [0 for i in range(rain_num)]

while True:
    # get events from the event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:    # press A key to stop
                 exit()

    pygame.time.delay(30)  # pause for 30ms

    # draw the background surface onto the screen
    screen.blit(bg_surface, (0, 0))

    # draw the text onto the screen
    for i in range(rain_num):
        text = font.render(str(random.choice('0123456789abcdefghijklmnopqrstuvwxyz')), True, (0, 255, 0))  # choose a random character from 0-9 and a-z
        screen.blit(text, (i * screen_width // rain_num, drops[i] * (font_num - 10)))  # draw the text onto the screen based on the current position of the column

        # update the position of the column, if it exceeds the screen height or based on a random value, reset the position to 0
        drops[i] += 1
        if drops[i] * (font_num - 10) > screen_height or random.random() > 0.95:
            drops[i] = 0

    # update the screen
    pygame.display.flip()
