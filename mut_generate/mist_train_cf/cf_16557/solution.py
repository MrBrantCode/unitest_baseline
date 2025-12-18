"""
QUESTION:
Create a function named `filter_strings` that takes a list of strings `lst` and an integer `n` as input, filters out strings that have more than `n` characters, do not contain at least one vowel, or do not start with a capital letter, and returns the remaining strings in alphabetical order as a comma-separated string.
"""

def filter_strings(lst, n):
    filtered_strings = [string for string in lst 
                       if len(string) <= n 
                       and any(char in 'aeiouAEIOU' for char in string) 
                       and string[0].isupper()]
    
    return ', '.join(sorted(filtered_strings))