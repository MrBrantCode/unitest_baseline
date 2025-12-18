"""
QUESTION:
Write a function `rearrange_array` that takes an array of integers as input, finds all prime numbers in the array, calculates their sum, and rearranges the array in descending order of the element's difference with the sum of prime numbers. The function should return the rearranged array.

The input array is not empty and contains only integers. The function should be implemented in Python.
"""

def rearrange_array(arr):
    """
    This function takes an array of integers as input, finds all prime numbers in the array, 
    calculates their sum, and rearranges the array in descending order of the element's 
    difference with the sum of prime numbers.

    Parameters:
    arr (list): A list of integers.

    Returns:
    list: The rearranged array.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    primes = [x for x in arr if is_prime(x)]
    total = sum(primes)
    diff = [(x, abs(x - total)) for x in arr]
    return [x[0] for x in sorted(diff, key=lambda x: x[1], reverse=True)]