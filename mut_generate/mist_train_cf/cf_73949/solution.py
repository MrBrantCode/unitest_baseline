"""
QUESTION:
Create a function `can_transform` that takes two strings `s` and `t`, and an integer `k`, and returns a boolean value. The function should determine if string `s` can be transformed into string `t` in `k` steps or fewer, where a step involves shifting a character in `s` to the next letter in the alphabet (looping from 'z' to 'a'). Each index in `s` can only be selected once. The lengths of `s` and `t` are between 1 and 10^5, and `k` is between 0 and 10^9. The strings `s` and `t` consist solely of lowercase English alphabets.
"""

def can_transform(s, t, k):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        diff = ord(t[i]) - ord(s[i])
        if diff < 0: 
            diff += 26
        k -= diff
        if k < 0: 
            return False
    return True