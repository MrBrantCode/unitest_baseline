"""
QUESTION:
Implement a function named `most_frequent_char(s)` that recursively finds the most frequent character in a given string `s` without using built-in functions or libraries. The function should return the most frequent character in the string. In case of ties, return the character that occurs first in the string. The input string `s` only contains lowercase letters.
"""

def most_frequent_char(s):
    # Base case: if the string is empty, return None
    if len(s) == 0:
        return None

    # Count the occurrences of the first character in the string
    count = s.count(s[0])

    # Recursive case: find the most frequent character in the remaining substring
    most_frequent = most_frequent_char(s[1:])

    # If the current character is more frequent than the most frequent character in the remaining substring,
    # or if there is no remaining substring, return the current character
    if most_frequent is None or count > s.count(most_frequent):
        return s[0]

    # Otherwise, return the most frequent character in the remaining substring
    return most_frequent