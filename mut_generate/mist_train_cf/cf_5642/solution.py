"""
QUESTION:
Implement a function named `sort_array` that sorts an array of numbers in ascending order without using built-in sorting functions or methods. The function should have a time complexity of O(n^2) or less and handle arrays containing non-numeric elements by displaying an error message. The function should not modify the input array and instead return the sorted array. If the array contains non-numeric elements, the function should return an error message instead of the sorted array.
"""

def sort_array(arr):
    """
    Sorts an array of numbers in ascending order without using built-in sorting functions or methods.
    
    Args:
        arr (list): The input array to be sorted.
    
    Returns:
        list: The sorted array if all elements are numeric; otherwise, returns an error message.
    """
    
    # Check if the array contains non-numeric elements
    for element in arr:
        try:
            float(element)
        except ValueError:
            return "Error: Array contains non-numeric elements"
    
    # Implement bubble sort algorithm
    arr_copy = arr[:]  # Create a copy of the input array
    n = len(arr_copy)
    for i in range(n):
        for j in range(n-i-1):
            if arr_copy[j] > arr_copy[j+1]:
                arr_copy[j], arr_copy[j+1] = arr_copy[j+1], arr_copy[j]
    
    return arr_copy