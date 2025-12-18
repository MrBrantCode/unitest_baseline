"""
QUESTION:
Create a function `find_z_vowels(word)` that takes a string `word` as input. The function should return the index of the character 'z' if it exists in the word (excluding the first and last characters), and is surrounded by vowels on both sides. If no such 'z' is found, return -1. The function should be case-insensitive.
"""

def find_z_vowels(word):
    # Making the word lower case to disregard letter casing
    word = word.lower()
    
    # Check if the word is less than 3 characters long. If so, return -1 immediately 
    # because the word will not be able to satisfy the condition.
    if len(word) < 3:
        return -1
    
    # Define the vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for i in range(1, len(word) - 1):
        # Check if the character is 'z'
        if word[i] == 'z':
            # Check if the characters before and after 'z' are vowels
            if word[i - 1] in vowels and word[i + 1] in vowels:
                # If the conditions are met, return the position index of 'z'
                return i
                
    # If the conditions are not met, return -1
    return -1