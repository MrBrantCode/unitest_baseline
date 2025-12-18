"""
QUESTION:
Write a function `f(x)` that calculates the `x`th number in the Fibonacci sequence, where each number is the sum of the two preceding ones, with a time complexity of O(n) and a space complexity of O(1).
"""

def f(x):
    if x == 0 or x == 1:
        return 1
    
    prev_1 = 1  # value of f(x-1)
    prev_2 = 1  # value of f(x-2)
    
    for i in range(2, x+1):
        current = prev_1 + prev_2
        prev_1, prev_2 = current, prev_1
    
    return current