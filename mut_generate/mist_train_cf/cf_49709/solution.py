"""
QUESTION:
Create a function named `is_happy` that takes a string `s` and two integers `n` and `m` as input. The function should return `True` if the string `s` meets the following conditions:
- The length of `s` is at least `n+m` (where 1 <= n <= len(s) and m <= len(s)).
- Every `n` consecutive letters in `s` are distinct.
- Each distinct letter in `s` appears at least `m` times in total.
- The first `m` characters of `s` are unique.
Otherwise, the function should return `False`.
"""

def is_happy(s, n, m):
    from collections import Counter
    
    # length of string should be at least n+m
    if len(s) < n+m:
        return False

    # check if every n consecutive letters are distinct
    for i in range(0, len(s), n):
        if len(set(s[i:i+n])) != n:
            return False

    # check if each distinct letter appears at least m times in total
    letter_counts = Counter(s)
    if any(count < m for count in letter_counts.values()):
        return False

    # check if the first m characters of the string are unique
    if len(set(s[:m])) != m:
        return False

    return True