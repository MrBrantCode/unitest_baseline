"""
QUESTION:
Create a function called `count_string_appearances` that takes a list of strings and a string as arguments, and returns the number of times the string appears in the list. If the list is empty or the string is empty, return -1.
"""

def count_string_appearances(strings, string):
    if len(strings) == 0 or len(string) == 0:
        return -1
    
    count = 0
    for word in strings:
        if word == string:
            count += 1
    return count