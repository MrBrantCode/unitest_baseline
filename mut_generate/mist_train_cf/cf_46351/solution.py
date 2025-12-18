"""
QUESTION:
Create a function called `detectAndCountPalindromes` that takes a string as input, and returns whether the string is a palindrome and counts the number of palindromic substrings within the given string. The palindrome detection should ignore white spaces, punctuation, and case sensitivity. The function should return a boolean value indicating whether the string is a palindrome and an integer value representing the number of palindromic substrings.
"""

import string
import re

def detectAndCountPalindromes(str):
    cleaned = str.lower()
    cleaned = re.sub('['+string.punctuation+']', '', cleaned)
    cleaned = re.sub('\s', '', cleaned)
    is_palindrome = cleaned == cleaned[::-1]
    count = 0
    length = len(cleaned)
    for i in range(length):
        for j in range(i+2,length+1):
            substring = cleaned[i:j]
            if substring == substring[::-1]:
                count += 1
    return is_palindrome, count