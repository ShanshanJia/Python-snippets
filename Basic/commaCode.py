#! /usr/bin/python
# commaCode.py - Connect list items with ',' and 'and'


def comma(targetList):
    headStr = ', '.join(targetList[:-1])
    print(headStr + ', and ' + targetList[-1])


inputList = ['apples', 'bananas', 'oranges', 'tofu']
comma(inputList)
