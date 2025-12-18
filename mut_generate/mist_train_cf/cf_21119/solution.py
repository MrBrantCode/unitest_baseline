"""
QUESTION:
Implement a function `is_armstrong_number(num: int) -> bool` that checks if a given integer `num` is an Armstrong number. An Armstrong number is a number equal to the sum of its digits raised to the power of the number of digits. The function should return `True` if the number is an Armstrong number, and `False` otherwise. It should handle negative numbers, non-integer inputs, and numbers outside the range of 0 to 1,000,000. Additionally, it should provide the decomposition of the Armstrong number as a list of its digits raised to the power of the number of digits.
"""

def is_armstrong_number(num: int) -> bool:
    """
    Checks if a given integer is an Armstrong number.
    
    Args:
    num (int): The number to be checked.
    
    Returns:
    bool: True if the number is an Armstrong number, False otherwise.
    list: A list of the digits raised to the power of the number of digits.
    """
    
    # Check if input is an integer
    if not isinstance(num, int):
        return False, []
    
    # Check if number is within the valid range
    if num < 0 or num > 1000000:
        return False, []
    
    # Convert the number to a list of digits
    digits = [int(x) for x in str(num)]
    
    # Calculate the power for the Armstrong number
    power = len(digits)
    
    # Calculate the sum of the digits raised to the power
    sum_of_digits = sum([x ** power for x in digits])
    
    # Check if the number is an Armstrong number
    if sum_of_digits == num:
        # Return True and the decomposition of the Armstrong number
        return True, [x ** power for x in digits]
    else:
        # Return False and an empty list
        return False, []