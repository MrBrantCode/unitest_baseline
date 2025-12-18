"""
QUESTION:
Implement a function named "compare_strings" that takes two strings as arguments and returns true if the strings are equal and false otherwise. The function should compare the strings character by character without using any built-in string comparison functions or operators. The time complexity of the algorithm should be O(n), where n is the length of the longest string.
"""

def compare_strings(string1, string2):
    if len(string1) != len(string2):
        return False
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            return False
    return True