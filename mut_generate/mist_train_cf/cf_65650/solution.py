"""
QUESTION:
Write a function `find_all_substrings(input_string)` that generates all possible substrings of a given input string. The function should return a list of all substrings, including single characters and the input string itself.
"""

def find_all_substrings(input_string):
    substrings = []
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string) + 1):
            substrings.append(input_string[i:j])
    return substrings