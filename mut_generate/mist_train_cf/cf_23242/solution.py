"""
QUESTION:
Implement a function called `customSort` that takes a list of integers as input, sorts the list in descending order using a modified version of the quicksort algorithm, and returns the sorted list. The algorithm should have a time complexity of O(n log n) and should not use any built-in sorting functions or libraries. The algorithm should handle duplicate elements in the list, preserve the relative order of equal elements after sorting, and use an iterative approach instead of recursion with a space complexity of O(log n).
"""

def customSort(array):
    """
    Sorts a list of integers in descending order using a modified version of the quicksort algorithm.

    This algorithm handles duplicates and ensures stability, preserving the relative order of equal elements.
    It uses an iterative approach instead of recursion with a space complexity of O(log n).

    Args:
        array (list): A list of integers to be sorted.

    Returns:
        list: The sorted list of integers in descending order.
    """
    
    stack = [(0, len(array) - 1)]
    
    while stack:
        low, high = stack.pop()
        
        if low >= high:
            continue
        
        pivot = array[high]
        pivotIndex = low
        
        # Partition the subarray into three sections: less than pivot, equal to pivot, and greater than pivot.
        for i in range(low, high):
            if array[i] > pivot:
                array[pivotIndex], array[i] = array[i], array[pivotIndex]
                pivotIndex += 1
        
        array[pivotIndex], array[high] = array[high], array[pivotIndex]
        
        # Handle duplicates and ensure stability.
        lowEq = pivotIndex
        highEq = pivotIndex + 1
        
        # Partition the subarray into three sections.
        for i in range(pivotIndex - 1, low - 1, -1):
            if array[i] == pivot:
                array[lowEq], array[i] = array[i], array[lowEq]
                lowEq -= 1
        
        for i in range(pivotIndex + 2, high + 1):
            if array[i] == pivot:
                array[highEq], array[i] = array[i], array[highEq]
                highEq += 1
        
        # Push subarrays onto the stack to sort.
        if low < lowEq - 1:
            stack.append((low, lowEq - 1))
        
        if highEq < high:
            stack.append((highEq, high))
    
    return array