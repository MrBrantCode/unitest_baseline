"""
QUESTION:
Implement the `find_longest_common_substring` function to find the longest common substring between two input strings, with the following restrictions:
- The function should have a time complexity of O(n^3), where n is the length of the longer string.
- The function should handle cases where the strings can contain special characters and are case-sensitive.
- The function should not use any built-in functions or libraries specifically designed for string manipulation.
- The function should minimize the space complexity to O(1) by using constant space instead of creating any additional data structures.

The function should take two strings as input and return the longest common substring.
"""

def find_longest_common_substring(str1, str2):
    max_length = 0
    start_index = 0

    for i in range(len(str1)):
        for j in range(len(str2)):
            length = 0
            while (i + length < len(str1)) and (j + length < len(str2)) and (str1[i + length] == str2[j + length]):
                length += 1

            if length > max_length:
                max_length = length
                start_index = i

    return str1[start_index:start_index + max_length]