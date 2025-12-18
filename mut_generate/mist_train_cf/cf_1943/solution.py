"""
QUESTION:
Write a function `process_string` that takes a string of words as input and returns `True` if the number of words with an odd number of vowels is greater than 5 after removing duplicates and sorting the words in descending order of their vowel count, and `False` otherwise.
"""

def process_string(string):
    # Split the string into a list of words
    words = string.split()
    
    # Remove any duplicates
    words = list(set(words))
    
    # Sort the words in descending order based on the number of vowels present in each word
    words.sort(key=lambda word: sum(1 for char in word if char.lower() in 'aeiou'), reverse=True)
    
    # Count the number of words that have an odd number of vowels
    odd_vowels_count = sum(1 for word in words if sum(1 for char in word if char.lower() in 'aeiou') % 2 != 0)
    
    # Return True if the count is greater than 5; otherwise, return False
    return odd_vowels_count > 5