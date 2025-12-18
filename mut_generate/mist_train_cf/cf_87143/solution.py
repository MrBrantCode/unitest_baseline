"""
QUESTION:
Create a function called `fill_with_zeros` that fills a 2D jagged array with zeros using a single loop and without using any built-in functions or methods. The input array is a list of lists where each inner list can have a different length.
"""

def fill_with_zeros(array):
    """
    Fills a 2D jagged array with zeros using a single loop and without using any built-in functions or methods.
    
    Args:
        array (list of lists): A 2D jagged array where each inner list can have a different length.
    
    Returns:
        list of lists: The input array filled with zeros.
    """
    # Iterate over each inner array and set all elements to zero
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = 0
    return array