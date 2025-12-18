"""
QUESTION:
Write a function named `doubleArrayElements` that takes an array of numbers as input, creates a new array where each element is the corresponding element in the input array multiplied by 2, and returns the new array. Use a traditional `for` loop to achieve the result, and do not use any built-in array methods such as `.map()`, `.forEach()`, or `.reduce()`.
"""

def doubleArrayElements(input_array):
    """
    This function takes an array of numbers as input, creates a new array where each element is the corresponding element in the input array multiplied by 2, and returns the new array.

    Args:
        input_array (list): A list of numbers.

    Returns:
        list: A new list with each element multiplied by 2.
    """
    new_array = []
    for i in range(len(input_array)):
        new_array.append(input_array[i] * 2)
    return new_array