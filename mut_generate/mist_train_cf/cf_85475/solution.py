"""
QUESTION:
Create a function `anagram_checker` that takes three strings as input and returns a boolean value. The function should check if the first two strings are anagrams of each other, considering case-sensitivity and frequency of each letter, and ignoring white spaces. If they are anagrams, the function should then check if all characters from the third string exist in the anagram. The function should return `True` if both conditions are met and `False` otherwise.
"""

from collections import Counter

def anagram_checker(str1, str2, str3):
    # Removing spaces and converting all letters to lower case
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()
    str3 = str3.replace(' ','').lower()

    # Checking if two strings are anagrams
    if Counter(str1) == Counter(str2):
        # Checking if characters from third string exist in the anagram
        for char in str3:
            if char not in str1:
                return False
        return True
    else:
        return False