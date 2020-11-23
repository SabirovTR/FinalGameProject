# coding: utf-8
# license: GPLv3

Grav = 9.8  # Ускорение свободного падения для снаряда.

class Planet:
    """
    Тип данных, описывающий планету.
    Cодержит массу, координаты, а также визуальный радиус
    планеты в пикселах и её цвет
    """

    type = "planet"
    """Признак объекта планеты"""

    m = 0
    """Масса планеты"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус планеты"""

    color = None
    """Цвет планеты"""

    image = None
    """Изображение планеты"""
    def __init__(self, m, x, y, Fx, Fy, R, color):
        self.m = m
        self.x = x
        self.y = y
        self.Fx = Fx
        self.Fy = Fy
        self.R = R
        self.color = color

    def move(self):
        """
        This type of planet can't move at all.
        :return: None
        """
    pass

class movingPlanet(Planet):
    """
    Тип данных, описывающий двигающую планету.
    Cодержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "planet"
    """Признак объекта планеты"""

    m = 0
    """Масса планеты"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус планеты"""

    color = None
    """Цвет планеты"""

    image = None
    """Изображение планеты"""

    def __init__(self, m, x, y, Vx, Vy, Fx, Fy, R, color):
        super.__init__(m, x, y, Vx, Vy, Fx, Fy, R, color)
        self.Vx = Vx
        self.Vy = Vy

    def move(self):
        self.x += self.Vx
        self.y += self.Vy




