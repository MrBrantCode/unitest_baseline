"""
QUESTION:
Write a function called `longest_substring` that takes a string as input and returns the length of the longest substring with non-repeating characters. The function should have a time complexity of O(n), where n is the length of the string.
"""

def longest_substring(string):
    # Handle edge cases
    if len(string) <= 1:
        return len(string)
    
    char_dict = {}  # To store characters and their last seen indices
    start = 0  # Starting index of the current window
    max_length = 0  # Maximum length of substring with non-repeating characters found so far
    
    for i in range(len(string)):
        if string[i] in char_dict and char_dict[string[i]] >= start:
            start = char_dict[string[i]] + 1
        char_dict[string[i]] = i
        
        current_length = i - start + 1
        if current_length > max_length:
            max_length = current_length
    
    return max_length