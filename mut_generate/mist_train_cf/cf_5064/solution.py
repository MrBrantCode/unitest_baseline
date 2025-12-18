"""
QUESTION:
Write a function named `reverse_sort_palindrome` to take a string of words as input, reverse each word, ensure each word is a palindrome, then sort the words in alphabetical order and return them as a string. The input string contains only spaces and alphabets, and ignore case sensitivity.
"""

def reverse_sort_palindrome(s):
    """
    This function takes a string of words, reverses each word, checks if it's a palindrome, 
    and returns the palindromes in alphabetical order.

    Parameters:
    s (str): The input string of words.

    Returns:
    str: A string of palindromes in alphabetical order.
    """
    words = s.lower().split()
    reversed_words = [word[::-1] for word in words]
    palindromes = [word for word in reversed_words if word == word[::-1]]
    return ' '.join(sorted(palindromes))