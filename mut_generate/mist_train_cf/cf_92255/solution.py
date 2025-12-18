"""
QUESTION:
Write a function `count_a_occurrences(string)` that takes a string as input and returns the number of times the letter 'a' appears in the string, ignoring any occurrences of 'a' that are followed by 'b'.
"""

def count_a_occurrences(string):
    count = 0
    i = 0
    while i < len(string):
        if string[i] == 'a':
            if i + 1 < len(string) and string[i + 1] == 'b':
                i += 2
                continue
            else:
                count += 1
        i += 1
    return count