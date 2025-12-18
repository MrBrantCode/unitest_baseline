"""
QUESTION:
Develop a function called `generate_dict(s)` that generates a dictionary where keys are individual characters of a given string `s` and their corresponding values are the combined ASCII values of the key character and its preceding character in the string. If the key character is the first character in the string, its associated value should be twice its ASCII value. The function should handle repeat characters by considering only the first occurrence of the character, and it should be case-sensitive, treating lowercase and uppercase characters as distinct.
"""

def generate_dict(s):
    if not s:  # If the string is empty, return empty dict
        return {}

    result = {s[0]: ord(s[0]) * 2}
    for i in range(1, len(s)):
        if s[i] not in result:
            result[s[i]] = ord(s[i]) + ord(s[i - 1])

    return result