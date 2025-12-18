"""
QUESTION:
Write a function `penultimate_palindrome` that takes a string `s` as input and returns the second last longest palindromic subsequence within `s`. A palindromic subsequence is a subsequence that reads the same backward as forward. The function should return `None` if there is less than two palindromic subsequences in `s`.
"""

def is_palindrome(s):
    return s == s[::-1]

def penultimate_palindrome(s):
    length = len(s)
    penult = None
    second_last = None
    
    for len_sub in reversed(range(2, length + 1)):
        if second_last:
            break
        for start in range(0, length - len_sub + 1):
            substr = s[start : start + len_sub]
            if is_palindrome(substr):
                if not penult:
                    penult = substr
                elif  substr != penult: 
                    second_last = substr
                    break
    return second_last