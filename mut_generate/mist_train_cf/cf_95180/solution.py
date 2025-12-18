"""
QUESTION:
Implement a function called `minL` that takes two lists of positive integers as input and returns the smallest element from both lists. The input lists will always contain at least one element and their lengths will not exceed 10^6. The function should have a time complexity of O(n), where n is the total number of elements in the input lists, and a space complexity of O(1).
"""

def minL(list1, list2):
    """
    Returns the smallest element from two lists of positive integers.

    Args:
        list1 (list): The first list of positive integers.
        list2 (list): The second list of positive integers.

    Returns:
        int: The smallest element from both lists.
    """
    # Initialize the minimum element to the maximum possible value
    min_element = float('inf')

    # Iterate through both lists simultaneously
    for num1, num2 in zip(list1, list2):
        # Update the minimum element if a smaller element is found
        min_element = min(min_element, num1, num2)

    # If one list is longer than the other, find the minimum in the remaining part
    if len(list1) > len(list2):
        min_element = min(min_element, min(list1[len(list2):]))
    elif len(list2) > len(list1):
        min_element = min(min_element, min(list2[len(list1):]))

    return min_element