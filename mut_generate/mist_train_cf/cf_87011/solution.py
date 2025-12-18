"""
QUESTION:
Write a function called `first_repeated_letter` that finds the index of the first repeated letter in a given string, ignoring any whitespace characters. The string only contains lowercase letters and whitespace characters, and its length is at most 10^5. If there are no repeated letters, return -1.
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