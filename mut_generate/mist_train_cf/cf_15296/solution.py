"""
QUESTION:
Write a function named `reverse_string` that takes a string of comma-separated words as input, reverses the order of the words, and returns the modified string. The function should be able to handle any number of words separated by commas and should not include a trailing comma in the output.
"""

def entrance(s):
    words = s.split(',')
    result = ""
    
    for word in reversed(words):
        result += word + ","
    
    result = result.rstrip(',')
    
    return result