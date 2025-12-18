"""
QUESTION:
Write a function `convert_base(num, from_base, to_base)` that converts a given number `num` from a base `from_base` to a base `to_base`. The function should handle both string and integer inputs for `num`. The output should be a string representing the converted number.
"""

def convert_base(num, from_base, to_base):
    """
    Converts a given number from a base to another.

    Args:
    num (str or int): The number to convert.
    from_base (int): The base of the input number.
    to_base (int): The target base.

    Returns:
    str: The converted number as a string.
    """

    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base: 
        return alphabet[(n)]
    else:
        return convert_base(n // to_base, from_base, to_base) + alphabet[n % to_base]