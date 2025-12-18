"""
QUESTION:
Write a function called `reverse_and_concatenate_strings` that takes a list of strings as input. The function should concatenate the strings in reverse order into a single string, excluding any strings containing non-alphabetic characters. If the resulting string exceeds 100 characters in length, it should be truncated. If the resulting string is empty, return "No valid strings found." The input list is restricted to a maximum of 10 strings, each with a maximum length of 20 characters.
"""

def reverse_and_concatenate_strings(strings):
    valid_strings = [string for string in strings if string.isalpha()]
    valid_strings.reverse()
    result = ",".join(valid_strings)
    return result[:100] if result else "No valid strings found."