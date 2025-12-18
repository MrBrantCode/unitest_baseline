"""
QUESTION:
Write a function named `count_characters` that takes a string as input, handles uppercase and lowercase characters as separate entities, ignores special characters and punctuation marks, and returns a dictionary containing the frequency of each character in the string.
"""

def count_characters(string):
    frequencies = {}
    
    for char in string:
        if char.isalpha():  
            char = char.lower()  
            
            if char in frequencies:
                frequencies[char] += 1
            else:
                frequencies[char] = 1
    
    return frequencies