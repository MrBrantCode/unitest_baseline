"""
QUESTION:
Create a function `longest_substring_without_repeating_characters` that takes a string as input and returns the longest substring without repeating alphabetic characters and its length. The function should ignore non-alphabetic characters and handle cases where the input string is empty or contains a single character. The function should use an efficient algorithm or data structure to solve the problem, avoiding checking all possible substrings.
"""

def longest_substring_without_repeating_characters(string):
    if len(string) == 0:
        return "", 0

    longest_substring = ""
    current_substring = ""
    char_set = set()

    for char in string:
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