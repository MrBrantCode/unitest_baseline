"""
QUESTION:
Create a function called arrange_checker that takes a list of integers as input. Return a tuple containing the smallest index of an element that is greater than the element immediately following it, and the difference between these two numbers. If no such element exists, return (-1, -1). The input list will not contain any repeated values and will have at least one element. The function should run in O(N) time complexity.
"""

def arrange_checker(arr):
    """
    This function finds the smallest index of an element that is greater than the element immediately following it.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        tuple: A tuple containing the smallest index of an element that is greater than the element immediately following it, 
               and the difference between these two numbers. If no such element exists, returns (-1, -1).
    """
    # iterate over the list to check element by element
    for i in range(len(arr) - 1):
        # if current element is greater than next one
        if arr[i] > arr[i + 1]:
            # return a tuple with index and difference
            return (i, arr[i] - arr[i + 1])

    # if no such element was found, return -1
    return (-1, -1)