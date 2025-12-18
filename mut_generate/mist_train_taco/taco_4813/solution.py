"""
QUESTION:
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  If multiple answers exist, you may return any of them.
(A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)
 
Example 1:
Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

 
Note:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
"""

def shortest_common_supersequence(str1: str, str2: str) -> str:
    def dp(s1, s2, i, j, mem):
        if (i, j) in mem:
            return mem[i, j]
        elif i >= len(s1) and j >= len(s2):
            res = ''
        elif i >= len(s1):
            res = s2[j:]
        elif j >= len(s2):
            res = s1[i:]
        elif s1[i] == s2[j]:
            res = s1[i] + dp(s1, s2, i + 1, j + 1, mem)
        else:
            left = s1[i] + dp(s1, s2, i + 1, j, mem)
            right = s2[j] + dp(s1, s2, i, j + 1, mem)
            if len(left) < len(right):
                res = left
            else:
                res = right
        mem[i, j] = res
        return res

    return dp(str1, str2, 0, 0, {})