"""
QUESTION:
Create a function called `copy_array_recursive` that takes two lists of characters, `array1` and `array2`, as input. The function should copy the contents of `array1` to `array2` using recursion, without using any loops or additional variables, and utilizing only the heap for temporary data storage.
"""

def copy_array_recursive(array1, array2, i=0):
    """
    Copies the contents of array1 to array2 using recursion and heap storage.

    Args:
    array1 (list): The source array of characters.
    array2 (list): The target array of characters.
    i (int, optional): The index for recursion. Defaults to 0.

    Returns:
    list: The modified array2 with contents copied from array1.
    """
    if i < len(array1):
        array2[i] = array1[i]
        copy_array_recursive(array1, array2, i + 1)
    return array2