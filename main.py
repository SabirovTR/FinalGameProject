import pygame
from vis import *
# from main_menu import *
from level_downloader import *
from space_model import *
from space_objects import *


def simulation_step(level, ship, space_obj, surface, time_step):
    """ Функция симуляции полета
    Расчитывает одно действие за промежуток time_step
    """

    calculate_system_movement(level, ship, space_obj, time_step)
    update_system_position(ship, space_obj, surface)


def main():
    """Главная функция главного модуля
    1)Происходит выбор галактики и уровня
    2)Прорисовка игрового поля в pygame window
    3)Выбор снаряжения и параметров запуска
    4)Инициализация полета в реальном времени
    """

    print('Поехали!')

    game_surface = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()
    finished = False
    time_step = 100
    (level, ship, space_obj) = download_level('Levels/3.txt')
    '''
    level = Level()
    ship = SpaceShip()
    obj1 = SpaceObject()
    obj1.x = 200
    obj1.y = 400
    obj1.m = 10
    obj2 = SpaceObject()
    obj2.x = 1200
    obj2.y = 400
    obj1.m = 20
    space_obj = [obj1, obj2]
    '''

    while not finished:
        clock.tick(time_step)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        pygame.display.update()
        #game_surface.fill((0, 0, 0))
        simulation_step(level, ship, space_obj, game_surface, time_step/200)
        if crash_criteria(ship, space_obj):
            explosion(ship, game_surface)
            pygame.display.update()
            pygame.time.delay(2000)
            finished = True
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
