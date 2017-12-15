#! /usr/bin/python
# charPictureGrid.py - Draws the picture with text characters in a list


def drawPic(grid):
    for y in range(len(grid[0])):
        for x in range(len(grid)):
            print(grid[x][y], end='')
        print()


gridList = [['a0', 'a1', 'a2','a3'], ['b0', 'b1', 'b2','b3'], ['c0', 'c1', 'c2', 'c3'], ['d0', 'd1', 'd2', 'd3']]
drawPic(gridList)
