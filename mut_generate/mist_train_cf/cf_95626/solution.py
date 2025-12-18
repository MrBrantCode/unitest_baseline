"""
QUESTION:
Create a function `count_characters` that takes a string as input and returns a dictionary where keys are characters in the string and values are their occurrences. The function should exclude vowels from the dictionary and be case-sensitive, treating uppercase and lowercase versions of the same character as separate characters. The time complexity of the solution should be less than O(n^2), where n is the length of the string.
"""

def count_characters(string):
    char_counts = {}
    for char in string:
        if char.lower() in 'aeiou':
            continue
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts