"""
QUESTION:
Create a function called `find_longest_string` that takes two strings as input and returns the longest string with no duplicate characters. The function should handle strings of up to 100 characters, have a time complexity of O(n) where n is the length of the longest string, and use no built-in functions or libraries that directly remove duplicate characters.
"""

def find_longest_string(str1, str2):
    longest = str1 if len(str1) > len(str2) else str2
    unique_chars = set()
    longest_without_duplicates = []

    for char in longest:
        if char not in unique_chars:
            unique_chars.add(char)
            longest_without_duplicates.append(char)

    return ''.join(longest_without_duplicates)