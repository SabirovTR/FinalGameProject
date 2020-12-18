import math

class Level():

    episode = 0
    """Номер эпизода"""

    number = 0
    """Номер уровня"""

    name = 'Level name'
    """Название уровня"""

    dynamic = False
    """Подвижность уровня"""

    reflected = False
    """Отраженность условий"""


class SpaceShip():

    m = 0
    """Масса объекта"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    vx = 0
    """Скорость по оси **x**"""

    vy = 0
    """Скорость по оси **y**"""

    ax = 0
    """Ускорение по оси **x**"""

    ay = 0
    """Ускорение по оси **y**"""

    trace = False
    """След от корабля"""

    angle = 0

    engine = 2

    trace = []




class SpaceObj():
    """Тип данных, описывающий космический объект
    Содержитб тип, массу, координаты, скорость, ускорение объекта,
    а также размер в пикселях и его изображение.
    """

    dynamic = False
    """Подвижность объекта"""

    destroying = False
    """Опасность объекта"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""


class Planet(SpaceObj):

    type = 'Planet'
    """Тип объекта"""

    m = 0
    """Масса объекта"""

    vx = 0
    """Скорость по оси **x**"""

    vy = 0
    """Скорость по оси **y**"""

    ax = 0
    """Сила по оси **x**"""

    ay = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус объекта"""

    image = 6
    """Изображение объекта"""


class AntiPlanet(SpaceObj):

    type = 'AntiPlanet'
    """Тип объекта"""

    m = 0
    """Масса объекта"""

    vx = 0
    """Скорость по оси **x**"""

    vy = 0
    """Скорость по оси **y**"""

    ax = 0
    """Сила по оси **x**"""

    ay = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус объекта"""

    image = 6
    """Изображение объекта"""


class Star(SpaceObj):

    type = 'Star'
    """Тип объекта"""

    intensity = 0

    image = 1


class BlackHole(SpaceObj):

    type = 'BlackHole'
    """Тип объекта"""

    m = 10
    """Масса объекта"""


class WormHole(SpaceObj):

    type = 'WormHole'

    rotation = 0

    x_out = 0

    y_out = 0

    image = 'WormHole'


class Enterance(SpaceObj):

    r = 0


class AsteroidBelt(SpaceObj):

    type = 'Asteroid'
    """Тип объекта"""



if __name__ == "__main__":
    print("This module is not for direct call!")
