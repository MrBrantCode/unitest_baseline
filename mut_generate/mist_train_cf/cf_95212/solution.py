"""
QUESTION:
Optimize a loop that iterates over a multidimensional array and only processes elements meeting a specific condition. The function should take in a 2D array and a condition function as input. The condition function is a function that takes in an element and returns True if the element meets the condition, False otherwise.
"""

def process_elements(array, condition):
    """
    Iterate over a 2D array and process elements meeting a specific condition.

    Args:
    array (list): A 2D list of elements.
    condition (function): A function that takes an element and returns True if the element meets the condition, False otherwise.

    Returns:
    list: A list of elements that meet the condition.
    """
    result = []
    for row in array:
        for element in row:
            if condition(element):
                result.append(element)
    return result