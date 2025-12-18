"""
QUESTION:
Write a function `remove_consecutive_duplicates` that takes a string as input and modifies it in-place to remove consecutive duplicates, considering different cases, such that the function only uses a constant amount of additional space. The input string will only contain alphabetic characters.
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