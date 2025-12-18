"""
QUESTION:
Implement the `elite_truncation` function, which takes three parameters: a string figure representing a number and two integers, low and apex, representing the lower and upper bounds of a range. The function should return the closest integer to the figure within the specified range, rounding towards zero if the figure is halfway between two integers. If the figure is not a valid number or is outside the specified range, return an error message.
"""

def elite_truncation(figure, low, apex):
    '''
    Construct an operation that access to a figure (string) mimicking a digit along with two integers,
    low and apex, which act as limiters of scope. The assignment involves returning the closest integer 
    to the input figure without the assistance of already available functions like round(). Furthermore, 
    corroborate that the supplied figure equates to a valid integer or float, and resides within the assigned boundaries.
    If not, retrieve an error message. In a scenario where the digit finds itself at equal distance from two integers,
    round it in the direction of zero.

    Parameters
    ----------
    figure : str
        The input number as a string.
    low : int
        The lower bound of the range.
    apex : int
        The upper bound of the range.

    Returns
    -------
    int
        The closest integer to the figure within the specified range, or an error message if the figure is invalid or out of range.
    '''
    try:
        num = float(figure)
    except ValueError:
        return "Error: Invalid input."

    if num < low or num > apex:
        return "Error: Out of range."

    if num < 0:
        return int(num) if num-int(num) < 0.5 else int(num) - 1
    else:
        return int(num) if int(num) - num < 0.5 else int(num) + 1