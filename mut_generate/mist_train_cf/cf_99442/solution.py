"""
QUESTION:
Write a function named `remove_common_characters` that takes two strings as input and returns two new strings with all common characters removed. The function should return two new strings with all common characters between the input strings removed. The function should not modify the original strings.
"""

def remove_common_characters(s, t):
    common = set()
    for i in range(len(s)):
        if s[i] in t:
            common.add(s[i])
    for c in common:
        s = s.replace(c, '')
        t = t.replace(c, '')
    return s, t