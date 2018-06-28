# The program generates a random number from a range we specify and we have to guess the number

import random

highest = int(input('Enter the highest number '
                    'you\'d like me to randomly choose from: \n'))
number = random.randint(1, highest)
print('Guess a number between 1 and {}'.format(highest))
guessed_number = 0
while guessed_number != number:
    guessed_number = int(input())
    if guessed_number < number:
        print('Guess a higher number')
    elif guessed_number > number:
        print('Guess a lower number')
    else:
        print('Congrats! You guessed it!')
