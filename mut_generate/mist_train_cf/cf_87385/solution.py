"""
QUESTION:
Write a function named `count_distinct_vowels` that takes a string of characters as input and returns the number of distinct vowels in it. The function should be case-insensitive and consider both uppercase and lowercase vowels as the same. The function should also exclude any vowels that appear more than once consecutively in the string. The input string will contain at most 100 characters.
"""

def count_distinct_vowels(string):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    distinct_vowels = set()
    string = string.lower()
    prev_char = None
    
    for char in string:
        if char in vowels:
            if char != prev_char:
                distinct_vowels.add(char)
        prev_char = char
    
    return len(distinct_vowels)