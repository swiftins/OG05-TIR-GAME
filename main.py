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

# Функция для генерации случайных координат мишени
def get_random_target_position():
    return random.randint(0, SCREEN_WIDTH - target_width), random.randint(0, SCREEN_HEIGHT - target_height)

# Функция для проверки пересечения мишеней
def targets_overlap(x1, y1, x2, y2):
    return not (x1 + target_width < x2 or x2 + target_width < x1 or y1 + target_height < y2 or y2 + target_height < y1)

# Начальные координаты для двух мишеней
target1_x, target1_y = get_random_target_position()
target2_x, target2_y = get_random_target_position()

# Случайный цвет фона
def get_random_color():
    return (random.randint(0, 200), random.randint(0, 200), random.randint(0, 200))

color = get_random_color()

# Основной цикл игры
running = True
while running:
    # Проверка на пересечение мишеней
    if targets_overlap(target1_x, target1_y, target2_x, target2_y):
        color = get_random_color()

    # Заливка экрана цветом
    screen.fill(color)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Проверяем попадание по первой мишени
            if target1_x < mouse_x < target1_x + target_width and target1_y < mouse_y < target1_y + target_height:
                target1_x, target1_y = get_random_target_position()

            # Проверяем попадание по второй мишени
            if target2_x < mouse_x < target2_x + target_width and target2_y < mouse_y < target2_y + target_height:
                target2_x, target2_y = get_random_target_position()

    # Отображение мишеней
    screen.blit(target_image1, (target1_x, target1_y))
    screen.blit(target_image2, (target2_x, target2_y))

    # Обновление экрана
    pygame.display.update()

# Завершение Pygame
pygame.quit()
