"""
QUESTION:
Write a function `most_frequent_letter(s)` that takes a string `s` as input and returns the most frequent letter in the string. If there are multiple letters with the same highest frequency, return the letter that appears first in the string. If the string is empty or contains non-alphabetic characters, return an empty string. The string `s` has a maximum length of 10^5 characters.
"""

def most_frequent_letter(s):
    """
    This function finds the most frequent letter in a given string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    str: The most frequent letter in the string. If there are multiple letters with the same highest frequency, 
         return the letter that appears first in the string. If the string is empty or contains non-alphabetic 
         characters, return an empty string.
    """
    s = ''.join(filter(str.isalpha, s)).lower()
    if not s:
        return ''

    letter_count = {}
    for letter in s:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    max_count = max(letter_count.values())
    most_frequent = next(letter for letter, count in letter_count.items() if count == max_count)
    return most_frequent