"""
QUESTION:
Implement a function `compare_strings` that takes two strings as input, sorts the characters within each string using a sorting algorithm of your choice, and returns an integer value representing their alphabetical order based on their ASCII values. The function should return -1 if the first string is alphabetically before the second string, 1 if the first string is alphabetically after the second string, and 0 if the strings are equal. You are not allowed to use any built-in string comparison functions or methods. You may assume that the input strings contain only lowercase letters and are not empty.
"""

def compare_strings(string1, string2):
    # Sort both input strings
    sorted_string1 = ''.join(sorted(string1))
    sorted_string2 = ''.join(sorted(string2))

    # Compare the sorted strings character by character
    for i in range(min(len(sorted_string1), len(sorted_string2))):
        if sorted_string1[i] < sorted_string2[i]:
            return -1
        elif sorted_string1[i] > sorted_string2[i]:
            return 1

    # If all characters are the same, return 0 if the lengths are equal
    if len(sorted_string1) == len(sorted_string2):
        return 0
    # If string1 is shorter, return -1
    elif len(sorted_string1) < len(sorted_string2):
        return -1
    # If string1 is longer, return 1
    else:
        return 1