"""
QUESTION:
Write a function called `remove_duplicates` that takes a string `input_str` as input, removes all duplicate characters while ignoring case sensitivity, and returns a new string consisting of unique characters in alphabetical order.
"""

def remove_duplicates(input_str):
    # convert to lowercase and create a list of characters
    char_list = list(input_str.lower())
    
    # remove duplicates and sort the list
    unique_chars = sorted(set(char_list))
    
    # join the list back into a string
    output_str = ''.join(unique_chars)
    
    return output_str