"""
QUESTION:
Write a function `longestSubstring(s: str, k: int) -> int` that returns the length of the longest substring with exactly k distinct characters. If there are multiple substrings with the same maximum length, return the length of the substring that appears first in the original string. The function takes two parameters: `s`, a string, and `k`, an integer representing the number of distinct characters.
"""

def longestSubstring(s: str, k: int) -> int:
    count = {}
    start = 0
    max_length = 0
    
    for end in range(len(s)):
        count[s[end]] = count.get(s[end], 0) + 1
        
        while len(count) > k:
            count[s[start]] -= 1
            if count[s[start]] == 0:
                del count[s[start]]
            start += 1
        
        max_length = max(max_length, end - start + 1)
    
    return max_length