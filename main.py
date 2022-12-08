import pygame
import random
import sys
from game_of_life import GameOfLife

def draw_grid(frame, matrix, width, height, cell_size, show_grid=True):
    '''
    Draws the matrix grid and calls for draw_cell for each active cell in the matrix
    
    Parameters
    ----------
    frame : pygame.Surface
        Pygame window
    matrix : array
        2D array of integers where each cell may be either 0 or 1
    width : int
        Number of pixels of the width of the window
    height : int
        Number of pixels of the height of the window
    cell_size : int
        Number of pixels of the side of each matrix cell
    show_grid : bool
        Whether or not the lines of the matrix are shown
    
    Returns
    -------
    None
    '''
    x = 0
    y = 0

    horizontal_rows = width // cell_size
    vertical_rows = height // cell_size

    if (show_grid):
        for e in range(horizontal_rows):
            x = x + cell_size
            pygame.draw.line(frame, (255, 255, 255), (x, 0), (x, height))

        for e in range(vertical_rows):
            y = y + cell_size
            pygame.draw.line(frame, (255, 255, 255), (0, y), (width, y))

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (matrix[i][j] == 1):
                draw_cell(frame, i, j, cell_size)

def draw_cell(frame, x, y, cell_size):
    '''
    Draws a given cell on the pygame window.
    
    Parameters
    ----------
    frame : pygame.Surface
        Pygame window
    x : int
        x coordinate of the cell
    y : int
        y coordinate of the cell
    cell_size : int
        Number of pixels of the side of each matrix cell
    
    Returns
    -------
    None
    '''
    pygame.draw.rect(frame, (200, 200, 200), ((cell_size * x), (cell_size * y), cell_size, cell_size))


def redraw_window(frame, matrix, width, height, cell_size, show_grid=True):
    '''
    General method for creating and drawing the current iteration on the pygame window
    
    Parameters
    ----------
    frame : pygame.Surface
        Pygame window
    matrix : array
        2D array of integers where each cell may be either 0 or 1
    width : int
        Number of pixels of the width of the window
    height : int
        Number of pixels of the height of the window
    cell_size : int
        Number of pixels of the side of each matrix cell
    show_grid : bool
        Whether or not the lines of the matrix are shown
    
    Returns
    -------
    None
    '''
    frame.fill((0, 0, 0))
    draw_grid(frame, matrix, width, height, cell_size, show_grid=show_grid)
    pygame.display.update()


def main():
    width = 600
    height = 600
    cell_size = 10
    framerate = 10
    show_grid = False

    for i in range(1, len(sys.argv)):
        curr_arg = sys.argv[i]
        height = int(sys.argv[i + 1]) if curr_arg == '-h' else height
        width = int(sys.argv[i + 1]) if curr_arg == '-w' else width
        cell_size = int(sys.argv[i + 1]) if curr_arg == '--cell-size' else cell_size
        framerate = int(sys.argv[i + 1]) if curr_arg == '--framerate' else framerate
        show_grid = True if curr_arg == '--show-grid' else show_grid


    game = GameOfLife((width // cell_size), (height // cell_size))
    window = pygame.display.set_mode((width, height))
    flow = True
    clock = pygame.time.Clock()
    matrix = game.matrix_a

    while flow:
        clock.tick(framerate)
        redraw_window(window, matrix, width, height, cell_size, show_grid=show_grid)
        matrix = game.update_generation()

        for e in pygame.event.get():
            # Pressing escape key or close button
            if e.type == pygame.QUIT or \
                (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                flow = False
    
    pygame.quit()


if __name__ == '__main__':
    main()
