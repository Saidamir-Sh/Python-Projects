"""Poor Man's Bar Chart."""
from pprint import pprint
from collections import defaultdict

def etaoin():
    """
    Accept sentence as input and print the frequency of each letter as dict.
    """

    sentence = input("Enter a sentence: ")
    sentence.lower()

    letters = {}

    for char in sentence:
        if char.isalpha():
            if char in letters:
                letters[char] = letters.get(char) + 1
            else:
                letters[char] = 0

    sorted_letters = sorted(letters.items(), key=lambda x: x[1])
    bar_chart = {letter: '*' * count for letter, count in sorted_letters}

    pprint(bar_chart)


def etaoin_improved():
    """
    Accept sentence as input and print the frequency of each letter as dict.
    """

    sentence = input("Enter a sentence: ")
    letter_counts = defaultdict(int)

    for char in sentence:
        if char.isalpha():
            letter_counts[char] += 1

    sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1])
    bar_chart = {letter: '*' * count for letter, count in sorted_letters}

    pprint(bar_chart)


if __name__ == "__etaoin_improved__":
    etaoin_improved()

etaoin_improved()

