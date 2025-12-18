"""
QUESTION:
Write a function named `sum_divisible_by_three` that takes two 2D arrays as input and returns a new 2D array of the same dimensions where each element is the sum of the corresponding elements in the input arrays if the sum is divisible by 3, otherwise the element is 0.
"""

def sum_divisible_by_three(array1, array2):
    """
    This function takes two 2D arrays as input and returns a new 2D array of the same dimensions.
    Each element in the new array is the sum of the corresponding elements in the input arrays
    if the sum is divisible by 3, otherwise the element is 0.

    Args:
        array1 (list): The first 2D array.
        array2 (list): The second 2D array.

    Returns:
        list: A new 2D array with the sum of corresponding elements if divisible by 3.
    """
    # Create a new array with the same dimensions as the original arrays
    result_array = [[0 for _ in range(len(array1[0]))] for _ in range(len(array1))]

    # Iterate over each element of the arrays
    for i in range(len(array1)):
        for j in range(len(array1[i])):
            # Add the corresponding elements
            total = array1[i][j] + array2[i][j]
            
            # Check if the sum is divisible by 3
            if total % 3 == 0:
                # Store the sum in the result array
                result_array[i][j] = total

    return result_array