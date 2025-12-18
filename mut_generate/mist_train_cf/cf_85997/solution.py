"""
QUESTION:
Design a function named `find_frequency` that takes a sorted array `arr` and a target element `x` as input, and returns the frequency of `x` in `arr`. Implement the function using the binary search algorithm. The function should first find the index of the target element using binary search, then determine the range of the element's occurrence, and finally calculate the frequency of the element within that range. The function should return 0 if the target element is not found in the array.
"""

def find_frequency(arr, x):
    """
    This function calculates the frequency of a target element in a sorted array using binary search.
    
    Parameters:
    arr (list): A sorted list of elements.
    x (int): The target element to find the frequency of.
    
    Returns:
    int: The frequency of the target element if found, 0 otherwise.
    """
    
    # Define a helper function for binary search
    def binary_search(low, high):
        while low <= high:
            mid = (high + low) // 2

            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                return mid
        return -1
    
    # Perform binary search to find the index of the target element
    index = binary_search(0, len(arr) - 1)

    # If the target element is not found, return 0
    if index == -1:
        return 0

    # Find the range of the target element
    left, right = index, index
    while left >= 0 and arr[left] == x:
        left -= 1
    while right < len(arr) and arr[right] == x:
        right += 1

    # Return the frequency of the target element
    return right - left - 1