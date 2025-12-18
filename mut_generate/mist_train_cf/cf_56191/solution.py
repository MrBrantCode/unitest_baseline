"""
QUESTION:
Write a function named `product_prime` that accepts a list of integers and two optional integer parameters `start` and `end`, which represent the starting and ending indices of the sublist to consider. If `start` and `end` are not provided, the function should consider the entire list. The function should return a Boolean indicating whether the product of the integers in the specified sublist is a prime number. The function should handle negative integers and zero in the list correctly. Note that the function uses 0-based indexing.
"""

def product_prime(numbers, start=None, end=None):
    """Check if product of numbers between start and end indexes is prime"""
    
    def is_prime(n):
        """Check if a number is prime"""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    if start is None and end is None:
        product = 1
        for number in numbers:
            product *= number
    else:
        product = 1
        for number in numbers[start:end+1]:
            product *= number
    return is_prime(product)