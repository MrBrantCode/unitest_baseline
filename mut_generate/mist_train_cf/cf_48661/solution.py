"""
QUESTION:
Construct a function `count_nums` that takes an unsorted array of integers as input and returns the quantity of non-repeating, distinct numerical elements and the frequency of each of these unique elements. The function should be optimized for speed and efficiency to handle large data inputs, and null or zero values within the array should be counted as valid numerical elements.
"""

def count_nums(arr):
    """
    This function takes an unsorted array of integers as input and returns the quantity of non-repeating, 
    distinct numerical elements and the frequency of each of these unique elements.

    Parameters:
    arr (list): The input array of integers.

    Returns:
    tuple: A tuple containing the quantity of non-repeating, distinct numerical elements and a dictionary 
    where the keys are the unique elements and the values are their frequencies.
    """

    # Define a dictionary to store the numerical elements and their frequencies
    num_dict = {}

    # Iterate through the array
    for num in arr:
        # If the number is already in the dictionary, increase its count
        if num in num_dict:
            num_dict[num] += 1
        # If the number is not in the dictionary, add it with a count of 1
        else:
            num_dict[num] = 1

    # Return the quantity of non-repeating, distinct numerical elements and the frequency of each unique element
    return len(num_dict), num_dict