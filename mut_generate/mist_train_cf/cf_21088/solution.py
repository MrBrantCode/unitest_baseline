"""
QUESTION:
Create a function `find_longest_substring(input_string)` that takes a string as input, considers only alphabetic characters, and returns the longest substring without repeating characters and its length. The function should handle cases where the input string contains special characters, numbers, whitespace, is empty, or is a single character. Implement an optimal algorithm or data structure without using built-in functions or libraries that directly solve the problem.
"""

def find_longest_substring(input_string):
    max_length = 0
    current_length = 0
    longest_substring = ""
    current_substring = ""
    char_set = set()

    for char in input_string:
        if char.isalpha():
            if char in current_substring:
                if current_length > max_length:
                    max_length = current_length
                    longest_substring = current_substring
                current_substring = char
                current_length = 1
            else:
                current_substring += char
                current_length += 1
                if current_length > max_length:
                    max_length = current_length
                    longest_substring = current_substring

    return longest_substring, max_length