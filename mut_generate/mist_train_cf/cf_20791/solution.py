"""
QUESTION:
Write a function called `conditional_swap` that takes an array of integers as input. Swap the elements at index 2 and 4 if the sum of the elements at index 0 and 1 is greater than the sum of the elements at index 3 and 4, and the difference between the maximum and minimum values in the array is less than or equal to 10.
"""

def conditional_swap(arr):
    """
    Swap the elements at index 2 and 4 in the array if the sum of the elements at index 0 and 1 is greater than the sum of the elements at index 3 and 4, 
    and the difference between the maximum and minimum values in the array is less than or equal to 10.

    Args:
        arr (list): A list of integers.

    Returns:
        list: The modified list after swapping elements if conditions are met.
    """
    
    # Calculate the sum of the elements at index 0 and 1
    sum_01 = arr[0] + arr[1]
    
    # Calculate the sum of the elements at index 3 and 4
    sum_34 = arr[3] + arr[4]
    
    # Calculate the difference between the maximum and minimum values in the array
    diff_max_min = max(arr) - min(arr)
    
    # Check if the sum of the elements at index 0 and 1 is greater than the sum of the elements at index 3 and 4, 
    # and the difference between the maximum and minimum values in the array is less than or equal to 10
    if sum_01 > sum_34 and diff_max_min <= 10:
        # Swap the elements at index 2 and 4
        arr[2], arr[4] = arr[4], arr[2]
    
    return arr