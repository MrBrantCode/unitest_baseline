"""
QUESTION:
Create a function `factorial_tuple` that takes a tuple of integers as input, calculates the factorial of each integer, and returns a tuple containing the factorials. The function should also return the sum of the input tuple and the sum of the factorial tuple. The input integers are between 1 and 10. The function should not use the math.factorial function.
"""

def factorial_tuple(nums):
    """
    This function calculates the factorial of each integer in a tuple, 
    returns a tuple containing the factorials, and the sum of the input tuple 
    and the sum of the factorial tuple.

    Args:
        nums (tuple): A tuple of integers between 1 and 10.

    Returns:
        tuple: A tuple containing the factorials and the sums.
    """
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n-1)

    factorial_nums = tuple(factorial(num) for num in nums)
    original_sum = sum(nums)
    factorial_sum = sum(factorial_nums)
    
    return factorial_nums, original_sum, factorial_sum