"""
QUESTION:
Write a function `array_difference` that takes two arrays of integers or real numbers as input. The function should calculate the absolute differences of corresponding pairs in the arrays and return a list of these differences along with their sum. Ensure the function includes error checking to handle cases where the input arrays are of unequal length or contain non-numerical values.
"""

def array_difference(array1, array2):
    # Check if both arrays have the same length
    if len(array1) != len(array2):
        return "Error: Arrays do not have equal lengths"

    # Create a list for storing differences and variable for total difference
    difference_list = []
    total_difference = 0

    # Calculate the difference for each pair
    for i in range(len(array1)):
        # Check if values are numbers
        if not (isinstance(array1[i], (int, float)) and isinstance(array2[i], (int, float))):
            return "Error: Arrays contain non-numerical values"
        # Calculate absolute difference and add to list and total
        diff = abs(array1[i] - array2[i])
        difference_list.append(diff)
        total_difference += diff

    return difference_list, total_difference