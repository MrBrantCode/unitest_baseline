"""
QUESTION:
Write a function `nth_term` that calculates the nth term of an arithmetic sequence given the first term and the common difference. The function should take three parameters: `first_term`, `common_difference`, and `n`, where `n` is the term number. Use this function to find the seventh and eighth terms of an arithmetic sequence that starts at 1 and has a common difference of 4.
"""

def nth_term(first_term, common_difference, n):
    return first_term + (n - 1) * common_difference