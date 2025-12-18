"""
QUESTION:
Implement the `extract_integer` function, which takes a float number and an optional boolean parameter `round_down` (defaulting to True), and returns the integer part of the number. If `round_down` is True, the function should round down to the nearest integer; if False, it should round up. The function should work correctly for both positive and negative numbers.
"""

def extract_integer(number: float, round_down: bool = True) -> int:
    """
    Extracts the integer part of a float number.

    Args:
    number (float): The input float number.
    round_down (bool): Optional parameter to specify whether to round down (default) or up. Defaults to True.

    Returns:
    int: The integer part of the number.
    """
    if round_down:
        return int(number)
    else:
        if number < 0:
            return int(number) if number == int(number) else int(number) - 1
        else:
            return int(number) if number == int(number) else int(number) + 1