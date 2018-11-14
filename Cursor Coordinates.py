import pygame
import pygame.freetype
import sys

pygame.init()

mainloop = True

screenX = 640
screenY = 480

font = pygame.freetype.SysFont('Comic Sans MS', 30)

screen = pygame.display.set_mode((screenX, screenY))

background = pygame.Surface(screen.get_size())
background.fill((210, 210, 255))
background = background.convert()
screen.blit(background, (0, 0))







while mainloop:

    mousePos = pygame.mouse.get_pos()

    screen.blit(background, (0, 0))

    font.render_to(screen, (30, 30), str(mousePos[0]), (0, 0, 0))
    font.render_to(screen, (30, 60), str(mousePos[1]), (0, 0, 0))


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
