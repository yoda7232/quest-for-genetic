import pygame
import pygame.freetype
import time
import sys
import random

pygame.init()

        ############################################################

class tile:
    def __init__(self, x, y, tileSize, color):
        self.x = x
        self.y = y
        self.tileSize = tileSize
        self.surface = pygame.Surface((tileSize, tileSize))
        pygame.draw.rect(self.surface, color, (0, 0, tileSize, tileSize))
        self.surface = self.surface.convert()

    def show(self):
        screen.blit(self.surface, (self.x, self.y))

        ############################################################

mainloop = True

screenX = 640
screenY = 480

color = (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))

tileSize = 80

paintTiles = []

font = pygame.freetype.SysFont('Comic Sans MS', 30)

screen = pygame.display.set_mode((screenX, screenY))

background = pygame.Surface(screen.get_size())
background.fill((210, 210, 255))
background = background.convert()
screen.blit(background, (0, 0))

mousePos = pygame.mouse.get_pos()

snapTile = tile(mousePos[0] - (mousePos[0] % 80), mousePos[1] - (mousePos[1] % 80), 80, color)
color = (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))

while mainloop:

    mousePos = pygame.mouse.get_pos()

    snapTile.x = mousePos[0] - (mousePos[0] % tileSize)
    snapTile.y = mousePos[1] - (mousePos[1] % tileSize)

    screen.blit(background, (0, 0))

    for block in paintTiles:
        block.show()

    snapTile.show()

    font.render_to(screen, (30, 30), str(mousePos[0]), (0, 0, 0))
    font.render_to(screen, (30, 60), str(mousePos[1]), (0, 0, 0))
    font.render_to(screen, (30, 100), "When finished, press 'r'", (0, 0, 0))


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_r:
                mainloop = False
        elif event.type == pygame.MOUSEBUTTONUP:
                paintTiles.append(tile(mousePos[0] - (mousePos[0] % tileSize), mousePos[1] - (mousePos[1] % tileSize), tileSize, color))
                color = (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))

mapString = ""
tileFound = False


for r in range(6):
    for c in range(8):
        tileFound = False
        for block in paintTiles:
            if ((block.x == c * tileSize) and (block.y == r * tileSize) and not(tileFound)):
                mapString += "w"
                tileFound == True

        if not(tileFound):
            mapString += " "


mapString += "X"
print(mapString)
print(len(mapString))

currTile = 0
screen.blit(background, (0, 0))

totalRow = 6
totalCol = 8

tiles = []

for r in range(totalRow):
    for c in range(totalCol):
        if mapString[c + (r * totalCol)] == "w":
            tiles.append(tile(c * 80, r * 80, tileSize, color))
            color = (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))
            tiles[currTile].show()

            currTile += 1

pygame.display.flip()
mainloop = True

while mainloop:
    time.sleep(5)
    mainloop = False
