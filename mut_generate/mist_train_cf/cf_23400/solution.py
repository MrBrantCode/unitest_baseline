"""
QUESTION:
Write a function called `find_substring` that takes a string `str` as input and returns a list of all possible substrings in the given string. The function should consider substrings of all lengths, from 1 to the length of the input string.
"""

def find_substring(str):
    substrings = []
    for length in range(1, len(str)+1):
        for start in range(len(str)- length + 1):
            substrings.append(str[start:start+length])
    return substrings