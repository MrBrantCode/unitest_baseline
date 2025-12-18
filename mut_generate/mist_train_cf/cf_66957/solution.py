"""
QUESTION:
Create a function `find_trailing_zeros(n)` that calculates the number of trailing zeros in the factorial of a given non-negative integer `n`. The function should return an error message if `n` is not a non-negative integer.
"""

def find_trailing_zeros(n: int) -> int:
    # Check if n is a non-negative integer
    if not isinstance(n,int) or n<0:
        return 'Input should be a non-negative integer'
    
    count = 0
    
    # Keep dividing n by powers of
    # 5 and update Count
    i = 5
    while n // i >= 1:
        count += n // i
        i *= 5
        
    return count