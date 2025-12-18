"""
QUESTION:
Implement the QuickSort function to sort a list of elements. The function should utilize the divide-and-conquer strategy and must include the partitioning process. The function must be able to handle lists of varying sizes and should have an average time complexity of O(n log n).
"""

def quick_sort(arr):
    """
    Sorts a list of elements using the QuickSort algorithm.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    if len(arr) <= 1:
        # Base case: If the list has one or zero elements, it's already sorted.
        return arr
    else:
        # Select the pivot element (in this case, the middle element).
        pivot = arr[len(arr) // 2]
        # Divide the list into three sub-lists: elements less than the pivot,
        # elements equal to the pivot, and elements greater than the pivot.
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        # Recursively apply the QuickSort function to the sub-lists and combine the results.
        return quick_sort(left) + middle + quick_sort(right)