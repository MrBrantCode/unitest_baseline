"""
QUESTION:
A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).
Given a string s. Return the longest happy prefix of s .
Return an empty string if no such prefix exists.
 
Example 1:
Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".

Example 2:
Input: s = "ababab"
Output: "abab"
Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.

Example 3:
Input: s = "leetcodeleet"
Output: "leet"

Example 4:
Input: s = "a"
Output: ""

 
Constraints:

1 <= s.length <= 10^5
s contains only lowercase English letters.
"""

def longest_happy_prefix(s: str) -> str:
    max_prefs = [0] * len(s)
    curr = 0
    for idx in range(1, len(s)):
        while True:
            if curr == 0:
                if s[idx] == s[0]:
                    curr = 1
                max_prefs[idx] = curr
                break
            elif s[idx] == s[curr]:
                curr += 1
                max_prefs[idx] = curr
                break
            else:
                curr = max_prefs[curr - 1]
    return s[:max_prefs[-1]]