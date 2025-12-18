"""
QUESTION:
Implement a recursive function `find_last_index` that takes two arguments: `string` and `substring`. The function should return the index of the starting position of the last occurrence of the `substring` in the `string`, ignoring any leading and trailing whitespaces in both the `string` and the `substring` and performing a case-insensitive comparison. If the `substring` is not found, return -1.
"""

def find_last_index(string, substring):
    # Remove leading and trailing whitespaces, convert to lowercase
    string = string.strip().lower()
    substring = substring.strip().lower()

    # Check if substring is longer than string
    if len(substring) > len(string):
        return -1

    # Check if substring is found at the end of the string
    if string[-len(substring):] == substring:
        return len(string) - len(substring)

    # Recursively search for the substring in the remaining string
    result = find_last_index(string[:-1], substring)

    # If substring is not found, return -1
    if result == -1:
        return -1

    # Add the length of the substring to the result
    return result + len(substring)