import pygame

pygame.init()
screen_width = 1500
screen_height = 1000
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.update()

background = pygame.image.load('menu/вселенная.jpg')
music_true = pygame.image.load('menu/music_true.png')
music_false = pygame.image.load('menu/music_false.png')
start = pygame.image.load('menu/start.jpg')
exit = pygame.image.load('menu/exit.jpg')
selector = pygame.image.load('menu/select level.jpg')
levels = pygame.image.load('menu/levels.jpg')

def menu():

    finished = False
    music = True
    BLACK = (0, 0, 0)

    while not finished:
        screen.blit(background, (0, 0))
        if music:
            screen.blit(music_true, (1400, 0))
        else:
            screen.blit(music_false, (1400, 0))

        screen.blit(start, (450, 250))


        screen.blit(exit, (0, 900))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                    coord = event.pos
                    if coord[0] > 1400:
                        if coord[1] < 100:
                            if music:
                                music = False
                            else:
                                music = True
                    if coord[0] > 0 and coord[0] < 400:
                        if coord[1] > 900 and coord[1] < 1000:
                            pygame.quit()
                    if coord[0] > 450 and coord[0] < 1050:
                        if coord[1] > 250 and coord[1] < 450:
                            screen.fill((0, 0, 0))
                            finished = False
                            while not finished:
                                screen.blit(background, (0, 0))
                                screen.blit(selector, (450, 250))
                                screen.blit(levels, (250, 500))

                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        finished = True
                                    elif event.type == pygame.MOUSEBUTTONDOWN:
                                        coord = event.pos
                                        if coord[1] > 500 and coord[1] < 800:
                                            if coord[0] > 250 and coord[0] < 450:
                                                pygame.quit()
                                                return 0
                                            if coord[0] > 500 and coord[0] < 700:
                                                pygame.quit()
                                                return 1
                                            if coord[0] > 750 and coord[0] < 950:
                                                pygame.quit()
                                                return 2
                                            if coord[0] > 1000 and coord[0] < 1250:
                                                pygame.quit()
                                                return 3
                                pygame.display.update()



        pygame.display.update()


    pygame.quit()