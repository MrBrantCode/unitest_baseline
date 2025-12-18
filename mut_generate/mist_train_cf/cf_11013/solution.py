"""
QUESTION:
Create a function called `count_characters` that takes a string as input and returns a dictionary containing the frequency of alphabetic characters in the string, handling uppercase and lowercase characters as separate entities and ignoring non-alphabetic characters.
"""

def count_characters(string):
    frequencies = {}
    
    for char in string:
        if char.isalpha():  
            if char in frequencies:
                frequencies[char] += 1
            else:
                frequencies[char] = 1
    
    return frequencies