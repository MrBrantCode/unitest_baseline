"""
QUESTION:
Write a function named `lcm` that calculates the Least Common Multiple (LCM) of a list of N integers. The function should validate the input and handle potential errors. The input list should contain between 1 and 10^5 integers, each in the range 1 to 10^9. The function should return the LCM of the input integers or an error message if the input is invalid.
"""

from typing import List
import math

def lcm(sequence: List[int]):
    """
    Calculate the LCM of a list of N integers using an advanced algorithm with consideration for added constraints.
    """
    if type(sequence) != list:
        return "Error: Input is not a list."
    if len(sequence) > 10**5 or len(sequence) < 1:
        return "Error: The number of elements in the list should be in range [1, 10^5]"
    for num in sequence:
        if not isinstance(num, int):
            return "Error: All elements in the list should be integers."
        if num > 10**9 or num < 1:
            return "Error: Numbers in the list should be in range [1, 10^9]"
      
    def lcm_two(a,b):
        """
        Calculate the LCM of two integers a, b.
        """
        return abs(a*b) // math.gcd(a, b)
      
    ans = sequence[0]
    for num in sequence[1:]:
        ans = lcm_two(ans, num)

    return ans