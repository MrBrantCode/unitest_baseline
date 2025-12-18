"""
QUESTION:
Write a function called `most_frequent_char` that takes a string `s` as input and returns the most frequent character in the string. The function must be recursive and cannot use any built-in functions or libraries. If there is a tie, the function should return the character that occurs first in the string.
"""

def most_frequent_char(s):
    # Base case: if the string is empty, return None
    if len(s) == 0:
        return None

    # Count the occurrences of the first character in the string
    count = 0
    for char in s:
        if char == s[0]:
            count += 1

    # Recursive case: find the most frequent character in the remaining substring
    most_frequent = most_frequent_char(s[1:])

    # If the current character is more frequent than the most frequent character in the remaining substring,
    # or if there is no remaining substring, return the current character
    if most_frequent is None or count > 0 and (most_frequent is None or count > s.count(most_frequent)):
        return s[0]

    # Otherwise, return the most frequent character in the remaining substring
    return most_frequent