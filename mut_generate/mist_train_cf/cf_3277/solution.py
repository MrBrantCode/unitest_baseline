"""
QUESTION:
Create a function `longest_substring_length` that calculates the length of the longest substring of a given string that does not contain any repeated characters. The function should take a string as input and return the length of the longest substring without repeated characters. The function should be able to handle strings with repeated and non-repeated characters.
"""

def longest_substring_length(string):
    max_length = 0
    current_length = 0
    visited = {}

    for i in range(len(string)):
        if string[i] in visited:
            current_length = min(current_length + 1, i - visited[string[i]])
        else:
            current_length += 1

        visited[string[i]] = i
        max_length = max(max_length, current_length)

    return max_length