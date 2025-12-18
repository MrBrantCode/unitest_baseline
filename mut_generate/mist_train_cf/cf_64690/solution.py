"""
QUESTION:
Implement a function `median(l: list) -> float` that calculates the median of elements in the list `l` without sorting or using built-in functions. The function should handle collections including negative numbers and floating point numbers, and it should use the QuickSelect algorithm for linear time complexity. The input list `l` can contain any type of numbers (integers or floats) and can have either an odd or even number of elements. If the list has an odd number of elements, the median is the middle element. If the list has an even number of elements, the median is the average of the two middle elements.
"""

def quick_select(num_list, k):
    if len(num_list) == 1:
        return num_list[0]

    pivot_index = partition(num_list, 0, len(num_list) - 1)

    if pivot_index == k:
        return num_list[k]
    elif pivot_index > k:
        return quick_select(num_list[:pivot_index], k)
    else:
        return quick_select(num_list[pivot_index + 1:], k - pivot_index - 1)


def partition(num_list, low, high):
    pivot = num_list[high]
    i = low - 1
    for j in range(low, high):
        if num_list[j] <= pivot:
            i += 1
            num_list[i], num_list[j] = num_list[j], num_list[i]
    num_list[i+1], num_list[high] = num_list[high], num_list[i+1]
    return i + 1


def median(l: list) -> float:
    """
    Return median of elements in the list l without sorting or using built-in functions.

    Handles collections including negative numbers and floating point numbers 
    using the QuickSelect algorithm for linear time complexity.

    """
    num_list = l if isinstance(l, list) else list(l)
    length = len(num_list)

    if length % 2 == 1:
        # If list has odd number of elements, the median is the middle element
        return quick_select(num_list, length // 2)
    else:
        # If list has even number of elements, the median is the average of the two middle elements
        return 0.5 * (quick_select(num_list, length // 2 - 1) + quick_select(num_list, length // 2))