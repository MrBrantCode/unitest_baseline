"""
QUESTION:
Write a function `count_substring_occurrences(string, substring)` that takes a string and a substring as input and returns the number of occurrences of the substring in the string, ignoring occurrences that are part of a larger word. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1). The function should also handle case-insensitive matching.
"""

def count_substring_occurrences(string, substring):
    count = 0
    i = 0

    while i < len(string):
        # Find the next occurrence of the substring, ignoring case
        index = string.lower().find(substring.lower(), i)

        if index == -1:
            break

        # Check if the found occurrence is part of a larger word
        if (index == 0 or not string[index-1].isalpha()) and \
                (index + len(substring) == len(string) or not string[index + len(substring)].isalpha()):
            count += 1

        i = index + 1

    return count