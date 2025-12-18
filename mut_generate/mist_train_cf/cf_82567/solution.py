"""
QUESTION:
Create a function `is_monotonic` that checks if a given function is monotonic. A function is considered monotonic if it either always increases or always decreases. Use this function to verify if ReLU (Rectified Linear Unit) and sigmoid functions are monotonic.
"""

def is_monotonic(func, start, end, step):
    """
    Checks if a given function is monotonic.

    Args:
        func (function): The function to check.
        start (float): The start of the range to check.
        end (float): The end of the range to check.
        step (float): The step size.

    Returns:
        bool: True if the function is monotonic, False otherwise.
    """
    increasing = decreasing = True

    x = start
    while x <= end:
        y = func(x)
        next_y = func(x + step)
        
        if next_y > y:
            decreasing = False
        elif next_y < y:
            increasing = False
        
        x += step

    return increasing or decreasing