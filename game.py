#!/usr/bin/env python3
import sys
import random

def greet(min_number, max_number, max_guesses):
    """Greet the user."""
    print('hello, human! would you like to play a game?')
    # Print instructions
    print(f"I'm thinking of a number between {min_number} and {max_number}. Can you find it in {max_guesses} or less?")


def play_game(min_number, max_number, max_guesses):
    # TODO:
    # Choose a random number:
    random_number = random.choice(range(0, max_number))
    
    for attempt in range(0, max_guesses):
        guess = int(input(f"Enter a number: "))
        if guess == random_number: 
            print("You won! The grand and glorious jackpot!")
            sys.exit()
        if guess > random_number: 
            print("Your guess is too high")
        if guess < random_number:
            print("Your guess is too low")
        ##if guess is not int 
    print("You are not the chosen brother, Eli. You brother Paul is the smart one, and he would try again.")
    
    
        # TODO:
        # Print a message showing the user's guess.
        # Check if the provided guess is correct.
        # If it is, print a congratulatory message and exit.
        # If not, say whether the guess was too low or too high.

    # We are now outside of the above for-loop.
    # If we reach this point, it means we have run out of guesses.
    # Insult the user, and invite them to try again (or not).


# The following line will evaluate to True when the script is executed directly (as opposed to being `import`ed from another python file):
if __name__ == "__main__":
    min_number = 0
    max_number = 10
    max_guesses = 3
    greet(min_number, max_number, max_guesses)
    play_game(min_number, max_number, max_guesses)

    print("~ fin ~")
    sys.exit() # (redundant, because this is not really necessary at the end of the program)
