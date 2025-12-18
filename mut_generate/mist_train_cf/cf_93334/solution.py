"""
QUESTION:
Write a function `count_letters(string)` that takes a string as input and returns a list of tuples, where each tuple contains a unique letter from the string (in lowercase) and its frequency. The list should be sorted in descending order based on the frequency. The function should ignore non-alphabetic characters and be case-insensitive.
"""

def count_letters(string):
    counts = {}
    string = string.lower()
    
    for char in string:
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts