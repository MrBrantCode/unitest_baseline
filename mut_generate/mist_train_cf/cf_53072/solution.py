"""
QUESTION:
Implement the `extract_number` function, which takes a float `number` and an integer `precision` as input, and returns the `number` with precision preserved up to the specified decimal point, including trailing zeroes. The function should handle both positive and negative floats, and round the last decimal digit if the precision specified is less than the actual precision in the input number.
"""

def extract_number(number: float, precision: int) -> float:
    """ Given a float, it breaks down into
    an integer component (largest integer less or equal to the number) and decimals
    (remainder always less than 1 and greater than -1).

    The function should return the number preserving precision up to a specified decimal point.
    """
    format_string = "{:." + str(precision) + "f}"
    formatted_number = format_string.format(number)
    return float(formatted_number)