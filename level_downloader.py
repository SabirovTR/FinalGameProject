from space_objects import *


def strbool(str):

    if str == 'True': return True
    else: return False


def read_level_parameters(parameters_line, level):

    parameters_list = parameters_line.split()

    level.episode = int(parameters_list[1])
    level.number = int(parameters_list[2])
    level.name = parameters_list[3]
    level.dynamic = bool(parameters_list[4])
    level.reflected = bool(parameters_list[5])


def read_ship_parameters(parameters_line, ship):

    parameters_list = parameters_line.split()

    ship.m = float(parameters_list[1])
    ship.x = float(parameters_list[2])
    ship.y = float(parameters_list[3])
    ship.vx = float(parameters_list[4])
    ship.vy = float(parameters_list[5])
    ship.ax = float(parameters_list[6])
    ship.ay = float(parameters_list[7])


def read_obj_parameters(parameters_line, obj):

    parameters_list = parameters_line.split()

    obj.type = parameters_list[1]
    obj.dynamic = strbool(parameters_list[2])
    print(obj.dynamic)
    obj.interacting = strbool(parameters_list[3])
    obj.x = float(parameters_list[4])
    obj.y = float(parameters_list[5])

    if obj.type == 'Planet':
        obj.m = float(parameters_list[6])
        obj.vx = float(parameters_list[7])
        obj.vy = float(parameters_list[8])
        obj.ax = float(parameters_list[9])
        obj.ay = float(parameters_list[10])
        obj.image = int(parameters_list[11])
        print(obj.dynamic, obj.vx, obj.vy, obj.ax, obj.ay)

    elif obj.type == 'AntiPlanet':
        obj.m = -float(parameters_list[6])
        obj.vx = float(parameters_list[7])
        obj.vy = float(parameters_list[8])
        obj.ax = float(parameters_list[9])
        obj.ay = float(parameters_list[10])
        obj.image = int(parameters_list[11])
        print(obj.dynamic, obj.vx, obj.vy, obj.ax, obj.ay)

    elif obj.type == 'WormHole':
        obj.rotation = float(parameters_list[6])
        obj.x_out = float(parameters_list[7])
        obj.y_out = float(parameters_list[8])

    elif obj.type == 'Entrance':
        obj.r = float(parameters_list[6])


def download_level(level_file):

    space_obj = []

    with open(level_file) as level_description:
        for line in level_description:
            if len(line.strip()) == 0:
                continue
            line_description = line.split()[0]
            if line_description == 'Level':
                level = Level()
                read_level_parameters(line, level)

            elif line_description == 'SpaceShip':
                ship = SpaceShip()
                read_ship_parameters(line, ship)

            elif line_description == "SpaceObj":
                obj = SpaceObj()
                read_obj_parameters(line, obj)
                space_obj.append(obj)

    return(level, ship, space_obj)

#download_level('Levels/1.txt')
if __name__ == "__main__":
   print("This module is not for direct call!")
