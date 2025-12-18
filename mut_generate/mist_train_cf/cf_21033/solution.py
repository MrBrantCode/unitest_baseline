"""
QUESTION:
Create a function `find_longest_common_substring(str1, str2)` that finds the longest common substring from two given strings `str1` and `str2`. The function should have a time complexity of O(n^3), where n is the length of the longer string. The function should handle cases where the strings can contain special characters and are case-sensitive, and it should not use any built-in functions or libraries specifically designed for string manipulation. The function should minimize space complexity to O(1) by using constant space instead of creating any additional data structures.
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