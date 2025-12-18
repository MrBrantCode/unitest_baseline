"""
QUESTION:
Write a function search_element that performs either a linear search or a binary search for a specific element in a sorted array. The function should take three parameters: a sorted array, an element to be searched, and a method string. The method string should be either "linear" or "binary". If the method is "linear", the function should perform a linear search; if the method is "binary", the function should perform a binary search. The function should return the index of the first occurrence of the element if it is found, and -1 otherwise.
"""

def search_element(array, element, method):
    """
    Searches for an element in a sorted array using either linear or binary search.

    Args:
        array (list): A sorted list of elements.
        element: The element to be searched.
        method (str): The search method. Either "linear" or "binary".

    Returns:
        int: The index of the first occurrence of the element if found, -1 otherwise.
    """
    if method == "linear":
        for i in range(len(array)):
            if array[i] == element:
                return i
        return -1
    
    elif method == "binary":
        low = 0
        high = len(array) - 1

        while low <= high:
            mid = (high + low) // 2

            if array[mid] < element:
                low = mid + 1
            elif array[mid] > element:
                high = mid - 1
            else:
                return mid
        return -1