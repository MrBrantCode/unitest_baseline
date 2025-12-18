"""
QUESTION:
Given string s, the task is to find the count of all substrings which have the same character at the beginning and end.
Example 1:
Input: s = "abcab"
Output: 7
Explanation: a, abca, b, bcab, 
c, a and b
Example 2:
Input: s = "aba"
Output: 4
Explanation: a, b, a and aba
User Task:
Your task is to complete the function countSubstringWithEqualEnds() which takes a single string as input and returns the count. You do not need to take any input or print anything.
Expected Time Complexity: O(|str|)
Expected Auxiliary Space: O(constant)
Constraints:
1 <= |s| <= 10^{4}
s contains lower case english alphabets
"""

def count_substrings_with_equal_ends(s: str) -> int:
    d = {}
    c = 0
    for char in s:
        if char not in d:
            d[char] = 0
        d[char] += 1
        c += d[char]
    return c