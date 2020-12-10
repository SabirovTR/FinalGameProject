G = 30
"""Игровая гравитационная постоянная Ньютона"""


def calculate_ship_acceleration(ship, space_obj):
    """Вычисляет силы, действующую на корабль

    Параметры:
    **space_obj** — список объектов, которые воздействуют корабль
    **ship** - параметры корабля
    """

    ship.ax = ship.ay = 0

    for obj in space_obj:
        if obj.type == 'Planet':
            x = obj.x - ship.x
            y = obj.y - ship.y
            r = (x ** 2 + y ** 2) ** 0.5
            ship.ax = G * obj.m / r ** 3 * x
            ship.ay = G * obj.m / r ** 3 * y


def calculate_object_acceleration(obj, space_obj):
    """Вычисляет силу, действующую на подвижные космические объекты

    Параметры:
    **obj** — тело, для которого нужно вычислить дейстующую силу.
    **space_obj** — список объектов, которые воздействуют на тело.
    """

    obj.ax = obj.ay = 0

    for other_obj in space_obj:
        if obj.static or (obj == other_obj):
            continue
        x = other_obj.x - obj.x
        y = other_obj.y - obj.y
        r = (x ** 2 + y ** 2) ** 0.5
        obj.ax += G * other_obj.m / r ** 3 * x
        obj.ay += G * other_obj.m / r ** 3 * y


def calculate_ship_movement(ship, space_obj, time_step):
    """Перемещает тело по просчитанной траектории

    Параметры:
    **ship** — перемещаемый космический корабль
    """

    calculate_ship_acceleration(ship, space_obj)

    ship.vx += ship.ax * time_step
    ship.x += ship.vx * time_step + ship.ax * time_step ** 2 / 2
    ship.vy += ship.ay * time_step
    ship.y += ship.vy * time_step + ship.ay * time_step ** 2 / 2


def calculate_object_movement(obj, time_step):
    """Перемещает тело по просчитанной траектории

    Параметры:
    **obj** — перемещаемый объект
    **space_obj** — список объектов
    """

    calculate_object_acceleration(obj, space_obj)

    obj.vx += obj.ax * time_step
    obj.x += obj.vx * time_step + ship.ax * time_step ** 2 / 2
    obj.vy += obj.ay * time_step
    obj.y += obj.vy * time_step + ship.ay * time_step ** 2 / 2


def crash_criteria(ship, space_obj):

    crushed = False

    for obj in space_obj:
        x = obj.x - ship.x
        y = obj.y - ship.y
        if (x**2 + y**2)**0.5 <= 40:
            crushed = True
            break

    return crushed


def calculate_system_movement(level, ship, space_obj, time_step):

    if not level.static:
        print('Not static')
        for obj in space_obj:
            if not obj.static:
                calculate_object_movement(obj, time_step)

    calculate_ship_movement(ship, space_obj, time_step)


if __name__ == "__main__":
    print("This module is not for direct call!")
