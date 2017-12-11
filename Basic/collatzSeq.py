#! /usr/bin/python
# collatzSeq.py - Generates Collatz Sequences starting with any number entered


def collatz(num):
    while num != 1:
        num = num // 2 if num % 2 == 0 else num * 3 + 1
        print(num)


def main():
    print('Enter an integer please:')
    try:
        number = int(input())
    except ValueError:
        print('You have to enter a number.')
    else:
        collatz(number)


main()
