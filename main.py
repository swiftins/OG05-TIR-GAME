import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры экрана
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ИГРА ТИР")

# Установка иконки окна
icon = pygame.image.load("target.jpg")
pygame.display.set_icon(icon)

# Загрузка изображений мишеней
target_image1 = pygame.image.load("amur.png")  # Первая мишень
target_image2 = pygame.image.load("amur.png")  # Вторая мишень

target_width = 111
target_height = 111
def get_random_target_position():
    return random.randint(0, SCREEN_WIDTH - target_width), random.randint(0, SCREEN_HEIGHT - target_height)
def targets_overlap(x1, y1, x2, y2):
    return not (x1 + target_width < x2 or x2 + target_width < x1 or y1 + target_height < y2 or y2 + target_height < y1)

# Начальные координаты для двух мишеней
target1_x, target1_y = get_random_target_position()
target2_x, target2_y = get_random_target_position()

# Случайный цвет фона
def get_random_color():
    return (random.randint(0, 200), random.randint(0, 200), random.randint(0, 200))

color = get_random_color()
running = True
while running:
    pass
pygame.quit()