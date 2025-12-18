"""
QUESTION:
Design a function `swapAndSort(list1, list2)` that takes two lists of numbers as input and interchanges their elements at the same index, then sorts the resulting lists in ascending order. 

The function should handle edge cases where the lists may be of unequal length or one or both lists could be empty. If the lists are of unequal length, only interchange elements at the indices available in both lists, leaving the rest of the elements as is. If one or both lists are empty, return the same lists.

The function should also include error handling to account for any invalid input like non-integer or non-numeric values, and return an error message in such cases.
"""

def swapAndSort(list1, list2):
    """
    This function takes two lists of numbers as input, interchanges their elements at the same index, 
    then sorts the resulting lists in ascending order.

    Args:
    list1 (list): The first list of numbers.
    list2 (list): The second list of numbers.

    Returns:
    tuple: A tuple containing the two sorted lists. If the input lists contain non-numeric values, 
    it returns an error message.
    """
    # Checking for non-numeric values
    try:
        list1 = [float(i) for i in list1]
        list2 = [float(i) for i in list2]
    except ValueError:
        return "Error: Both lists should only contain numeric values."

    # Checking for equal size of both lists.
    min_length = min(len(list1), len(list2))

    # Swapping elements
    for i in range(min_length):
        list1[i], list2[i] = list2[i], list1[i]

    # Bubble sort function
    def bubble_sort(list):
        for i in range(len(list) - 1):
            for j in range(len(list) - 1 - i):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
        return list

    # Sorting the lists
    list1 = bubble_sort(list1)
    list2 = bubble_sort(list2)

    return list1, list2