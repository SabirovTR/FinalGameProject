import math
import pygame


backgrond = pygame.image.load('Space_objects_images/Space.jpg')

window_width = 1440
"""Ширина окна"""

window_height = 900
"""Высота окна"""


def create_space_object_image(obj, surface):

    if obj.dynamic:
        rotation_angle = (180 / math.pi) * math.atan2(obj.vy, obj.vx)
    else:
        rotation_angle = 0

    if (obj.type == 'Planet') or (obj.type == 'AntiPlanet'):
        planet_surface = pygame.image.load('Space_objects_images/' + str(obj.image) + '.png').convert_alpha()
        transformed_surface = pygame.transform.scale(planet_surface,
                                                     (planet_surface.get_width() // 30,
                                                      planet_surface.get_height() // 30))
        transformed_surface = pygame.transform.rotate(transformed_surface, rotation_angle)
        planet_rect = transformed_surface.get_rect(center=(obj.x, obj.y))
        surface.blit(transformed_surface, planet_rect)

    elif obj.type == 'WormHole':
        planet_surface = pygame.image.load('Space_objects_images/WormHole.png').convert_alpha()
        transformed_surface = pygame.transform.scale(planet_surface,
                                                     (planet_surface.get_width() // 10,
                                                      planet_surface.get_height() // 10))
        planet_rect = transformed_surface.get_rect(center=(obj.x, obj.y))
        surface.blit(transformed_surface, planet_rect)
        planet_rect = transformed_surface.get_rect(center=(obj.x_out, obj.y_out))
        surface.blit(transformed_surface, planet_rect)

    elif obj.type == 'Enterance':
        pygame.draw.circle(surface, (173, 255, 47), (obj.x, obj.y), 40)


def trace_image(ship, surface):

    for step in ship.trace:
        pygame.draw.circle(surface, (200, 200, 200), step, 2)


def create_space_ship_image(ship, surface):

    trace_image(ship, surface)

    space_ship_surface = pygame.image.load('Space_objects_images/SpaceShip.png').convert()
    transformed_surface = pygame.transform.scale(space_ship_surface,
                                                 (space_ship_surface.get_width() // 40,
                                                  space_ship_surface.get_height() // 40))
    transformed_surface = pygame.transform.rotate(transformed_surface, ship.angle)
    space_ship_rect = transformed_surface.get_rect(center=(ship.x, ship.y))
    transformed_surface.set_colorkey((0, 0, 0))
    surface.blit(transformed_surface, space_ship_rect)


def explosion(ship, surface):

    explosion_surface = pygame.image.load('Space_objects_images/explosion.png').convert_alpha()
    transformed_surface = pygame.transform.scale(explosion_surface,
                                                 (explosion_surface.get_width() // 2,
                                                  explosion_surface.get_height() // 2))
    explosion_rect = transformed_surface.get_rect(center=(ship.x, ship.y))
    surface.blit(transformed_surface, explosion_rect)




def update_system_position(ship, space_obj, surface):

    surface.blit(backgrond, (0, 0))

    for obj in space_obj:
        create_space_object_image(obj, surface)

    #if ship.trace:
    #    print('trace')

    create_space_ship_image(ship, surface)


if __name__ == "__main__":
    print("This module is not for direct call!")
