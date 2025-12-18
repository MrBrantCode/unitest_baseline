"""
QUESTION:
Design a function named 'will_it_fly' that takes an array 'q' and a maximum permissible mass 'w' as input. The function should return True if 'q' is a palindrome and the sum of its elements does not exceed 'w', and False otherwise. The function should handle arrays of any length.
"""

def will_it_fly(q, w):
    return q == q[::-1] and sum(q) <= w