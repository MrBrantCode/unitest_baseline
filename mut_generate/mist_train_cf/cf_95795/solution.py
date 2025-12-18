"""
QUESTION:
Write a function `find_nth_prime` to find the nth prime number greater than a given number. The function should take two parameters: `n` (the position of the prime number to find) and `start` (the number from which to start the search). The function should return the nth prime number greater than `start`.
"""

def find_nth_prime(n, start):
    """
    Find the nth prime number greater than a given number.
    
    Args:
        n (int): The position of the prime number to find.
        start (int): The number from which to start the search.
    
    Returns:
        int: The nth prime number greater than start.
    """

    def is_prime(num):
        """
        Check if a number is prime.
        
        Args:
            num (int): The number to check.
        
        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    num = start + 1  # Start checking from the first number greater than start
    
    while count < n:
        if is_prime(num):
            count += 1
        num += 1
    
    return num - 1