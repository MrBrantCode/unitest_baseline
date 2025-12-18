"""
QUESTION:
Write a function called `find_unique_substrings` that takes a string as input and returns a list of unique substrings with a length of 3 or more characters. The function should not include any duplicate substrings in the output.
"""

def find_unique_substrings(s):
    unique_substrings = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            unique_substrings.add(s[i:j])
    return list(unique_substrings)