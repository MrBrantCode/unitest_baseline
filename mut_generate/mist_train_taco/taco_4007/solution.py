"""
QUESTION:
Given a string s, return the last substring of s in lexicographical order.
 
Example 1:
Input: "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".

Example 2:
Input: "leetcode"
Output: "tcode"

 
Note:

1 <= s.length <= 4 * 10^5
s contains only lowercase English letters.
"""

def find_last_substring(s: str) -> str:
    index = {c: i for (i, c) in enumerate(sorted(set(s)))}
    (cur, radix, max_val, max_i) = (0, len(index), 0, 0)
    for i in range(len(s) - 1, -1, -1):
        cur = index[s[i]] + cur / radix
        if cur > max_val:
            (max_val, max_i) = (cur, i)
    return s[max_i:]