#! /usr/bin/python
# tablePrinter.py - Display a list of lists of strings in a well-organized
# table with each column right-justified.

tableData = [['apples', 'oranges', 'cherries', 'bananas'], ['Kaka', 'Datao', 'xiaotao', 'Heimiao'], ['dogs', 'cats', 'birds', 'rabbits']]


def tMatrix(matrix):
    newMatrix = []
    for y in range(len(matrix[0])):
        r = []
        for x in range(len(matrix)):
            r.append(matrix[x][y])
        newMatrix.append(r)
    return newMatrix


'''def colWidths(table):
    colWidth = []
    for x in range(len(table)):
        colWidth.append(0)
        for y in range(len(table[0])):
            if len(table[x][y]) > colWidth[x]:
                colWidth[x] = len(table[x][y])
    return colWidth'''


def colWidths(table):
    colWidth = [0] * len(table)
    for x in range(len(table)):
        colWidth[x] = len(max(table[x], key=len))
    return colWidth


def printTable(table, colWidth):
    for x in range(len(table)):
        for y in range(len(table[0])):
            print(table[x][y].rjust(colWidth[y]), end=' ')
        print()


tTable = tMatrix(tableData)
print(tTable)
width = colWidths(tableData)
print(width)
printTable(tTable, width)

# Little peach, you did great in this task and congrats that you make yourself
# finally understand how to write neseted loops! That's a big achievement !!
# Your code is well organized and clearyly and every function only has one
# responsibility.
# Here are some new things you can try:
# 1. In colWidth function, you can initialize a list with this method:
#    https://stackoverflow.com/questions/521674/initializing-a-list-to-a-known-number-of-elements-in-python
#    Even though Python hasn't provided built-in ways to do this, you
#    can always find some simple and specific ways (with Google) to do the task
#    if you find that the "normal way" is a little bit awkward.
# A: Rewritten function colWidths()
# 2. In funciton colWidth, `max` funciton is helpful when findin the longest
#    element in a list. Official document is here:
#    https://docs.python.org/3.5/library/functions.html#max. You may find the
#    `key` parameter is useful for this task.
# A: Rewritten function colWidths()
