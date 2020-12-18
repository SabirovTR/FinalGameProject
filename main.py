import pygame
import math
from vis import *
from main_menu import *
from level_downloader import *
from space_model import *
from space_objects import *

def simulation_step(level, ship, space_obj, surface, time_step):
    """ Функция симуляции полета
    Расчитывает одно действие за промежуток time_step
    """

    calculate_system_movement(level, ship, space_obj, time_step)
    update_system_position(ship, space_obj, surface)


def keydown_control(event):

    if (event.key == pygame.K_w) or (event.key == pygame.K_w): return 'w'
    if (event.key == pygame.K_a) or (event.key == pygame.K_a): return 'a'
    if (event.key == pygame.K_s) or (event.key == pygame.K_s): return 's'
    if (event.key == pygame.K_d) or (event.key == pygame.K_d): return 'd'


def ship_launcher(ship, event):

    flag = False

    if (event.type == pygame.MOUSEBUTTONUP) and (event.button == 1):
        v = ship.engine * (ship.vx**2 + ship.vy**2)**0.5
        (mouse_x, mouse_y) = pygame.mouse.get_pos()
        ship.angle = 90 + (180 / math.pi) * math.atan2(ship.y - mouse_y, ship.x - mouse_x)
        ship.vx = - v * math.sin((math.pi / 180) * ship.angle)
        ship.vy = v * math.cos((math.pi / 180) * ship.angle)
        flag = True

    return flag



def main():
    """Главная функция главного модуля
    1)Происходит выбор галактики и уровня
    2)Прорисовка игрового поля в pygame window
    3)Выбор снаряжения и параметров запуска
    4)Инициализация полета в реальном времени
    """

    print('Поехали!')

    level = menu()
    if level == 0:
        (level, ship, space_obj) = download_level('Levels/1.txt')
    if level == 1:
        (level, ship, space_obj) = download_level('Levels/2.txt')
    if level == 2:
        (level, ship, space_obj) = download_level('Levels/3.txt')
    if level == 3:
        (level, ship, space_obj) = download_level('Levels/4.txt')
    if level == 4:
        (level, ship, space_obj) = download_level('Levels/5.txt')
    if level == 5:
        (level, ship, space_obj) = download_level('Levels/6.txt')
    if level == 6:
        (level, ship, space_obj) = download_level('Levels/7.txt')
    if level == 7:
        (level, ship, space_obj) = download_level('Levels/8.txt')
    if level == 8:
        (level, ship, space_obj) = download_level('Levels/9.txt')
    """"
    if level == 9:
        (level, ship, space_obj) = download_level('Levels/10.txt')
    if level == 10:
        (level, ship, space_obj) = download_level('Levels/11.txt')
    if level == 11:
        (level, ship, space_obj) = download_level('Levels/12.txt')
    if level == 12:
        (level, ship, space_obj) = download_level('Levels/13.txt')
    if level == 13:
        (level, ship, space_obj) = download_level('Levels/14.txt')
    if level == 14:
        (level, ship, space_obj) = download_level('Levels/15.txt')
    if level == 15:
        (level, ship, space_obj) = download_level('Levels/16.txt')
    if level == 16:
        (level, ship, space_obj) = download_level('Levels/17.txt')
    if level == 17:
        (level, ship, space_obj) = download_level('Levels/18.txt')
    if level == 18:
        (level, ship, space_obj) = download_level('Levels/19.txt')
    if level == 19:
        (level, ship, space_obj) = download_level('Levels/20.txt')
    """

    pygame.init()
    game_surface = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()
    finished = False
    started = False
    global timer
    timer = 0
    time_step = 100

    simulation_step(level, ship, space_obj, game_surface, time_step / 100)
    pygame.display.update()

    while not finished:
        clock.tick(time_step)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif (started) or (ship_launcher(ship, event)):
                started = True
            if event.type == pygame.KEYDOWN:
                manual_control(ship, keydown_control(event))

        if started:
            pygame.display.update()
            simulation_step(level, ship, space_obj, game_surface, time_step / 100)

            if obj_interaction(ship, space_obj):
                explosion(ship, game_surface)
                pygame.display.update()
                pygame.time.delay(2000)
                finished = True
                pygame.display.update()

        else:
            (mouse_x, mouse_y) = pygame.mouse.get_pos()
            ship.angle = (180 / math.pi) * math.atan2(ship.x - mouse_x, ship.y - mouse_y)
            create_space_ship_image(ship, game_surface)
            pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
