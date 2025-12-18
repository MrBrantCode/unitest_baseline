"""
QUESTION:
Given the strings s1 and s2 of size n, and the string evil. Return the number of good strings.
A good string has size n, it is alphabetically greater than or equal to s1, it is alphabetically smaller than or equal to s2, and it does not contain the string evil as a substring. Since the answer can be a huge number, return this modulo 10^9 + 7.
 
Example 1:
Input: n = 2, s1 = "aa", s2 = "da", evil = "b"
Output: 51 
Explanation: There are 25 good strings starting with 'a': "aa","ac","ad",...,"az". Then there are 25 good strings starting with 'c': "ca","cc","cd",...,"cz" and finally there is one good string starting with 'd': "da". 

Example 2:
Input: n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"
Output: 0 
Explanation: All strings greater than or equal to s1 and smaller than or equal to s2 start with the prefix "leet", therefore, there is not any good string.

Example 3:
Input: n = 2, s1 = "gx", s2 = "gz", evil = "x"
Output: 2

 
Constraints:

s1.length == n
s2.length == n
s1 <= s2
1 <= n <= 500
1 <= evil.length <= 50
All strings consist of lowercase English letters.
"""

from functools import lru_cache

def failure(pat):
    (i, target, n) = (1, 0, len(pat))
    res = [0]
    while i < n:
        if pat[i] == pat[target]:
            target += 1
            res.append(target)
            i += 1
        elif target:
            target = res[target - 1]
        else:
            res.append(0)
            i += 1
    return res

def count_good_strings(n: int, s1: str, s2: str, evil: str) -> int:
    f = failure(evil)

    @lru_cache(None)
    def dfs(idx, max_matched=0, lb=True, rb=True):
        if max_matched == len(evil):
            return 0
        if idx == n:
            return 1
        l = s1[idx] if lb else 'a'
        r = s2[idx] if rb else 'z'
        candidates = [chr(i) for i in range(ord(l), ord(r) + 1)]
        res = 0
        for (i, c) in enumerate(candidates):
            next_matched = max_matched
            while next_matched and evil[next_matched] != c:
                next_matched = f[next_matched - 1]
            res += dfs(idx + 1, next_matched + (evil[next_matched] == c), lb and i == 0, rb and i == len(candidates) - 1)
        return res
    
    return dfs(0) % (10 ** 9 + 7)