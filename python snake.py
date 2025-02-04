

import pygame
import time
import random

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Ekran boyutları
WIDTH, HEIGHT = 600, 400

# Yılan ve yem boyutu
BLOCK_SIZE = 20

# Pygame başlatma
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Yılan Oyunu")

clock = pygame.time.Clock()

# Başlangıç hızı
INITIAL_SPEED = 10
SNAKE_SPEED = INITIAL_SPEED

# Font ayarları
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], block_size, block_size])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def show_score(score, level):
    value = score_font.render("Skor: " + str(score) + "  Seviye: " + str(level), True, WHITE)
    screen.blit(value, [10, 10])

def gameLoop():
    global SNAKE_SPEED
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    score = 0
    level = 1

    while not game_over:

        while game_close == True:
            screen.fill(BLUE)
            message("Kaybettin! Q-Tuşu ile Çık veya C-Tuşu ile Yeniden Başla", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        SNAKE_SPEED = INITIAL_SPEED
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(BLOCK_SIZE, snake_List)
        show_score(score, level)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            Length_of_snake += 1
            score += 10

            # Her 50 puan sonrası seviye atlama
            if score // 50 >= level and level < 10:
                level += 1
                SNAKE_SPEED += 2  # Hızı artır

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

# Oyunu başlat
gameLoop()