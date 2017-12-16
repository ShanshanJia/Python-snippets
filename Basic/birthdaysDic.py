#! /usr/bin/python
# birthdaysDic.py - Stores data of your friends' birthdays

birthdays = {'kaka': 'Apr 1', 'datao': 'Dec 23', 'xiaotao': 'Jul 27'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday datdabase updated.')
