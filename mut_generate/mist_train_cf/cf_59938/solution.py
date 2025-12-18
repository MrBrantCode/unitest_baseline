"""
QUESTION:
Create a function named `square_root` that takes a single numerical argument `n` and returns its square root. The function should employ a binary search approach to find the square root. It should also handle potential edge cases such as negative numbers and fractions, and it should return accurate results for both integers and fractions. The function should not return -1 when the value does not meet the conditions; instead, it should follow standard conventions for finding square roots.
"""

def square_root(n):
    if n<0:
        return None
    if n == 1 or n == 0:
        return n
    
    accuracy = 0.00001
    start = 0
    end = n
    if n < 1: # If the number is a fraction
        end = 1
    
    while end - start > accuracy:
        mid = (start + end) / 2
        if mid * mid < n:
            start = mid
        else:
            end = mid
            
    return (start + end) / 2