"""
QUESTION:
Create a function called `minimal_operations` that takes a string of characters as input and returns the minimal number of division/multiplication operations (equivalent to replacing a character) needed to make all characters within the string the same. The string can contain any characters, including lowercase and uppercase alphabets and special characters, and its length is between 1 and 100.
"""

def minimal_operations(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    max_frequency = max(frequency.values())
    
    operations = len(s) - max_frequency
    
    return operations