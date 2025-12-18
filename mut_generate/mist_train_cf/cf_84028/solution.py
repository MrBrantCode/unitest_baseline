"""
QUESTION:
Create a function named `is_anagram_of_palindrome(s)` that determines whether a given string `s` is an anagram of a palindrome. The function should consider both lowercase and uppercase alphabets, and ignore digits and special characters.
"""

def is_anagram_of_palindrome(s):
    count = dict()
    s = s.lower()
    s = ''.join(c for c in s if c.isalpha())

    for i in s:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    odd = 0
    for key, value in count.items():
        if value % 2 != 0:
            odd += 1
            if odd > 1:
                return False
    return True