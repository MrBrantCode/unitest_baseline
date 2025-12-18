"""
QUESTION:
Write a function `is_happy(s, n)` where `s` is a string and `n` is an integer (1 <= n <= len(s)). The function should return `True` if the string `s` meets the following conditions: 
1. The string length is at least `n+2`.
2. Every `n` consecutive letters are distinct.
3. Each distinct letter emerges at least twice.
4. The string contains at least one vowel ('a', 'e', 'i', 'o', 'u'). 
Otherwise, the function should return `False`.
"""

def is_happy(s, n):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    if not any(char in vowels for char in s):
        return False
    seen = {}
    for i in range(len(s) - n + 1):
        substring = s[i : i + n]
        if len(set(substring)) != len(substring):
            return False
        for char in substring:
            seen[char] = seen.get(char, 0) + 1
    if all(count >= 2 for count in seen.values()) and len(s) >= n+2:
        return True
    return False