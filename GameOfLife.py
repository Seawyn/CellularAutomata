import copy
import random

class GameOfLife:
    def __init__(self, width, height):
        frame = []
        for w in range(width):
            col = []
            for h in range(height):
                col.append(random.randint(0,1))
            frame.append(col)
        self.width = width
        self.height = height
        self.frameA = frame
        self.frameB = copy.deepcopy(frame)
    
    def checkPopulation(self, frame, x, y):
        numAdjacent = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (i == 0 and j == 0):
                    continue
                elif ((x == 0 and i == -1) or (x == (self.width - 1) and i == 1)):
                    continue
                elif ((y == 0 and j == -1) or (y == (self.height - 1) and j == 1)):
                    continue
                elif (frame[x + i][y + j] == 1):
                    numAdjacent += 1
        return (frame[x][y] == 1 and 1 < numAdjacent and numAdjacent < 4) or (frame[x][y] == 0 and numAdjacent == 3)

    def updateGeneration(self):
        for i in range(len(self.frameA)):
            for j in range(len(self.frameA[0])):
                if (self.checkPopulation(self.frameA, i, j)):
                    self.frameB[i][j] = 1
                else:
                    self.frameB[i][j] = 0
        self.frameA = copy.deepcopy(self.frameB)
        return self.frameA
