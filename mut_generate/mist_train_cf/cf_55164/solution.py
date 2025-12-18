"""
QUESTION:
Create a function called `swap_elements` that takes an array and two indices as input and swaps the elements at those indices in the array in-place. The function should return the modified array.
"""

def swap_elements(array, index1, index2):
    """
    Swaps the elements at index1 and index2 in the given array in-place.

    Args:
        array (list): The input array.
        index1 (int): The index of the first element to swap.
        index2 (int): The index of the second element to swap.

    Returns:
        list: The modified array with the elements swapped.
    """
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp
    return array