"""
QUESTION:
Write a function named `longest_substring` that takes an input string as a parameter. This function should return the longest continuous segment of a unique character in the input string. The function should handle Unicode characters and single-character strings where a single character forms the longest repeated sequence. The function should be implemented using iterative loops.
"""

def longest_substring(input_string):
    curr_longest_substring = ""
    longest_substring = ""
    prev_char = ''

    for char in input_string:
        if char == prev_char:
            curr_longest_substring += char
        else:
            if len(curr_longest_substring) > len(longest_substring):
                longest_substring = curr_longest_substring
            curr_longest_substring = char
        
        prev_char = char

    if len(curr_longest_substring) > len(longest_substring):
        longest_substring = curr_longest_substring

    return longest_substring