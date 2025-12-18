"""
QUESTION:
Create a function named `remove_duplicates` that takes an input string, removes all duplicate characters regardless of case sensitivity, and returns a new string consisting only of unique characters sorted alphabetically.
"""

def remove_duplicates(input_str):
    # convert to lowercase and create a list of characters
    char_list = list(input_str.lower())
    
    # remove duplicates and sort the list
    unique_chars = sorted(set(char_list))
    
    # join the list back into a string
    output_str = ''.join(unique_chars)
    
    return output_str