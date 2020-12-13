import pygame
from vis import *
# from main_menu import *
# from level_downloader import *
from space_model import *
from space_objects import *


import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((600, 400))

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
    time_step = 32
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

    while not finished:
        clock.tick(time_step)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        simulation_step(level, ship, space_obj, game_surface, time_step)
        if crash_criteria(ship, space_obj):
            explosion(ship, game_surface)
            pygame.display.update()
            pygame.time.delay(2000)
            finished = True
        pygame.display.update()



def set_level():
    # Do the job here !
    pass

def set_ammunition():
    # Do the job here !
    pass

def menu():

    menu = pygame_menu.Menu(400, 500, 'HI DUDU',
                           theme=pygame_menu.themes.THEME_DARK)

    menu.add_text_input('Name :', default='aaaHHMED')
    menu.add_selector('Level :', [('1st map', 1), ('2nd map', 2), ('3rd map', 3)], onchange=set_level())
    menu.add_selector('Ammunition :', [('Engines', 1), ('Solar sail', 2)], onchange=set_ammunition())
    menu.add_button('Play', main)
    menu.add_button('Exit', pygame_menu.events.EXIT)


    menu.mainloop(surface)

menu()

if __name__ == "__main__":
    main()