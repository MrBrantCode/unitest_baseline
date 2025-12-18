"""
QUESTION:
Write a function `longest_substring(input_string)` that takes a string of characters as input and returns the longest continuous substring consisting of the same character. The function should operate iteratively and handle Unicode characters efficiently. If the input string contains multiple substrings of the same maximum length, the function can return any of them.
"""

def longest_substring(input_string):
    max_substring = ''
    current_substring = ''

    for index in range(len(input_string)):
        if index == 0 or input_string[index] != input_string[index-1]:
            current_substring = input_string[index]
        else:
            current_substring += input_string[index]
            
        if len(current_substring) > len(max_substring):
            max_substring = current_substring

    return max_substring