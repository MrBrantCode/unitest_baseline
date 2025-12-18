"""
QUESTION:
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.


Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.



Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""

def longest_substring_with_k_repeats(s: str, k: int) -> int:
    for c in set(s):
        if s.count(c) < k:
            return max((longest_substring_with_k_repeats(sp, k) for sp in s.split(c)))
    return len(s)