"""
QUESTION:
Create a function `can_form_palindrome(s, k)` that takes a string `s` and an integer `k` as inputs. Return `True` if it is possible to create a palindrome by changing at most `k` characters in the string, otherwise return `False`. Implement the function without using any built-in reverse functions or additional data structures other than the input string.
"""

def can_form_palindrome(s, k):
    changes_needed = sum(s[i] != s[~i] for i in range(len(s) // 2))
    return changes_needed <= k