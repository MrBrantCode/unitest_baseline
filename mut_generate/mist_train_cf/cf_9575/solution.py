"""
QUESTION:
Find the median of three distinct positive integers between 1 and 1000 where one of the integers must be divisible by 5. The function should take three integers as input and return the median. Assume that the input integers are distinct and one of them is divisible by 5.
"""

def find_median(a, b, c):
    """
    This function calculates the median of three distinct integers.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    c (int): The third integer.
    
    Returns:
    int: The median of the three integers.
    """
    numbers = [a, b, c]
    numbers.sort()
    return numbers[1]