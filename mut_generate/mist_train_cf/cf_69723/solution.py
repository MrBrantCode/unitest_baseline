"""
QUESTION:
Write a function `is_happy(s)` that takes a string `s` as input and returns `True` if it is "happy" and `False` otherwise. A string is considered "happy" if it meets the following conditions:

- It has at least 3 characters.
- It does not contain consecutive repeating letters.
- All letters have even frequency.
- Exactly three letters repeat twice each.
- All letters are distinct.

The function should only use a single loop to iterate over the string, and it should use a dictionary to store the frequency of letters and a set to store distinct letters.
"""

def is_happy(s):
    if len(s) < 3:
        return False

    freq = {}
    repeat = 0
    distinct = set()

    for i in range(len(s)):
        if i > 0 and s[i] == s[i-1]:
            return False
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
        distinct.add(s[i])

    for k, v in freq.items():
        if v % 2 != 0:
            return False
        if v == 2:
            repeat += 1

    if repeat < 3 or len(distinct) != len(freq):
        return False

    return True