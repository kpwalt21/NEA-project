import pygame
import math
import random

floor_colour = 77,50,165
WIDTH = 900
HEIGHT = 382
FPS = 30
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Name to be decided")

green = 0, 255, 0
white = 255, 255, 255
black = 0, 0, 0
pygame.font.init()
textfont = pygame.font.SysFont('monospace', 25)

background = pygame.image.load('background scroll.jpg').convert()
background_width = background.get_width()

def game():
    scroll = 0
    tiles = math.ceil(WIDTH / background_width) + 1


    enemy_speed = 10  
    player_x = 50
    player_y = 260
    y_change = 0
    gravity = 2
    active = False
    restart = False
    score = 0
    enemy = [900]

    scroll = 0
    clock = pygame.time.Clock()
    run = True
    while run:
        for i in range(0, tiles):
            WINDOW.blit(background, (i * background_width + scroll, 0))
        

        if abs(scroll) > background_width:
            scroll = 0

        score_text = textfont.render(f'Score: {score}', True, white)
        WINDOW.blit(score_text, (700, 50))
        
        floor = pygame.draw.rect(WINDOW, floor_colour, [0, 277, WIDTH, 1])

        player = pygame.draw.rect(WINDOW, green, [player_x, player_y, 20, 20])

        enemy0 = pygame.draw.rect(WINDOW, green, [enemy[0], 260, 20, 20])


        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN and restart == True:
                if event.key == pygame.K_r:
                    restart = False
                    player_x = 50
                    player_y = 260
                    score = 0
                    enemy = [900]

            if event.type == pygame.KEYDOWN and active == False and restart == False:
                if event.key == pygame.K_p:
                    active = True
                    
            if event.type == pygame.KEYDOWN and active == True:
                if event.key == pygame.K_SPACE and y_change == 0:
                    y_change = 20

        for i in range(len(enemy)):
            if active:
                scroll -= 5
                enemy[i] -= enemy_speed
                if enemy[i] < -10:
                    enemy[i] = random.randint(950, 1200)
                    score += 1
                if player.colliderect(enemy0):
                    active = False
                    restart = True
                    

        if y_change > 0 or player_y < 260:
            player_y -= y_change
            y_change -= gravity
        
        if player_y > 260:
            player_y = 260
        if player_y < 140:
            player_y = 140

        if player_y == 260 and y_change < 0:
            y_change = 0
        
        pygame.display.update()
        
    pygame.quit()
game()