"""Модуль визуализации.
Нигде, кроме этого модуля, не используются экранные координаты объектов.
Функции, создающие гaрафические объекты и перемещающие их на экране, принимают физические координаты
"""


window_width = 800
'''
Ширина окна
'''

window_height = 800
'''
Высота окна
'''

scale_factor = None
'''
Масштабирование экранных координат по отношению к физическим.
Тип: float
Мера: количество пикселей на один метр.
'''


def calculate_scale_factor(max_distance):
    """Вычисляет значение глобальной переменной **scale_factor** по данной характерной длине"""
    global scale_factor
    scale_factor = 0.4*min(window_height, window_width)/max_distance
    print('Scale factor:', scale_factor)


def scale_x(x):
    """Возвращает экранную **x** координату по **x** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **x** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.

    Параметры:

    **x** — x-координата модели.
    """

    return int(x*scale_factor) + window_width//2


def create_space_obj_image(space, space_obj):
    '''
    Создаёт отображаемый космический объект.

    Параметры:

    **space** — холст для рисования.
    **space_obj** — объект планеты.
    '''
    x = scale_x(space_obj.x)
    y = scale_y(space_obj.y)
    r = scale(space_obj.R)
    #Будет обновлено после добавления новых космических объектов
    space_obj.image = pygame.draw.circle(screen, (100, 100, 100), x, y, r)


def pause_menu(space, level_number):
    '''
    Вызов меню паузы.

    Параметры:
    **space** - холст для рисования
    **level_number** - номер уровня, для подбора цвета
    '''


if __name__ == "__main__":
    print("This module is not for direct call!")
