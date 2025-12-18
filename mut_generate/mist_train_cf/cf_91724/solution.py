"""
QUESTION:
Write a function named `longest_substring_without_repeated_characters` that takes a string as input and returns the longest substring without repeated characters. If there are multiple substrings of the same length, return the one that appears first in the original string.
"""

def longest_substring_without_repeated_characters(string):
    longest_substring = ""
    current_substring = ""

    for char in string:
        if char not in current_substring:
            current_substring += char
        else:
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
            current_substring = current_substring[current_substring.index(char) + 1:] + char

    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring

    return longest_substring