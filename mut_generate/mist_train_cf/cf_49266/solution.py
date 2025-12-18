"""
QUESTION:
Write a function named `char_frequency` that calculates the frequency of each character in a given string. The function should ignore case sensitivity, treating uppercase and lowercase characters as the same, and ignore spaces. Given a character, return its frequency. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def char_frequency(string):
    frequency = {}
    
    for char in string:
        if char == " ":
            continue
        char = char.lower()
        
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            
    return frequency