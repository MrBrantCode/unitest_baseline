"""
QUESTION:
Given two strings `haystack` and `needle`, write a function `find_needle_indices(haystack, needle)` that finds the starting index of all occurrences of the `needle` within the `haystack`, considering both case sensitivity and partial matches. The function should return the indices as a list in ascending order.

The function must have a time complexity of O(n), where n is the length of the `haystack` string. It cannot use any built-in functions or libraries that directly solve this problem, regular expressions, or string matching algorithms. The lengths of `haystack` and `needle` will not exceed 10^5, and both strings will only contain alphabetic characters and spaces.
"""

def find_needle_indices(haystack, needle):
    indices = []
    haystack = haystack.lower()
    needle = needle.lower()

    needle_len = len(needle)
    haystack_len = len(haystack)

    for i in range(haystack_len - needle_len + 1):
        if haystack[i:i+needle_len] == needle:
            indices.append(i)

    return indices