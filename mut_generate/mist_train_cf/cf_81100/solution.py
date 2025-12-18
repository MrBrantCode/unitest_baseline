"""
QUESTION:
Create a function called `willItFly` that takes two parameters: an array `q` and a number `w`. The function should return `True` if the array `q` is a palindrome (i.e., reads the same backward as forward) and the sum of its elements is less than or equal to `w`.
"""

def willItFly(q, w):
    # Check if array is palindrome
    is_palindrome = q == q[::-1]
    
    # Calculate sum of all elements in array q
    total_sum = sum(q)

    # Return true if sum is less or equal to w and array is palindromic
    return is_palindrome and total_sum <= w