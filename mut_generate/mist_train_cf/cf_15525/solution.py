"""
QUESTION:
Create a function `bubbleSort` that sorts an array in ascending order using Bubble sort. The function should not use any additional data structures or built-in sorting functions, and it should have a time complexity of O(n^2) and a space complexity of O(1).
"""

def bubbleSort(array):
    """
    Sorts an array in ascending order using Bubble sort.
    
    Time complexity: O(n^2)
    Space complexity: O(1)
    
    Args:
        array (list): The list of elements to be sorted.
    
    Returns:
        list: The sorted list in ascending order.
    """
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                # Swap array[j] and array[j+1]
                array[j], array[j+1] = array[j+1], array[j]
    return array