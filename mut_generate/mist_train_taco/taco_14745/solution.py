"""
QUESTION:
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:


Input: s = "anagram", t = "nagaram"
Output: true


Example 2:


Input: s = "rat", t = "car"
Output: false


Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    if s == t:
        return True
    for char in map(chr, range(97, 123)):
        if s.count(char) != t.count(char):
            return False
    return True