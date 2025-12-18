"""
QUESTION:
Design a function `reverse_and_remove_duplicates` that takes a string input, removes non-alphabet characters, reverses the order of its words, and excludes any consecutive duplicate words in the reversed string. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.
"""

import re

def reverse_and_remove_duplicates(s):
    # Remove non-alphabet characters from the string
    cleaned_string = re.sub(r'[^a-zA-Z\s]', '', s)
    
    # Split the cleaned string into words
    words = cleaned_string.split()
    
    # Reverse the order of words
    reversed_words = words[::-1]
    
    # Remove consecutive duplicate words
    result = []
    for i in range(len(reversed_words)):
        if i == 0 or reversed_words[i] != reversed_words[i-1]:
            result.append(reversed_words[i])
    
    # Join the words back into a string
    reversed_string = ' '.join(result)
    
    return reversed_string