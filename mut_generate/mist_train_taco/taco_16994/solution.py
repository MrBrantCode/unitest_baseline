"""
QUESTION:
Given a string, your task is to count how many palindromic substrings in this string.



The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters. 


Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".



Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".



Note:

The input string length won't exceed 1000.
"""

def count_palindromic_substrings(s: str) -> int:
    def sum_n(n: int) -> int:
        return sum(range(1, n + 1))
    
    ret = 0
    left, right = 0, 0
    
    while left < len(s):
        while right < len(s) and s[right] == s[left]:
            right += 1
        ret += sum_n(right - left)
        l, r = left - 1, right
        while l >= 0 and r < len(s) and s[r] == s[l]:
            ret += 1
            l -= 1
            r += 1
        left = right
    
    return ret