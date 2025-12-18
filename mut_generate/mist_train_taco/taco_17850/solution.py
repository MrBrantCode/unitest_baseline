"""
QUESTION:
Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:

Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.



Example 2:

Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.



Example 3:

Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.
"""

def count_unique_substrings_in_wraparound_string(p: str) -> int:
    pc = None
    sl = 0
    ll = {}
    
    for c in p:
        if pc and (ord(pc) + 1 == ord(c) or (pc == 'z' and c == 'a')):
            sl += 1
        else:
            sl = 1
        ll[c] = max(ll[c], sl) if c in ll else sl
        pc = c
    
    s = 0
    for value in ll.values():
        s += value
    
    return s