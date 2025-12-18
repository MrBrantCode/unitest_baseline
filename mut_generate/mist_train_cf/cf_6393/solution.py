"""
QUESTION:
Create a function `calculate_sum` that takes an array of positive integers as a parameter. The function should continuously add each item to the total sum if the current item is larger than the previous item, and keep track of the index of the largest valid item in the array. The function should return the total sum of all the valid items and the index of the largest valid item. The time complexity of the function should be O(n), where n is the number of elements in the array.
"""

def calculate_sum(arr):
    """
    This function calculates the sum of valid items in the array where valid items are those
    that are larger than the previous item. It also keeps track of the index of the largest valid item.

    Parameters:
    arr (list): A list of positive integers.

    Returns:
    tuple: A tuple containing the sum of all valid items and the index of the largest valid item.
    """
    total_sum = 0
    max_index = -1
    prev = None
    
    for i in range(len(arr)):
        if prev is None or arr[i] > prev:
            total_sum += arr[i]
            max_index = i
        prev = arr[i]
    
    return total_sum, max_index