"""Pig Latin game"""
import sys

def pig_latin():
    """Accept english word as input and translate it to Pig Latin."""
    print("Welcome to Pig Latin\n")

    while True:

        word = input("Enter a word: ")

        if not word.isalpha():
            print("Please check your input, it should contain only letters !", file=sys.stderr)

        try_again = input("Play again ? (Press Enter to continue or press n to quit.) ")

        if try_again.lower() not in ['', 'n']:
            print("Entered invalid choice", file=sys.stderr)

        if try_again.lower() == "n":
            break

if __name__ == "__pig_latin__":
    pig_latin()

pig_latin()