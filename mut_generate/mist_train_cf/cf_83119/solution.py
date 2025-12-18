"""
QUESTION:
Design a function 'array_lcm' to compute the Least Common Multiple (LCM) of an array of integers. The function should take a list of integers as input and return the LCM of all the integers in the list.

Constraints: The input list 'arr' will contain between 1 and 10^4 integers, and each integer 'a' in 'arr' will be between 1 and 10^5.

Also, design a function 'is_prime' to check if the resulting LCM is a prime number. The function should take an integer 'n' as input and return True if 'n' is prime, False otherwise.

Constraints: The input integer 'n' will be between 1 and 10^10. The function should be efficient enough to handle large inputs.
"""

from typing import List
from math import gcd

def array_lcm(arr: List[int]) -> int:
    """
    Compute the Least Common Multiple (LCM) of an array of integers.

    Args:
    arr (List[int]): A list of integers.

    Returns:
    int: The LCM of all the integers in the list.
    """
    lcm = arr[0]
    for i in arr[1:]:
        lcm = (lcm * i) // gcd(lcm, i)
    return lcm


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True