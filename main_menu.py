import pygame

pygame.init()
screen_width = 1440
screen_height = 800
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.update()
from pygame.draw import *
from math import pi

background = pygame.image.load('menu/вселенная.jpg')
music_true = pygame.image.load('menu/music_true.png')
music_false = pygame.image.load('menu/music_false.png')
start = pygame.image.load('menu/start.png')
exit = pygame.image.load('menu/exit.png')
zagol = pygame.image.load('menu/zagol.png')


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


def menu():

    finished = False
    music = True
    BLACK = (0, 0, 0)

    while not finished:
        screen.blit(background, (0, 0))
        if music:
            screen.blit(music_true, (1340, 0))
        else:
            screen.blit(music_false, (1340, 0))

        pygame.font.init()

        f1 = pygame.font.SysFont('purisa', 150)
        text1 = f1.render('Space', True,
                          (255, 255, 255))

        f2 = pygame.font.SysFont('purisa', 150)
        text2 = f2.render("Odisey", False,
                          (255, 255, 255))

        f3 = pygame.font.SysFont('purisa', 100)
        text3 = f3.render("Exit", False,
                          (255, 0, 0))

        f4 = pygame.font.SysFont('purisa', 130)
        text4 = f4.render("Start", False,
                          (0, 255, 0))

        """
        Button start
        """
        line(screen, (0, 255, 0), (90, 375), (480, 375), width=4)
        line(screen, (0, 255, 0), (480, 375), (480, 510), width=4)
        line(screen, (0, 255, 0), (480, 510), (90, 510), width=4)
        line(screen, (0, 255, 0), (90, 510), (90, 375), width=4)

        """
        Button exit
        """
        line(screen, (255, 0, 0), (90, 550), (480, 550), width=4)
        line(screen, (255, 0, 0), (480, 550), (480, 685), width=4)
        line(screen, (255, 0, 0), (480, 685), (90, 685), width=4)
        line(screen, (255, 0, 0), (90, 685), (90, 550), width=4)

        screen.blit(text1, (10, 0))
        screen.blit(text2, (10, 150))
        screen.blit(text3, (175, 550))
        screen.blit(text4, (100, 350))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                    coord = event.pos
                    if coord[0] > 1340:
                        if coord[1] < 100:
                            if music:
                                music = False
                            else:
                                music = True
                    if coord[0] > 90 and coord[0] < 480:
                        if coord[1] > 550 and coord[1] < 685:
                            pygame.quit()
                    if coord[0] > 90 and coord[0] < 480:
                        if coord[1] > 375 and coord[1] < 510:
                            screen.fill((0, 0, 0))
                            finished = False
                            while not finished:
                                screen.blit(background, (0, 0))
                                f1 = pygame.font.SysFont('purisa', 120)
                                text1 = f1.render('Select level', True,
                                                  (255, 255, 255))
                                screen.blit(text1, (300, 0))


                                arc(screen, GREEN, [50, 150, 150, 150], 0, 2*pi, 4)
                                arc(screen, GREEN, [220, 150, 150, 150], 0, 2*pi, 4)
                                arc(screen, GREEN, [390, 150, 150, 150], 0, 2*pi, 4)
                                arc(screen, GREEN, [560, 150, 150, 150], 0, 2*pi, 4)
                                arc(screen, GREEN, [730, 150, 150, 150], 0, 2*pi, 4)
                                arc(screen, GREEN, [900, 150, 150, 150], 0, 2*pi, 4)
                                arc(screen, GREEN, [1070, 150, 150, 150], 0, 2*pi, 4)
                                arc(screen, GREEN, [1240, 150, 150, 150], 0, 2*pi, 4)

                                arc(screen, GREEN, [50, 340, 150, 150], 0, 2 * pi, 4)
                                arc(screen, GREEN, [220, 340, 150, 150], 0, 2 * pi, 4)
                                arc(screen, GREEN, [390, 340, 150, 150], 0, 2 * pi, 4)
                                arc(screen, GREEN, [560, 340, 150, 150], 0, 2 * pi, 4)
                                arc(screen, GREEN, [730, 340, 150, 150], 0, 2 * pi, 4)
                                arc(screen, GREEN, [900, 340, 150, 150], 0, 2 * pi, 4)
                                arc(screen, GREEN, [1070, 340, 150, 150], 0, 2 * pi, 4)
                                arc(screen, GREEN, [1240, 340, 150, 150], 0, 2 * pi, 4)

                                arc(screen, GREEN, [50, 530, 150, 150], 0, 2 * pi, 4)
                                arc(screen, GREEN, [220, 530, 150, 150], 0, 2 * pi, 4)
                                arc(screen, GREEN, [390, 530, 150, 150], 0, 2 * pi, 4)
                                arc(screen, GREEN, [560, 530, 150, 150], 0, 2 * pi, 4)

                                def draw_1(n):
                                    f2 = pygame.font.SysFont('purisa', 100)
                                    text2 = f2.render(str(n), True,
                                                      (255, 255, 255))
                                    screen.blit(text2, (100 + 170 * (n - 1), 150))

                                def draw_2(n):
                                    f2 = pygame.font.SysFont('purisa', 100)
                                    text2 = f2.render(str(n+8), True,
                                                      (255, 255, 255))
                                    screen.blit(text2, (100 + 165 * (n - 1), 340))

                                def draw_3(n):
                                    f2 = pygame.font.SysFont('purisa', 100)
                                    text2 = f2.render(str(n+16), True,
                                                      (255, 255, 255))
                                    screen.blit(text2, (100 + 160 * (n - 1), 530))

                                for i in range(9):
                                    draw_1(i)

                                for i in range(9):
                                    draw_2(i)

                                for i in range(5):
                                    draw_3(i)


                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        finished = True
                                    elif event.type == pygame.MOUSEBUTTONDOWN:
                                        coord = event.pos
                                        for i in range(8):
                                            if (coord[0]-(125+170*(i)))**2 + (coord[1]-225)**2 < 75**2:
                                                pygame.quit()
                                                return i
                                        for i in range(8):
                                            if (coord[0]-(125+165*(i)))**2 + (coord[1]-415)**2 < 75**2:
                                                pygame.quit()
                                                return i + 8
                                        for i in range(4):
                                            if (coord[0]-(125+160*(i)))**2 + (coord[1]-605)**2 < 75**2:
                                                pygame.quit()
                                                return i + 16


                                pygame.display.update()



        pygame.display.update()


    pygame.quit()

menu()
