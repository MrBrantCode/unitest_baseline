"""
QUESTION:
Create a function named `median` that calculates the median of a list of numbers without using built-in sorting functions or sorting the list. The function should be able to handle collections containing negative integers and floating point numbers. Note that achieving constant time complexity for this problem is not feasible, so a linear time complexity using the QuickSelect algorithm is acceptable. The function should return a single value representing the median of the input list.
"""

def median(l: list) -> float:
    """
    Return median of elements in the list l without sorting or using built-in functions.

    Handles collections including negative numbers and floating point numbers 
    using the QuickSelect algorithm for linear time complexity.
    """
    def partition(num_list, low, high):
        pivot = num_list[high]
        i = low - 1
        for j in range(low, high):
            if num_list[j] <= pivot:
                i += 1
                num_list[i], num_list[j] = num_list[j], num_list[i]
        num_list[i+1], num_list[high] = num_list[high], num_list[i+1]
        return i + 1

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

    num_list = l if isinstance(l, list) else list(l)
    length = len(num_list)

    if length % 2 == 1:
        # If list has odd number of elements, the median is the middle element
        return quick_select(num_list, length // 2)
    else:
        # If list has even number of elements, the median is the average of the two middle elements
        return 0.5 * (quick_select(num_list, length // 2 - 1) + quick_select(num_list, length // 2))