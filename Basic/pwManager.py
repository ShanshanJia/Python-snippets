#! /usr/bin/python
# pwManager.py - An insecure password locker program
import sys

PASSWORDS = {'email': 'F7minwi784M', 'blog': 'VMALvQyri0o', 'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python pwManager.py [account]')
    sys.exit()

account = sys.argv[1]  # first command line argument is the account name
if account in PASSWORDS:
    print('Password for ' + account + ' is ' + PASSWORDS[account])
else:
    print('There is no account named ' + account)
