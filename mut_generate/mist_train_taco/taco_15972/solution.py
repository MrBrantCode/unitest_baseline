"""
QUESTION:
Let's define a function countUniqueChars(s) that returns the number of unique characters on s, for example if s = "LEETCODE" then "L", "T","C","O","D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.

On this problem given a string s we need to return the sum of countUniqueChars(t) where t is a substring of s. Notice that some substrings can be repeated so on this case you have to count the repeated ones too.
Since the answer can be very large, return the answer modulo 10 ^ 9 + 7.
 
Example 1:
Input: s = "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Evey substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

Example 2:
Input: s = "ABA"
Output: 8
Explanation: The same as example 1, except countUniqueChars("ABA") = 1.

Example 3:
Input: s = "LEETCODE"
Output: 92

 
Constraints:

0 <= s.length <= 10^4
s contain upper-case English letters only.
"""

from collections import defaultdict

def calculate_unique_chars_sum(s: str) -> int:
    chrLoc = defaultdict(list)
    ct = 0
    md = 1000000007
    l = len(s)
    
    # Record the positions of each character in the string
    for i, c in enumerate(s):
        chrLoc[c].append(i)
    
    # Calculate the sum of unique characters in all substrings
    for c in chrLoc:
        locs = [-1] + chrLoc[c] + [l]
        loc_ct = len(locs)
        for i in range(1, loc_ct - 1):
            leftWingSpan = locs[i] - locs[i - 1]
            rightWingSpan = locs[i + 1] - locs[i]
            ct += leftWingSpan % md * (rightWingSpan % md) % md
            ct %= md
    
    return ct