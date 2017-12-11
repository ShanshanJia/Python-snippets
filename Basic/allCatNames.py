#! /usr/bin/python
# allCatNames.py - Working with Lists to store the names of your cats.
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + '(or enter nothing to stop):')
    name = input()
    if name == '':
        break
    catNames.append(name)

print('The cat names are: ')
for name in catNames:
    print(name)
