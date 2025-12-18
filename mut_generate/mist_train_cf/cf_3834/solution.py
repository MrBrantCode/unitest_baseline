"""
QUESTION:
Write a function called `min_operations` that takes a string of characters and returns the minimal number of division/multiplication operations needed to make all characters within the string the same. The string can contain any characters, including lowercase and uppercase alphabets, special characters, numbers, and spaces. The length of the string will be between 1 and 100.
"""

def min_operations(s):
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    max_occurrence = max(char_counts.values())
    
    min_operations = len(s) - max_occurrence
    
    return min_operations