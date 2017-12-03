# This is to show input validation.
print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 3:
        print('That is a lot of cats!')
    elif int(numCats) >= 0:
        print('That is not that many cats.')
    else:
        print('Miaow, I cannot understand you.')
except ValueError:
    print('You did not enter a number.')
