"""
QUESTION:
Create a function named `count_characters` that takes a string as input and returns a dictionary where keys are non-vowel characters and values are their occurrences in the string. The occurrences should be case-sensitive. The time complexity of the solution should be less than O(n^2), where n is the length of the string.
"""

def count_characters(string):
    char_counts = {}
    for char in string:
        if char.lower() in 'aeiou':
            continue
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts