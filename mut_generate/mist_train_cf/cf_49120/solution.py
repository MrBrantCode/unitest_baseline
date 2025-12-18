"""
QUESTION:
Write a function `SpecialFilter` that takes a list of integers as input and returns the count of numbers that satisfy the following conditions:
- The number has 4 digits (i.e., its absolute value is greater than 999 and less than 10000).
- The first and last digits are even.
- The second digit is even and the third digit is odd.
Note: The function should handle negative numbers and ignore numbers that do not meet the above conditions.
"""

def SpecialFilter(nums):
    """
    This function takes a list of integers as input and returns the count of numbers 
    that satisfy the following conditions:
    - The number has 4 digits (i.e., its absolute value is greater than 999 and less than 10000).
    - The first and last digits are even.
    - The second digit is even and the third digit is odd.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The count of numbers that satisfy the conditions.
    """
    count = 0
    for num in nums:
        if abs(num) > 999 and abs(num) < 10000:
            num_str = str(abs(num))
            if len(num_str) == 4 and int(num_str[0]) % 2 == 0 and int(num_str[-1]) % 2 == 0:
                if int(num_str[1]) % 2 == 0 and int(num_str[2]) % 2 != 0:
                    count += 1
    return count