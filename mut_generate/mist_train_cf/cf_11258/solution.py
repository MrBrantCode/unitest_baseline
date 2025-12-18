"""
QUESTION:
Create a function `find_closest_number` that takes an array of numbers and a target number as input, and returns the number in the array that is closest to the target number. If the array is empty, return an error message. If there are multiple numbers equally close to the target number, return the smallest one.
"""

def find_closest_number(array, number):
    """
    This function finds the number in the array that is closest to the target number.
    
    If the array is empty, it returns an error message.
    If there are multiple numbers equally close to the target number, it returns the smallest one.

    Parameters:
    array (list): A list of numbers.
    number (int): The target number.

    Returns:
    int or str: The closest number in the array or an error message if the array is empty.
    """
    
    if len(array) == 0:
        return "Error: Array is empty."
    
    closest = array[0]
    diff = abs(array[0] - number)
    
    for i in range(1, len(array)):
        if abs(array[i] - number) < diff:
            closest = array[i]
            diff = abs(array[i] - number)
        elif abs(array[i] - number) == diff and array[i] < closest:
            closest = array[i]
    
    return closest