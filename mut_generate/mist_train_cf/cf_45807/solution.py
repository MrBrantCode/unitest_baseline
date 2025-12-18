"""
QUESTION:
Implement a function named `five_nine_twelve(n: int)` that returns the count of whole numbers less than `n` that are divisible by either 9 or 12 and contain the digit 5. The function should handle cases where `n` is negative, in which case it should return 0.
"""

def five_nine_twelve(n: int) -> int:
    """
    Returns the count of whole numbers less than `n` that are divisible by either 9 or 12 and contain the digit 5.
    
    If `n` is negative, the function returns 0.
    
    Parameters:
    n (int): The upper limit for the numbers to check.
    
    Returns:
    int: The count of numbers that meet the specified conditions.
    """
    if n < 0: 
        return 0

    count = 0
    for i in range(5, n):
        if (i % 12 == 0 or i % 9 == 0) and '5' in str(i):
            count += 1
    return count