"""
QUESTION:
Write a function `remove_consecutive_duplicates` that takes a string of alphabetic characters as input, removes consecutive duplicates (case-insensitive) from the string in-place, and returns the modified string. The function should only use a constant amount of additional space.
"""

def remove_consecutive_duplicates(string):
    length = len(string)
    if length < 2:
        return string
    
    j = 1
    for i in range(1, length):
        if string[i].lower() != string[i-1].lower():
            string[j] = string[i]
            j += 1
    
    string[j:] = []  # Remove remaining characters
    
    return string[:j]