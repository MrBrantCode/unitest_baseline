"""
QUESTION:
Write a function called check_overflow that takes an integer and a data type as input, and returns a boolean indicating whether an overflow would occur when storing the integer using the specified data type.

The data type will be represented as a string, with possible values of "int8", "int16", "int32", and "int64", representing signed integers of 8, 16, 32, and 64 bits respectively. The function should handle both positive and negative integers.

The function should not attempt to actually store the integer, but rather calculate whether an overflow would occur based on the range of the specified data type.
"""

def check_overflow(num: int, data_type: str) -> bool:
    """
    Checks if an overflow would occur when storing an integer using the specified data type.

    Args:
    num (int): The integer to check.
    data_type (str): The data type to check against, one of "int8", "int16", "int32", "int64".

    Returns:
    bool: True if an overflow would occur, False otherwise.
    """
    max_values = {
        "int8": 2**7 - 1,
        "int16": 2**15 - 1,
        "int32": 2**31 - 1,
        "int64": 2**63 - 1,
    }
    min_values = {
        "int8": -2**7,
        "int16": -2**15,
        "int32": -2**31,
        "int64": -2**63,
    }

    return num < min_values[data_type] or num > max_values[data_type]