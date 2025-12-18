"""
QUESTION:
Create a function named `append_elements` that takes two parameters: `array` and `elements`. The function should return a new array that is a combination of `array` and `elements`, without modifying the original `array`. The function should be able to handle empty inputs for both `array` and `elements`. The function should not use the built-in `append()` function.
"""

def append_elements(array, elements):
    """
    Returns a new array that is a combination of `array` and `elements`, 
    without modifying the original `array`.

    Args:
        array (list): The original array.
        elements (list): The elements to be appended.

    Returns:
        list: A new array that combines `array` and `elements`.
    """
    return array + elements