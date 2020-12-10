def read_object_parameters(parameters_line, obj):

    parameters_list = parameters_line.split()

    obj.type = parameters_list[1]
    obj.static = bool(parameters_list[2])
    obj.firm = bool(parameters_list[3])
    obj.m = float(parameters_list[4])
    obj.x = float(parameters_list[5])
    obj.y = float(parameters_list[6])
    obj.vx = float(parameters_list[7])
    obj.vy = float(parameters_list[8])
    obj.ax = float(parameters_list[9])
    obj.ay = float(parameters_list[10])


def read_ship_parameters(parameters_line, ship):

    parameters_list = parameters_line.split()

    ship.m = parameters_list[1]
    ship.x = parameters_list[2]
    ship.y = parameters_list[3]
    ship.vx = parameters_list[4]
    ship.vy = parameters_list[5]
    ship.ax = parameters_list[6]
    ship.ay = parameters_list[7]


def download_level(level_file):

    space_obj = []
    with open(level_file) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue
            object_class = line.split()[0]
            if object_class == "SpaceObject":
                obj = SpaceObject()
                read_object_parameters(parameters_line, obj)
                space_obj.append(obj)
            elif object_type == "SpaceShip":
                ship = SpaceShip()
                read_ship_parameters(parameters_line, ship)

    return (space_obj, ship)


if __name__ == "__main__":
    print("This module is not for direct call!")
