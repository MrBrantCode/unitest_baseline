"""
QUESTION:
You are given a string s containing lowercase letters and an integer k. You need to :

First, change some characters of s to other lowercase English letters.
Then divide s into k non-empty disjoint substrings such that each substring is palindrome.

Return the minimal number of characters that you need to change to divide the string.
 
Example 1:
Input: s = "abc", k = 2
Output: 1
Explanation: You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.

Example 2:
Input: s = "aabbc", k = 3
Output: 0
Explanation: You can split the string into "aa", "bb" and "c", all of them are palindrome.
Example 3:
Input: s = "leetcode", k = 8
Output: 0

 
Constraints:

1 <= k <= s.length <= 100.
s only contains lowercase English letters.
"""

from functools import lru_cache

def min_changes_to_palindrome_partitions(s: str, k: int) -> int:
    n = len(s)
    if n == k:
        return 0

    @lru_cache(None)
    def cnt(left, right):
        if left >= right:
            return 0
        return cnt(left + 1, right - 1) + (s[left] != s[right])

    @lru_cache(None)
    def dp(length, partition):
        if partition == length:
            return 0
        if partition == 1:
            return cnt(0, length - 1)
        return min((dp(prelength, partition - 1) + cnt(prelength, length - 1) for prelength in range(partition - 1, length)))
    
    return dp(n, k)