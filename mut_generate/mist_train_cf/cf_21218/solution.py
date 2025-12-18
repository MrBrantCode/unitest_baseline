"""
QUESTION:
Write a function `sum_corresponding_elements` that takes two arrays of integers, `arr1` and `arr2`, as input and returns a new array containing the sum of corresponding elements from both arrays. The function should handle arrays of different lengths by appending the remaining elements of the longer array to the new array. If the sum of corresponding elements exceeds 100, the function should append 100 to the new array instead.
"""

def sum_corresponding_elements(arr1, arr2):
    """
    This function takes two arrays of integers as input and returns a new array containing 
    the sum of corresponding elements from both arrays. If the sum of corresponding elements 
    exceeds 100, the function appends 100 to the new array instead.

    Args:
        arr1 (list): The first array of integers.
        arr2 (list): The second array of integers.

    Returns:
        list: A new array containing the sum of corresponding elements from both arrays.
    """

    # Find the maximum length of the two arrays
    max_len = max(len(arr1), len(arr2))

    # Initialize a new array to store the sum of corresponding elements
    new_arr = []

    # Iterate through the arrays
    for i in range(max_len):
        # Get the corresponding elements from arr1 and arr2, defaulting to 0 if out of range
        element1 = arr1[i] if i < len(arr1) else 0
        element2 = arr2[i] if i < len(arr2) else 0

        # Calculate the sum of the corresponding elements
        sum_elements = element1 + element2

        # If the sum exceeds 100, append 100 to the new array
        new_arr.append(100 if sum_elements > 100 else sum_elements)

    return new_arr