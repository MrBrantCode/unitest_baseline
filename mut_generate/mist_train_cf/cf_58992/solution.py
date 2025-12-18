"""
QUESTION:
Write a function `is_anagram_of_palindrome(word)` that determines whether a given string can be rearranged into a palindrome. The function should return a boolean value and is case-sensitive, treating 'A' and 'a' as distinct characters.
"""

def is_anagram_of_palindrome(word):
    char_dict = {}
    for char in word:
        char_dict[char] = char_dict.get(char, 0) + 1
    
    odd_count = sum(value%2 for value in char_dict.values())
    return odd_count <= 1