"""
QUESTION:
Write a function `segregate_numbers` that takes a list of integers as input and returns the list with its elements rearranged into three sections: prime numbers, perfect squares, and all other numbers. The prime numbers should come first, followed by the perfect squares, and then the remaining numbers. The order of the numbers within each section must be maintained.
"""

def segregate_numbers(nums):
    """
    Segregate the input list of integers into three sections: prime numbers, perfect squares, and other numbers.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        list: The input list with its elements rearranged into prime numbers, perfect squares, and other numbers.
    """
    
    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqrt_n = int(n**0.5) + 1
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                return False
        return True
    
    def is_perfect_square(n):
        """Check if a number is a perfect square."""
        return n >= 0 and n**0.5 == int(n**0.5)
    
    primes = [num for num in nums if is_prime(num)]
    perfect_squares = [num for num in nums if is_perfect_square(num) and not is_prime(num)]
    others = [num for num in nums if not is_prime(num) and not is_perfect_square(num)]
    
    return primes + perfect_squares + others