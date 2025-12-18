"""
QUESTION:
Find all strings in a list that are composed of 'n' characters and contain a given substring. The function should handle case sensitivity, overlapping occurrences of the substring, and substrings found towards the end of a string that exceed 'n' characters.

The function should be named `find_substrings` and take four parameters: `string_list`, `sub_string`, `case_sensitive` (optional, defaulting to `True`), and `length_n` (optional, defaulting to `0`). It should return a list of matching strings or a custom message if no matches are found or the input is invalid.
"""

def find_substrings(string_list, sub_string, case_sensitive=True, length_n=0):
    if not string_list or not sub_string: 
        return "Input is not valid" 
    
    matched_items = []

    for word in string_list:
        
        if len(word) != length_n:
            continue
        
        if case_sensitive and sub_string in word:
            matched_items.append(word)
        elif not case_sensitive and sub_string.lower() in word.lower():
            matched_items.append(word)
        
    if len(matched_items) > 0:
        return matched_items
    
    if length_n > 0:
        return "No suitable matches found."
    else:
        return "No matches found."