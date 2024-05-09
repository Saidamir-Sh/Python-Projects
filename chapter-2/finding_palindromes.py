from load_dictionary import load

def find_palindromes():
    """
    Find palindromes from file
    
    Arguments:
        - file
    
    Returns::
        - str[] contains palindromes
    """
    word_list = load("words.txt")
    pali_list = []

    for word in word_list:
        if(len(word) > 1 and word == word[::-1]):
            pali_list.append(word)
    
    print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
    print(*pali_list, sep="\n")

word_list = load("./words.txt")

def is_palindrome(word: str):
    if len(word) == 0 or len(word) == 1:
        return True
    elif word[0] != word[len(word) - 1]:
        return False
    else:
        return is_palindrome(word[1, len(word) - 1])

def find_palingrams():
    pali_list = []
    words = set(word_list)

    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    pali_list.append((word, rev_word[end-i:i]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                    pali_list.append((rev_word[:end-i], word))

    return pali_list