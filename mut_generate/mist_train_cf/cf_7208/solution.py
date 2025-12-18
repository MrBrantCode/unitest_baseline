"""
QUESTION:
Write a function named "is_substring" that takes two string parameters, "string1" and "string2". The function should return a boolean value indicating whether "string1" is a substring of "string2" or not, considering the following requirements:

- The function should trim leading and trailing whitespaces from both "string1" and "string2" before performing the substring comparison.
- The function should ignore case when comparing the strings.
- The function should not use any built-in functions or methods that directly solve this problem.
- The function should have a time complexity of O(n), where n is the length of "string2".
"""

def is_substring(string1, string2):
    # Trim leading and trailing whitespaces
    string1 = string1.strip()
    string2 = string2.strip()

    # Check if string1 is longer than string2
    if len(string1) > len(string2):
        return False

    # Convert both strings to lowercase
    string1 = string1.lower()
    string2 = string2.lower()

    # Loop through string2 and check for substring
    for i in range(len(string2) - len(string1) + 1):
        if string2[i:i + len(string1)] == string1:
            return True

    return False