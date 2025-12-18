"""
QUESTION:
Write a function `find_unique_palindromes(word_list)` that identifies and returns all unique palindromic lexemes in a given list of words, ignoring case sensitivity. If no palindromic lexeme exists, the function should return "No palindromic lexemes found". The function should only count each unique palindromic lexeme once, even if it appears multiple times in the input list.
"""

def find_unique_palindromes(word_list):
    palindromes = set()

    for word in word_list:
        word_lower = word.lower() # convert to lower case to ensure case-insensitivity
        if word_lower == word_lower[::-1]: # check if the word is a palindrome
            palindromes.add(word) # if it is, add it to the set (automatically handles duplicates)

    if len(palindromes) == 0:
        return "No palindromic lexemes found"
    else:
        return list(palindromes)