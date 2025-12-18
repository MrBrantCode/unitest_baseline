"""
QUESTION:
Given a string S, count the number of distinct, non-empty subsequences of S .
Since the result may be large, return the answer modulo 10^9 + 7.
 
Example 1:
Input: "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".


Example 2:
Input: "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and "aba".


Example 3:
Input: "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".



 
 
Note:

S contains only lowercase letters.
1 <= S.length <= 2000
"""

def count_distinct_subsequences(s: str) -> int:
    MOD = 10**9 + 7
    seen = {}
    a = 1
    
    for char in s:
        b = 2 * a
        if char in seen:
            b -= seen[char]
        b %= MOD
        seen[char] = a
        a = b
    
    return a - 1