"""
QUESTION:
Write a function named `longest_common_prefix` that takes a list of strings and returns the longest common prefix of the list of strings. The function should have a time complexity of O(n*m), where n is the number of strings in the list and m is the length of the longest string. The function must not use any built-in string matching functions, explicit loops, or recursion.
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