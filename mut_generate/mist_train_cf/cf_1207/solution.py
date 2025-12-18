"""
QUESTION:
Implement a function `longest_common_prefix(strings)` that finds the longest common prefix string from an array of strings. The function should return the common prefix if it is at least 10 characters long; otherwise, it should return the actual longest common prefix found. The input array can contain up to 500 strings, each with a maximum length of 200 characters, and may include uppercase and lowercase letters, numbers, special characters, and non-ASCII characters. The function should achieve a time complexity of O(n*m), where n is the length of the input array and m is the maximum length of the strings, and should not use any built-in functions or libraries for string manipulation, sorting, or comparison.
"""

def longest_common_prefix(strings):
    if len(strings) == 0:
        return ""

    longest_prefix = ""
    first_string = strings[0]

    for i in range(len(first_string)):
        current_char = first_string[i]
        for string in strings[1:]:
            if i >= len(string) or string[i] != current_char:
                return longest_prefix
        longest_prefix += current_char

    if len(longest_prefix) >= 10:
        return longest_prefix
    else:
        return longest_prefix