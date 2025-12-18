"""
QUESTION:
Write a function `findMostCommonString(strings)` that finds the most common string in the given array of strings. The function should have a time complexity of O(n), where n is the length of the input array, and should be able to handle arrays with up to 10^6 elements and string lengths of up to 100 characters.
"""

def findMostCommonString(strings):
    counts = {}
    max_count = 0
    most_common = ""

    for string in strings:
        if string in counts:
            counts[string] += 1
        else:
            counts[string] = 1

        if counts[string] > max_count:
            max_count = counts[string]
            most_common = string

    return most_common