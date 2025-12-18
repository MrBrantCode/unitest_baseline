"""
QUESTION:
Implement the function `is_happy(s, n)` that determines if the given string `s` is 'happy' based on the following conditions: 
- the length of `s` is at least `n + 2`
- every group of `n` consecutive letters are distinct
- every unique letter appears at least twice
- the first character cannot be the same as the last character in the string `s`. 
The function should accept a string `s` and an integer `n` as parameters, where `1 <= n <= the length of s`, and return `True` if the string is 'happy', otherwise return `False`.
"""

def is_happy(s, n):
    # Check first condition: length of s is at least n + 2
    if len(s) < n + 2:
        return False

    # Check second condition: every n character is unique, using a sliding window approach
    for i in range(len(s) - n + 1):
        if len(set(s[i:i+n])) != n:
            return False

    # Check third condition: every character appears at least twice, using a frequency counter
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    if min(frequency.values()) < 2:
        return False

    # Check fourth new condition: The first character cannot be the same as the last character
    if s[0] == s[-1]:
        return False
    
    return True