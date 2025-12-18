"""
QUESTION:
Write a function named `count_common_characters` that takes two string parameters. The function should return the number of common alphabetic characters between the two strings. If either string is empty or contains non-alphabetic characters, the function should return "Error: Invalid strings". You can only use basic string manipulation operations such as indexing and concatenation.
"""

def count_common_characters(string_1, string_2):
    if len(string_1) == 0 or len(string_2) == 0 or not string_1.isalpha() or not string_2.isalpha():
        return "Error: Invalid strings"

    count = 0
    for char in string_1:
        if char in string_2:
            count += 1

    return count