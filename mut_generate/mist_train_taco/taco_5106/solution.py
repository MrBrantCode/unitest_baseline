"""
QUESTION:
Given a string s, return the maximum number of unique substrings that the given string can be split into.
You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.
A substring is a contiguous sequence of characters within a string.
 
Example 1:
Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.

Example 2:
Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].

Example 3:
Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.

 
Constraints:


1 <= s.length <= 16


s contains only lower case English letters.
"""

def max_unique_split(s: str) -> int:
    n = len(s)
    max_count = 0

    def backtrack(start=0, substrings=set()):
        nonlocal max_count
        if start == n:
            max_count = max(max_count, len(substrings))
            return
        
        for end in range(start + 1, n + 1):
            substring = s[start:end]
            if substring not in substrings:
                substrings.add(substring)
                backtrack(end, substrings)
                substrings.remove(substring)

    backtrack()
    return max_count