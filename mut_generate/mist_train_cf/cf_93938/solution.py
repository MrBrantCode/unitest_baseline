"""
QUESTION:
Implement a recursive function named `recursive_function` that takes a positive integer `n` as input. The function should call itself with decreasing values of `n` until it reaches a base case where `n` equals 0, at which point the recursion stops. Analyze the function to determine its time complexity.
"""

def recursive_function(n):
    if n == 0:
        return
    else:
        recursive_function(n-1)