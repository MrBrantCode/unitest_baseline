"""
QUESTION:
Create a function `count_strings` that takes a list of strings as input and returns a dictionary where each key is a unique string from the input list and its corresponding value is the frequency of that string in the list. The function should not utilize any built-in Python functions or libraries.
"""

def count_strings(strings):
    counts = {}
    for string in strings:
        if string in counts:
            counts[string] += 1
        else:
            counts[string] = 1
    return counts