"""
QUESTION:
Implement a function `is_anagram(str1, str2)` that takes two strings as input and returns `True` if they are anagrams and `False` otherwise. An anagram is a word or phrase formed by rearranging the letters of another word or phrase. The function should ignore case and whitespace differences between the strings.
"""

def is_anagram(str1, str2):
    # Remove spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Sort the characters in both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Check if the sorted strings are equal
    return sorted_str1 == sorted_str2