"""
QUESTION:
Create a function `will_it_fly(q, w, n)` that evaluates if an array `q` of integers can "fly" based on the following conditions: 
- The array `q` must be a palindrome. 
- The sum of its elements must be less than or equal to the maximum allowed sum `w`. 
- The array must contain exactly `n` unique digits.
"""

def will_it_fly(q, w, n):
    is_palindrome = q == q[::-1]  # True if 'q' is a palindrome.
    sum_condition = sum(q) <= w  # True if sum of 'q' is <= 'w'.
    n_unique_vals = len(set(q)) == n  # True if 'q' contains exactly 'n' unique values.
    return is_palindrome and sum_condition and n_unique_vals