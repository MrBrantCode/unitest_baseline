"""
QUESTION:
Write a function `longest_common_prefix(strings)` that finds the longest common prefix string from an array of strings. The function should have a time complexity of O(n*m), where n is the length of the input array and m is the maximum length of the strings. The function should not use any built-in functions or libraries for string manipulation, sorting, or comparison. The longest common prefix string should be at least 1 character long, but there is no minimum length restriction.
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

    return longest_prefix