"""
QUESTION:
Create a function `merge_and_sort_desc` that merges two arrays and returns a new array containing all elements from the first array followed by all elements from the second array. The resulting array should be sorted in descending order without using any built-in sorting functions.
"""

def merge_and_sort_desc(arr1, arr2):
    """
    Merge two arrays and return a new array containing all elements from the first array 
    followed by all elements from the second array. The resulting array is sorted in descending order.

    Args:
        arr1 (list): The first array.
        arr2 (list): The second array.

    Returns:
        list: A new array containing all elements from the first array followed by all elements 
        from the second array, sorted in descending order.
    """
    res = arr1 + arr2  # merge arrays
    n = len(res)
    
    # Sort array in descending order
    for i in range(n):
        for j in range(i + 1, n):
            if res[i] < res[j]:
                temp = res[i]
                res[i] = res[j]
                res[j] = temp
                
    return res