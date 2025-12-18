"""
QUESTION:
Write a function named `longest_common_prefix` that takes a list of strings as input and returns the longest common prefix among all the strings in the list. The function should achieve a time complexity of O(n*m), where n is the number of strings in the list and m is the length of the longest string.
"""

def longest_common_prefix(strs):
    if len(strs) == 0:
        return ""

    min_length = min(len(s) for s in strs)

    def all_chars_same(index):
        char = strs[0][index]
        return all(s[index] == char for s in strs)

    left = 0
    right = min_length - 1

    while left <= right:
        mid = (left + right) // 2
        if all_chars_same(mid):
            left = mid + 1
        else:
            right = mid - 1

    return strs[0][:left]