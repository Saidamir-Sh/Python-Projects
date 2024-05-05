import load_dictionary

def find_palindromes(file):
    """
    Find palindromes from file
    
    Arguments:
        - file
    
    Returns::
        - str[] contains palindromes
    """
    word_list = load_dictionary("words.txt")
    pali_list = []

    for word in word_list:
        if(len(word) > 1 and word == word[::-1]):
            pali_list.append(word)
    
    print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
    print(*pali_list, sep="\n")