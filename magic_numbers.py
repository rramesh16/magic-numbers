# Magic Number Game



# Import random number from python library
import random


while True:
    # generate a random number
    num = random.randint(1, 10)
    # ask for user input
    user_guess = int(input('Guess the magic number between 0-10:'))
    # evaluate input and respond accordingly
    if num == user_guess:
        print('Well done! You guessed it right.')
    elif user_guess > num:
        print('Too high!')
    elif user_guess == 0:           # Breaks if user input the number 0
        break
    elif user_guess < num:
        print('Too low!')

print('No more magic')