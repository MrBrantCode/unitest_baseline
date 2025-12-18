"""
QUESTION:
Create a function called findMaxMin that takes an array of integers as input and returns the maximum and minimum elements in the array. The function should compare each element in the array to find the maximum and minimum values.
"""

def findMaxMin(arr):
    """
    This function finds the maximum and minimum elements in an array.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    tuple: A tuple containing the maximum and minimum elements in the array.
    """
    maxEle = minEle = arr[0]
    for num in arr:
        if num > maxEle:
            maxEle = num
        elif num < minEle:
            minEle = num
    return maxEle, minEle