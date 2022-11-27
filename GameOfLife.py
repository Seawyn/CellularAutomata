import copy
import random

class GameOfLife:
    def __init__(self, width, height):
        matrix = []
        for w in range(width):
            col = []
            for h in range(height):
                col.append(random.randint(0,1))
            matrix.append(col)
        self.width = width
        self.height = height
        self.matrix_a = matrix
        self.matrix_b = copy.deepcopy(matrix)
    
    def check_population(self, matrix, x, y):
        '''
        Checks whether or not a cell in a given coordinate will be active the next iteration.
        
        Parameters
        ----------
        matrix : array
            2D array of integers where each cell may be either 0 or 1
        x : int
            x coordinate of the cell
        y : int
            y coordinate of the cell
        
        Returns
        -------
        int : status of the selected cell in the next iteration
        '''
        num_adjacent = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (i == 0 and j == 0):
                    continue
                elif ((x == 0 and i == -1) or (x == (self.width - 1) and i == 1)):
                    continue
                elif ((y == 0 and j == -1) or (y == (self.height - 1) and j == 1)):
                    continue
                elif (matrix[x + i][y + j] == 1):
                    num_adjacent += 1
        return (matrix[x][y] == 1 and 1 < num_adjacent and num_adjacent < 4) or (matrix[x][y] == 0 and num_adjacent == 3)

    def update_generation(self):
        '''
        Updates the matrix of matrix_b based on the status of matrix_a.
        
        Returns
        -------
        array : the next iteration's matrix
        '''
        for i in range(len(self.matrix_a)):
            for j in range(len(self.matrix_a[0])):
                if (self.check_population(self.matrix_a, i, j)):
                    self.matrix_b[i][j] = 1
                else:
                    self.matrix_b[i][j] = 0
        self.matrix_a = copy.deepcopy(self.matrix_b)
        return self.matrix_a
