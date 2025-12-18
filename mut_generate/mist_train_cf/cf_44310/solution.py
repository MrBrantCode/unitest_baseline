"""
QUESTION:
Find a function `find_missing_and_index` that accepts two arrays and returns the missing number in the second array and its final index if inserted back into the second array at its original sorted position. The first array contains distinct integers, while the second array is a shuffled version of the first array with one number deleted. The time complexity of the algorithm should not exceed O(n log n).
"""

def find_missing_and_index(array1, array2):
    """
    This function finds the missing number in the second array and its final index 
    if inserted back into the second array at its original sorted position.
    
    Parameters:
    array1 (list): The original array with distinct integers.
    array2 (list): A shuffled version of array1 with one number deleted.
    
    Returns:
    str: A string containing the missing number and its final index.
    """
    array1.sort()
    array2.sort()
    for i in range(len(array2)):
        if array1[i] != array2[i]:
            return f"Missing Number: {array1[i]}, Final Index: {i}"
    return f"Missing Number: {array1[-1]}, Final Index: {len(array1)-1}"