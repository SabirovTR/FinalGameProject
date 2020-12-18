import math

G = 2
"""Игровая гравитационная постоянная Ньютона"""


def manual_control(ship, speed_vector):
    efficiency = 0.1
    dv = efficiency * ship.engine

    if ship.engine > 0:
        if speed_vector == 'w': ship.ay -= dv
        if speed_vector == 'a': ship.ax -= dv
        if speed_vector == 's': ship.ay += dv
        if speed_vector == 'd': ship.ax += dv


def calculate_ship_acceleration(ship, space_obj):
    """Вычисляет силы, действующую на корабль

    Параметры:
    **space_obj** — список объектов, которые воздействуют корабль
    **ship** - параметры корабля
    """

    for obj in space_obj:
        if (obj.type == 'Planet') or (obj.type == 'AntiPlanet'):
            x = obj.x - ship.x
            y = obj.y - ship.y
            r = (x ** 2 + y ** 2) ** 0.5
            ship.ax += G * obj.m / r ** 3 * x
            ship.ay += G * obj.m / r ** 3 * y


def calculate_object_acceleration(obj, space_obj):
    """Вычисляет силу, действующую на подвижные космические объекты

    Параметры:
    **obj** — тело, для которого нужно вычислить дейстующую силу.
    **space_obj** — список объектов, которые воздействуют на тело.
    """

    for other_obj in space_obj:

        if (obj.dynamic == False) or (obj == other_obj):
            continue
        else:
            x = other_obj.x - obj.x
            y = other_obj.y - obj.y
            r = (x ** 2 + y ** 2) ** 0.5
            obj.ax += G * other_obj.m * (abs(obj.m) / obj.m) / r ** 3 * x
            obj.ay += G * other_obj.m * (abs(obj.m) / obj.m) / r ** 3 * y


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
    ship.angle = 180 + (180 / math.pi) * math.atan2(ship.vx, ship.vy)

    ship.ax = ship.ay = 0


def calculate_object_movement(obj, space_obj, time_step):
    """Перемещает тело по просчитанной траектории

    Параметры:
    **obj** — перемещаемый объект
    **space_obj** — список объектов
    """

    calculate_object_acceleration(obj, space_obj)

    obj.vx += obj.ax * time_step
    obj.x += obj.vx * time_step + obj.ax * time_step ** 2 / 2
    obj.vy += obj.ay * time_step
    obj.y += obj.vy * time_step + obj.ay * time_step ** 2 / 2

    obj.ax = obj.ay = 0


def obj_interaction(ship, space_obj):

    interaction_distance = 40

    explode = False

    for obj in space_obj:

        if obj.interacting:
            if obj.type == 'WormHole':
                x = obj.x - ship.x
                y = obj.y - ship.y
                x_out = obj.x_out - ship.x
                y_out = obj.y_out - ship.y
                distance = (x ** 2 + y ** 2) ** 0.5
                distance_out = (x_out ** 2 + y_out ** 2) ** 0.5

                if distance < interaction_distance:
                    ship.x = obj.x_out
                    ship.y = obj.y_out
                    angle = ship.angle + obj.rotation
                    v = (ship.vx ** 2 + ship.vy ** 2) ** 0.5
                    ship.x += - 1.1 * interaction_distance * math.sin((math.pi / 180) * angle)
                    ship.y += 1.1 * interaction_distance * math.cos((math.pi / 180) * angle)
                    ship.vx = - v * math.sin((math.pi / 180) * angle)
                    ship.vy = v * math.cos((math.pi / 180) * angle)

                elif distance_out < interaction_distance:
                    ship.x = obj.x
                    ship.y = obj.y
                    angle = ship.angle - obj.rotation
                    v = (ship.vx ** 2 + ship.vy ** 2) ** 0.5
                    ship.vx = - v * math.sin((math.pi / 180) * angle)
                    ship.vy = v * math.cos((math.pi / 180) * angle)

            else:
                x = obj.x - ship.x
                y = obj.y - ship.y
                distance = (x ** 2 + y ** 2) ** 0.5
                if distance <= interaction_distance:
                    explode = True

    return explode


def calculate_system_movement(level, ship, space_obj, time_step):
    if not not level.dynamic:
        for obj in space_obj:
            if obj.dynamic:
                calculate_object_movement(obj, space_obj, time_step)

    calculate_ship_movement(ship, space_obj, time_step)


if __name__ == "__main__":
    print("This module is not for direct call!")
