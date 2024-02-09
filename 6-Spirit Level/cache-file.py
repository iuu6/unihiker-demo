#  -*- coding: UTF-8 -*-
# unihiker.com

import sys
import pygame
from pygame.locals import QUIT
import math
from pinpong.board import Board
from pinpong.extension.unihiker import *
import time

print("Spirit Level")
print("Start...")
time.sleep(2)

Board("unihiker").begin()  

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((240, 320))
pygame.display.set_caption('Level App')

# Dimensions
outer_circle_radius = 100
inner_circle_radius = 10


def get_inner_circle_position(x_accel, y_accel, outer_circle_center):
    angle = math.atan2(y_accel, x_accel)
    distance = min(outer_circle_radius - inner_circle_radius,
                   math.sqrt(x_accel**2 + y_accel**2))
    x = outer_circle_center[0] + distance * math.cos(angle)
    y = outer_circle_center[1] + distance * math.sin(angle)
    return x, y


def draw_crosshairs(surface, center, radius, color):
    pygame.draw.line(
        surface, color, (center[0] - radius, center[1]), (center[0] + radius, center[1]), 2)
    pygame.draw.line(
        surface, color, (center[0], center[1] - radius), (center[0], center[1] + radius), 2)


def draw_inner_circles(surface, center, radius, count, color):
    for i in range(1, count + 1):
        pygame.draw.circle(surface, color, center, radius * i, 1)


def convert_accel_to_pixels(accel, scale_factor):
    return accel * scale_factor


def main():
    clock = pygame.time.Clock()
    scale_factor = 100  # Adjust this value to change the sensitivity of the movement
    inner_circle_count = 4

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    sys.exit()

        # Get accelerometer data 
        x_accel_raw = -accelerometer.get_y()
        y_accel_raw = accelerometer.get_x()
        #Perform anti-shake processing on the original acceleration value
        x_accel_raw = x_accel_raw if abs(x_accel_raw) > 0.1 else 0
        y_accel_raw = y_accel_raw if abs(y_accel_raw) > 0.1 else 0
        #convert to pixels
        x_accel = convert_accel_to_pixels(x_accel_raw, scale_factor)
        y_accel = convert_accel_to_pixels(y_accel_raw, scale_factor)

        # Clear the screen
        screen.fill('#FFFFFF')

        outer_circle_center = (120, 160)
        inner_circle_position = get_inner_circle_position(
            x_accel, y_accel, outer_circle_center)
        # Draw the outer circle    
        pygame.draw.circle(screen, '#000000', outer_circle_center,
                           outer_circle_radius, 2)

        draw_crosshairs(screen, outer_circle_center,
                        outer_circle_radius, '#3333FF')

        draw_inner_circles(screen, outer_circle_center, outer_circle_radius //
                           (inner_circle_count + 1), inner_circle_count, '#3333FF')
        # Draw the center circle
        pygame.draw.circle(screen, '#ecf0f1', outer_circle_center, inner_circle_radius)
        
        # Draw the ball 
        pygame.draw.circle(screen, '#ff6b81', (int(inner_circle_position[0]), int(
            inner_circle_position[1])), inner_circle_radius)
        # Update the display
        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    main()
