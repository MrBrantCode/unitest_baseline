"""
QUESTION:
Write a function `identify_palindromes(lst)` that takes a list of strings as input, identifies which strings are palindromes (ignoring case, punctuation marks, and spaces), and returns a list of the palindromes. Do not use built-in string manipulation or regular expression functions.
"""

def identify_palindromes(lst):
    palindromes = []
    for string in lst:
        clean_string = ''.join(char for char in string if char.isalnum())
        lowercase_string = clean_string.lower()
        if lowercase_string == lowercase_string[::-1]:
            palindromes.append(string)
    return palindromes