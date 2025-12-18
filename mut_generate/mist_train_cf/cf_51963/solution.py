"""
QUESTION:
Design a function called `longest_common_substring` that takes an array of strings as input and returns the longest consecutive alphabetic substring common to all strings in the array, assuming the strings are case sensitive and 'consecutive' means the characters appear in the same order in the original strings. The function should not consider alphabetic order or continuity in the alphabetic sense. The length of the longest common substring cannot exceed the length of the shortest string in the array.
"""

def longest_common_substring(arr):
    shortest_string = min(arr, key=len)
    length = len(shortest_string)
    for i in range(length, 0, -1):
        for j in range(length - i + 1):
            candidate = shortest_string[j: j+i]
            if all(candidate in string for string in arr):
                return candidate
    return ''