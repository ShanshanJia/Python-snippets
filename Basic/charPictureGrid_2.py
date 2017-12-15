#! /usr/bin/python
# charPictureGrid.py - Draws the picture with text characters in a list


def tMatrix(matrix):
    newMatrix = []
    for y in range(len(matrix[0])):
        r = []
        for x in range(len(matrix)):
            r.append(matrix[x][y])
        newMatrix.append(r)
    return newMatrix


def printMatrix(matrix):
    r = []
    for i in range(len(matrix)):
        r.append(''.join(matrix[i]))
    newMatrix = '\n'.join(r)
    print(newMatrix)


gridList = [['a0', 'a1', 'a2', 'a3'], ['b0', 'b1', 'b2', 'b3'], ['c0', 'c1', 'c2', 'c3'], ['d0', 'd1', 'd2', 'd3']]
grid = tMatrix(gridList)
printMatrix(grid)
