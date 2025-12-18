"""
QUESTION:
Construct a function named `common_substring` that accepts an array of strings and an integer `num`, and returns the smallest alphabetic substring that is common among at least `num` strings in the array. The function should be case-insensitive and consider all possible substrings of each string in the array. If no such substring exists, the function should return an empty string.
"""

from collections import Counter

def common_substring(arr, num):
    def all_substrings(string):
        length = len(string)
        return [string[i: j] for i in range(length) for j in range(i + 1, length + 1)]

    subs = []
    for string in arr:
        subs.extend(all_substrings(string.lower()))  
    subs_counter = Counter(subs)
    common_subs = [k for k, v in subs_counter.items() if v >= num] 
    if len(common_subs) == 0: return ""
    return min(common_subs, key=len)