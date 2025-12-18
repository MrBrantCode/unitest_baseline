"""
QUESTION:
Create a function named `find_longest_string` that takes two strings `str1` and `str2` as arguments. The function should return the longest string after removing any duplicate characters. The function should be able to handle strings with a length of up to 100 characters and have a time complexity of O(n), where n is the length of the longest string. Do not use any built-in functions or libraries that can directly remove duplicate characters. Implement the logic to remove duplicate characters manually and optimize the function to use as little memory as possible.
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