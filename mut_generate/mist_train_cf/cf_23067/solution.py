"""
QUESTION:
Create a method named `remove_duplicates` that takes a string as input and returns a string with all duplicate characters removed while maintaining the original order of the characters. The method should handle any printable ASCII characters, including alphanumeric characters, special characters, and punctuation. The time complexity should be O(n), where n is the length of the input string, and the method should not use any built-in string manipulation functions or regular expressions.
"""

def remove_duplicates(string):
    seen = set()
    result = []

    for char in string:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return ''.join(result)