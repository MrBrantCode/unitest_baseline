"""
QUESTION:
Write a function `first_repeated_letter(string)` that finds the index of the first repeated letter in a string, ignoring whitespace characters. The string will only contain lowercase letters and whitespace characters, and its length will be at most 10^5. If no repeated letters are found, return -1.
"""

def first_repeated_letter(string):
    seen = set()
    for i, c in enumerate(string):
        if c == ' ':
            continue
        if c in seen:
            return i
        seen.add(c)
    return -1