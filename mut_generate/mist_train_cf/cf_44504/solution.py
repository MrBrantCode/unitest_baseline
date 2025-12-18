"""
QUESTION:
Write a function `solve(str1, str2)` to find the longest common substring between two given strings `str1` and `str2`. The function should be able to handle strings with up to 10^6 characters and should have a time complexity of O(n log n) or better. The substring can contain alphanumeric and special characters, and the comparison should be case-sensitive.
"""

def entrance(str1, str2):
    min_len = min(len(str1), len(str2)) + 1
    low, high = 0, min_len
    result = ''

    while low < high:
        mid = (low + high) // 2
        substrs = create_map(str1, mid).intersection(create_map(str2, mid))
        if substrs:
            result = substrs.pop()
            low = mid + 1
        else:
            high = mid

    return result

def create_map(s, n):
    add = set()
    for i in range(len(s) - n + 1):
        add.add(s[i: i+n])

    return add