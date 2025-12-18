"""
QUESTION:
Write a function `superior_parallel_dividend(x, y, z)` that takes in three positive integers x, y, and z. The function should return the largest even integer in the range [x, y] that is divisible by z. If no such integer exists, the function should return -1.
"""

def superior_parallel_dividend(x, y, z):
    """Returns the largest even integer in the range [x, y] that is divisible by z or -1 if no such integer exists"""
    
    highest_even = y if y % 2 == 0 else y - 1
    
    for i in range(highest_even, x - 1, -2):
        if i % z == 0:
            return i
            
    return -1