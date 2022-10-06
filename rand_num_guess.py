#!/usr/bin/env python3
# Created by: Patrice Pat-Odita
# Created on: Oct 06, 2022.
# This program asks the user to guess a
# number and if they get it wrong they are told so.
import random


def main():
    # a number between 0 and 9
    random_variable = random.randint(0, 3)
    # Get number from user
    number_guessed = int(input("Guess my favorite number from 0-9: "))
    print("")

    # Check to see if they got the right number or wrong
    if number_guessed == random_variable:
        print("YOU GOT IT RIGHT!")
    else:
        print("You got it wrong...")
        print("my favorite number is {} ".format(random_variable))


if __name__ == "__main__":
    main()
