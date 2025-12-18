"""
QUESTION:
Write a function `length_of_longest_substring(s, k)` that takes a string `s` and an integer `k` as input and returns the length of the longest substring that contains at most `k` distinct characters.

The function should handle strings of length up to 10^5 and `k` values ranging from 1 to 26. The string consists of English letters.
"""

def length_of_longest_substring(s, k):
    n = len(s) 
    if k == 0 or n == 0:
        return 0
  
    left, right = 0, 0
    hashmap = dict()
    max_length = 1
    while right < n:
        hashmap[s[right]] = right
        right += 1
        if len(hashmap) == k + 1:
            del_idx = min(hashmap.values())
            del hashmap[s[del_idx]]
            left = del_idx + 1
        max_length = max(max_length, right - left)
  
    return max_length