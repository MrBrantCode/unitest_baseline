"""
QUESTION:
Create a function called `sort_and_reverse_strings` that takes a list of strings as input, sorts them in descending order of length, reverses the order of characters in each string, and returns the sorted and reversed strings. The function should be able to handle strings with special characters and white spaces.
"""

def sort_and_reverse_strings(strings):
    # Sort the strings in descending order of length
    strings.sort(key=len, reverse=True)
    # Reverse the order of the characters for each string
    return [s[::-1] for s in strings]