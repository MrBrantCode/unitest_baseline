"""
QUESTION:
Create a function called `clamp_number` that takes a number and its minimum and maximum allowed values as input. If the input number is negative, return its absolute value before clamping. Clamp the number to the minimum and maximum values, and return a string if the clamped number is within 10% of either boundary. Otherwise, return the clamped number. The input number and the minimum and maximum values can be floating-point numbers.
"""

def clamp_number(num, min_val, max_val):
    """
    Clamp a number to a specified range and return a string if it's within 10% of the boundary.

    Args:
    num (float): The input number.
    min_val (float): The minimum allowed value.
    max_val (float): The maximum allowed value.

    Returns:
    float or str: The clamped number or a string indicating proximity to the boundary.
    """
    
    # If the input number is negative, return its absolute value before clamping.
    if num < 0:
        num = abs(num)
    
    # Clamp the number to the minimum and maximum values.
    if num < min_val:
        if min_val - num <= 0.1 * min_val:
            # Return a string if the clamped number is within 10% of the minimum boundary.
            return f"The number is within 10% of the minimum value: {min_val - num} away from the boundary."
        else:
            return min_val
    elif num > max_val:
        if num - max_val <= 0.1 * max_val:
            # Return a string if the clamped number is within 10% of the maximum boundary.
            return f"The number is within 10% of the maximum value: {num - max_val} away from the boundary."
        else:
            return max_val
    else:
        # Return the clamped number.
        return num