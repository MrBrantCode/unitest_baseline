"""
QUESTION:
Implement a function named `quick_sort` that sorts an input list of elements using the quick sort algorithm. The function should include a detailed, multi-line comment explaining the algorithm's steps and its suitability for specific scenarios. Upon successful completion of the sorting operation, the function should print a custom message. The function should be efficient and well-structured, and its time complexity should be suitable for large data sets. The function should not include any input list or test cases, and it should only sort lists that do not contain duplicate values and are not too small.
"""

def quick_sort(arr):
    """
    This function implements quick sort algorithm. 

    The algorithm works as follows:
    1. Select a 'pivot' element from the array and partition the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. 
    2. Recursively sort the sub-arrays.
    3. Combine the sub-arrays with the pivot to get the sorted array.

    Quick sort is very efficient for large data sets. It performs well for data sets that do not contain duplicate values. 

    The function is not suitable for smaller lists as its overhead is higher than simple sorting algorithms like insertion sort.
    It is also not suitable for lists with many duplicate values as they decrease the efficiency of the pivot selection process.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

    items_greater = []
    items_lower = []

    for item in arr:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    print("Custom message: Sorting has been successfully completed.")
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)