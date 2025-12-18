"""
QUESTION:
Find all starting indices of the substring needle in the string haystack, considering both case sensitivity and partial matches, and return the indices as a list in ascending order. The function should be named `find_needle_indices` and take two parameters, `haystack` and `needle`. The function should not use any built-in functions or libraries that directly solve this problem, or regular expressions or string matching algorithms, and should have a time complexity of O(n), where n is the length of the haystack string.
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