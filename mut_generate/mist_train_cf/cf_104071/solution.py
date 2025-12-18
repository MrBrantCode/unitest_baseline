"""
QUESTION:
Write a function `manipulate_list` that takes a list of strings as input, removes any elements that contain the letter 'o', and returns a single string formed by concatenating the remaining elements together.
"""

def manipulate_list(strings):
    # Remove elements containing 'o'
    strings = [string for string in strings if 'o' not in string]
    
    # Concatenate the remaining elements
    result = ''.join(strings)
    
    return result