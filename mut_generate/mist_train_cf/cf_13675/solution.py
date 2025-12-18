"""
QUESTION:
Design a function named `calculateLCM` that takes a list of integers as input and returns the greatest common multiple (LCM) of all the numbers in the list. The time complexity of the function should be O(n^2) and the space complexity should be O(1).
"""

def calculateLCM(nums):
    """
    Calculate the least common multiple (LCM) of a list of numbers.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The least common multiple of the input numbers.
    """
    def calculateGCD(a, b):
        """Calculate the greatest common divisor (GCD) of two numbers using the Euclidean algorithm."""
        while b != 0:
            a, b = b, a % b
        return a

    lcm = nums[0]
    for num in nums[1:]:
        lcm = (lcm * num) // calculateGCD(lcm, num)
    return lcm