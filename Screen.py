import pygame
import random
from GameOfLife import GameOfLife

width = 600
height = 600
rowSize = 10
framerate = 10
showGrid = False

def drawGrid(frame, matrix):
    x = 0
    y = 0

    horizontalRows = width // rowSize
    verticalRows = height // rowSize

    if (showGrid):
        for e in range(horizontalRows):
            x = x + rowSize
            pygame.draw.line(frame, (255, 255, 255), (x, 0), (x, height))

        for e in range(verticalRows):
            y = y + rowSize
            pygame.draw.line(frame, (255, 255, 255), (0, y), (width, y))

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (matrix[i][j] == 1):
                drawPixel(frame, i, j)

def drawPixel(frame, x, y):
    pygame.draw.rect(frame, (200, 200, 200), ((rowSize * x), (rowSize * y), rowSize, rowSize))


def redrawWindow(frame, matrix):
    frame.fill((0, 0, 0))
    drawGrid(frame, matrix)
    pygame.display.update()


def main():
    game = GameOfLife((width // rowSize), (height // rowSize))
    window = pygame.display.set_mode((width, height))
    flow = True
    clock = pygame.time.Clock()
    frame = game.frameA
    while flow:
        clock.tick(framerate)
        redrawWindow(window, frame)
        frame = game.updateGeneration()

main()
