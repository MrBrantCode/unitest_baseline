"""
QUESTION:
Write a function named find_second_largest_prime that takes an array of integers as input and returns the second largest prime number in the array. The array will contain at least two elements and may contain duplicates, with elements being positive, negative, or zero.
"""

def find_second_largest_prime(arr):
    """
    This function finds the second largest prime number in a given array.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    int: The second largest prime number in the array.
    """
    
    def is_prime(n):
        """
        Checks if a number is prime.
        
        Parameters:
        n (int): The number to check.
        
        Returns:
        bool: True if the number is prime, False otherwise.
        """
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

    largest_prime = float('-inf')
    second_largest_prime = float('-inf')
    for num in arr:
        if is_prime(abs(num)):
            if num > largest_prime:
                second_largest_prime = largest_prime
                largest_prime = num
            elif num > second_largest_prime and num != largest_prime:
                second_largest_prime = num
    return second_largest_prime