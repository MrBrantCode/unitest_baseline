"""
QUESTION:
Create a function `process_strings(strings)` that takes a list of strings as input. The function should return a new list containing the input strings converted to uppercase, excluding any strings that contain numbers or special characters. The output list should be sorted in descending order based on the length of the strings.
"""

def process_strings(strings):
    processed_strings = []
    
    for string in strings:
        if string.isalpha():
            processed_strings.append(string.upper())
    
    processed_strings.sort(reverse=True, key=lambda x: len(x))
    
    return processed_strings