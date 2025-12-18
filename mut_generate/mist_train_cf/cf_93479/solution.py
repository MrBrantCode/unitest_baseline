"""
QUESTION:
Implement a function `factorial(n)` that takes an integer `n` as input and returns the factorial of `n`. The function should handle cases where `n` is negative (return `None`) and where `n` is 0 (return 1). The time complexity of the function should be O(n).
"""

def entance(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n+1):
        result *= i
    
    return result