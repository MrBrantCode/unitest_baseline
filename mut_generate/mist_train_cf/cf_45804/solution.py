"""
QUESTION:
Design a function `longest_substring` that finds the longest substring with unique characters in a given string. The function should take a string as input and return the longest substring without repeating characters. The function should be efficient and scalable to handle strings of any length.
"""

def longest_substring(string):
    max_length = 0
    max_substring =''
    visited = {}    # To store last found index of character
    substring_start = 0  # Starting index of current substring

    for i in range(len(string)):
        if string[i] in visited:
            if visited[string[i]] >= substring_start:
                substring_start = visited[string[i]] + 1
        # update the last index of the character
        visited[string[i]] = i 

        if i - substring_start + 1 > max_length:
            max_length = i - substring_start + 1
            max_substring = string[substring_start:i+1]
    return max_substring