"""
QUESTION:
Write a function `longest_substring_length(string)` that takes a string as input and returns the length of the longest substring without any repeated characters. The function should handle strings with repeated and non-repeated characters. The function should not return the actual substring, only its length.
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