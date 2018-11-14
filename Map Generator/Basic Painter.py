import pygame
import pygame.freetype
import sys

        ###########################################################
class tile:
    def __init__(self, x, y, tileSize):
        print ("Tile created")
        self.x = x
        self.y = y
        self.tileSize = tileSize
        self.surface = pygame.Surface((tileSize, tileSize))
        pygame.draw.rect(self.surface, (0, 255, 0), (0, 0, tileSize, tileSize))
        self.surface = self.surface.convert()

    def show(self):
        screen.blit(self.surface, (self.x, self.y))


        ###########################################################

pygame.init()

mainloop = True

screenX = 640
screenY = 480

color = (0, 255, 0)
tileSize = 40
paintTiles = []

font = pygame.freetype.SysFont('Comic Sans MS', 30)

screen = pygame.display.set_mode((screenX, screenY))

background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
background = background.convert()
screen.blit(background, (0, 0))

while mainloop:

    mousePos = pygame.mouse.get_pos()

    screen.blit(background, (0, 0))

    for block in paintTiles:
        block.show()

    font.render_to(screen, (30, 30), str(mousePos[0]), (0, 0, 0))
    font.render_to(screen, (30, 60), str(mousePos[1]), (0, 0, 0))


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
                paintTiles.append(tile(mousePos[0] - (tileSize / 2), mousePos[1] - (tileSize / 2), tileSize))
