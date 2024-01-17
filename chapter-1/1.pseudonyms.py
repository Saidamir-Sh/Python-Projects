"""
Objective: 
Randomly generate funny sidekick names using Python code that conforms to established
style guidelines
"""

# load list of first and last names
# choose first name randomly and second name
# assign to variable
# if user quits playing end and exit if not repeat

import sys
import random

print("Welcome to the Psych 'Sidekick Name Picker.' \n")
print("A name just like Sean would pick for Gus:. \n\n")

# First names
first_names = ('Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack',
               'Karen', 'Leo', 'Mia', 'Noah', 'Olivia', 'Paul', 'Quinn', 'Rachel', 'Samuel', 'Tara')

# Last names
last_names = ('Anderson', 'Brown', 'Carter', 'Davis', 'Evans', 'Fisher', 'Garcia', 'Hill', 'Irwin', 'Johnson',
              'Keller', 'Lopez', 'Martinez', 'Nelson', 'Owens', 'Perez', 'Quinn', 'Reyes', 'Smith', 'Taylor')

while True:
    first_name = random.choice(first_names) # randomly choice from the sequence
    last_name = random.choice(last_names)

    print("\n\n")
    print("{} {}".format(first_name, last_name), file=sys.stderr) # string.format(val1, val2) formats the values and inserts them in string
    print("\n\n")

    try_again = input("\n\nTry again? (Press Enter else n to quiq)\n")
    if try_again.lower() == "n":
        break

    input("\nPress Enter to exit.")


# New concepts:
    
    # what is standard I/O stream ? - > interconnected input and output communication channels between a computer program and its environment when it begins execution
    # different I/O streams : stdin, stdout, stderr
    
    # sys.stdout -> standard output stream. default destination of print(file=)
    # these below 2 codes are almost same (please google the difference):
    # print("this is string")
    # sys.stdout.write("this is string")

    # sys.stderr -> standart error stream. Used for error messages or warnings
    # usage:
    # except ValidationError as e:
        # print(f"Error: {e}", file=sys.stderr)