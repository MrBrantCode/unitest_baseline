"""
QUESTION:
Implement a function named 'gcd_array' that calculates the Greatest Common Divisor (GCD) of a series of integers contained within an array. The function should receive an array of integers and efficiently determine their GCD using an optimized algorithm. The input array has a length between 1 and 10^3, and each integer in the array is between 1 and 10^6.
"""

from typing import List

def gcd_array(nums: List[int]) -> int:
    """
    Finds the GCD of a list of numbers by successively applying Euclid's algorithm to pairs of numbers

    Params:
    nums - a list of positive integers

    Returns:
    the GCD of the numbers in the list
    """
    def gcd(m: int, n: int) -> int:
        """
        Euclid's recursive algorithm for finding the GCD of two numbers
        """
        if n == 0:
            return m
        else:
            return gcd(n, m%n)

    arr_len = len(nums)
    if arr_len == 1:
        return nums[0]
    else:
        g = gcd(nums[0], nums[1])
        for i in range(2, arr_len):
            g = gcd(g, nums[i])
    return g