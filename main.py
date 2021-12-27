# Import random number generator
import random

if __name__ == '__main__':
    # Create a list with all the numbers on a roll of dice
    diceRollList = [1,2,3,4,5,6]
    # Randomly pick a number from the list and print it out:
    print(random.choice(diceRollList))
