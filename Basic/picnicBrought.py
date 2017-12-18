#! /usr/bin/python
# picnicbrought.py - Sees who is bringing what to a picnic
allGuests = {'kaka': {'apples': 5, 'bananas': 12}, 'datao': {'sandwiches': 3, 'apples': 2}, 'xiaotao': {'cups': 3, 'apple pies': 1}}


def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought


print('Number of things being brought:')
print('- Apples  ' + str(totalBrought(allGuests, 'apples')))
print('- Cups  ' + str(totalBrought(allGuests, 'cups')))
print('- Cakes  ' + str(totalBrought(allGuests, 'cakes')))
print('- Bananas  ' + str(totalBrought(allGuests, 'bananas')))
print('- Sandwiches  ' + str(totalBrought(allGuests, 'sandwiches')))
