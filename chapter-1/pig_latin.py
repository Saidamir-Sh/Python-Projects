"""Pig Latin game"""
import sys

def pig_latin():
    """Accept english word as input and translate it to Pig Latin."""
    print("Welcome to Pig Latin\n")

    vowels = ["a","e","i","o","u"]

    while True:
        word = input("Enter a word: ")

        if word.isalpha():
            if word[0].lower() in vowels:
                print(f"Translation: {word}way\n\n")
            else:
                print(f"Translation: {word[1:]}{word[0]}ay\n\n")
        else:
            print("Enter only letters", file=sys.stderr)

        try_again = input("Continue ? (Press Enter or n to quit.)")

        if try_again.lower() == "n":
            break

if __name__ == "__pig_latin__":
    pig_latin()
