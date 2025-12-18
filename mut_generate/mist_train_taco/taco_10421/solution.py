"""
QUESTION:
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself. 

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.


Example:

Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14



Note:
The input number n will not exceed 100,000,000. (1e8)
"""

def is_perfect_number(num: int) -> bool:
    """
    Determines if a given number is a perfect number.

    A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding itself.

    Parameters:
    num (int): The number to be checked.

    Returns:
    bool: True if the number is a perfect number, False otherwise.
    """
    perfect_numbers = {6, 28, 496, 8128, 33550336, 8589869056}
    return num in perfect_numbers