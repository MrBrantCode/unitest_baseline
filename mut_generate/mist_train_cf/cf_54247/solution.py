"""
QUESTION:
Write a function named `five_nine_twelve` that takes an integer `n` as input and returns the count of integers less than `n` that contain the digit 5 and are divisible by either 9 or 12. The function should handle both positive and negative values of `n`.
"""

def five_nine_twelve(n: int):
    """
    Return the count of integers less than n, which contain the digit 5. 
    The returned count should include numbers that are:
    - divisible by either 9 or 12.
    - handle cases where n is negative. 
    """ 
    count = 0
    if n > 0:
        for i in range(1,n):
            if '5' in str(i) and (i % 12 == 0 or i % 9 == 0):
                count += 1
    else:
        for i in range(n+1,0):
            if '5' in str(i) and (i % 12 == 0 or i % 9 == 0):
                count += 1 
    return count