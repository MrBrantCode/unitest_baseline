"""
QUESTION:
Write a function `count_a` that takes a string as input and returns the number of times the letter 'a' appears, excluding any occurrences of 'a' that are immediately followed by the letter 'b'.
"""

def count_a(string):
    count = 0
    i = 0
    while i < len(string):
        if string[i] == 'a':
            if i + 1 < len(string) and string[i + 1] == 'b':
                i += 2
                continue
            count += 1
        i += 1
    return count