import pygame
import math
from subprocess import call
import random

#Constants for the window
WIDTH = 900
HEIGHT = 382
FPS = 30
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NEA project")

# Constants for colours that will be used in the game 
green = 0, 255, 0
white = 255, 255, 255
black = 0, 0, 0
floor_colour = 77,50,165

# Text
pygame.font.init()
textfont = pygame.font.SysFont('monospace', 25)

start_button_image = pygame.image.load('testing.png').convert_alpha()

class Button():
    def __init__(self, x, y, image, scale):
        image_width = image.get_width()
        image_height = image.get_height()
        self.image = pygame.transform.scale(image, (int(image_width*scale), int(image_height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        mouse_position = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                print('Clicked - true')
        if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
            self.clicked = False
            print('Clicked - false')
        WINDOW.blit(self.image, (self.rect.x, self.rect.y))
        return action

start_button = Button(340, 50, start_button_image, 0.5)

def main_menu():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

        WINDOW.fill(black)
        start_button.draw()
        pygame.display.update()

    pygame.quit()

main_menu()
