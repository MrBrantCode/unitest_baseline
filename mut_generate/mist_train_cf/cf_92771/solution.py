"""
QUESTION:
Create a function `longest_substring_without_repeating_characters` that takes a string as input and returns the longest substring without repeating alphabetic characters along with its length. The function should only consider alphabetic characters and ignore special characters, numbers, or whitespace. It should handle cases where the input string is an empty string or a single character, and it should be optimized to find the longest substring without repeating characters in an efficient manner.
"""

def longest_substring_without_repeating_characters(s):
    if len(s) == 0:
        return "", 0

    longest_substring = ""
    current_substring = ""
    char_set = set()

    for char in s:
        if char.isalpha():
            if char not in char_set:
                char_set.add(char)
                current_substring += char
            else:
                if len(current_substring) > len(longest_substring):
                    longest_substring = current_substring
                current_substring = char
                char_set = set(char)

    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring

    return longest_substring, len(longest_substring)