"""
QUESTION:
Create a function `validate_array` that takes a multi-dimensional array as input. Each sub-array contains three elements: a string representing a binary number, an integer, and a boolean. The function should return True if the following conditions are met for all sub-arrays: the binary string can be successfully converted to a decimal number, the integer is a prime number, and the boolean matches the truthiness of the binary string after conversion. The function should return False otherwise. The boolean value is considered True if the decimal equivalent of the binary string is greater than 0 and False otherwise.
"""

def validate_array(arr):
    """
    Validate a multi-dimensional array where each sub-array contains a binary string, 
    an integer, and a boolean. The function returns True if the binary string can be 
    successfully converted to a decimal number, the integer is a prime number, and 
    the boolean matches the truthiness of the binary string after conversion.

    Args:
        arr (list): A multi-dimensional array.

    Returns:
        bool: True if all sub-arrays meet the conditions, False otherwise.
    """
    def is_prime(n):
        """Check if integer n is a prime"""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i = i + 6
        return True

    for item in arr:
        if not isinstance(item[0], str) or not isinstance(item[1], int) or not isinstance(item[2], bool):
            return False
        try:
            decimal = int(item[0], 2)
        except ValueError:
            return False
        if item[2] != bool(decimal):
            return False
        if not is_prime(item[1]):
            return False
    return True