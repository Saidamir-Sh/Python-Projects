"""Generate funny names by randomly combining names from 2 separate lists."""
import sys
import random

def main():
    """Choose names at random from 2 tuples of names and print to screen."""
    print("Welcome to the Psych 'Sidekick Name Picker.' \n")
    print("A name just like Sean would pick for Gus:. \n\n")

    first = ('Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack',
               'Karen', 'Leo', 'Mia', 'Noah', 'Olivia', 'Paul', 'Quinn', 'Rachel', 'Samuel', 'Tara')

    last = ('Anderson', 'Brown', 'Carter', 'Davis', 'Evans', 'Fisher', 'Garcia', 'Hill', 'Irwin', 'Johnson',
              'Keller', 'Lopez', 'Martinez', 'Nelson', 'Owens', 'Perez', 'Quinn', 'Reyes', 'Smith', 'Taylor')
    
    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)

        print("\n\n")
        # Trick IDLE by using "fatal error" setting print name in red.
        print("{} {}".format(first_name, last_name), file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nTry again ? (Press Enter else n to quit)\n")

        if try_again.lower() == "n":
            break

        input("Press Enter to ext.")

if __name__ == "__main__":
    main()