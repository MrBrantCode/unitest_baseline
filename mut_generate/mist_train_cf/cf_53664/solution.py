"""
QUESTION:
Create a function named 'check_integer_in_list' that takes two parameters: 'x', an integer, and 'n', a list of integers. If 'n' is not in ascending order, sort 'n' without using Python's built-in 'sort()' function. Then, implement a binary search algorithm to find 'x' in the sorted list. Return "x exists in the list" if 'x' is found and "x does not exist in the list" otherwise.
"""

def check_integer_in_list(x, n):
    """
    Check if an integer exists in a list.
    
    If the list is not in ascending order, it is sorted without using Python's built-in 'sort()' function.
    Then, a binary search algorithm is implemented to find 'x' in the sorted list.

    Parameters:
    x (int): The target integer.
    n (list): A list of integers.

    Returns:
    str: "x exists in the list" if 'x' is found, "x does not exist in the list" otherwise.
    """

    # Function to check if the list is in ascending order
    def check_order(lst):
        return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

    # Function to sort the list using bubble sort
    def bubble_sort(lst):
        lst_length = len(lst)
        for i in range(lst_length):
            for j in range(0, lst_length-i-1):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
        return lst

    # Function to perform binary search
    def binary_search(lst, x):
        low = 0
        high = len(lst) - 1
        mid = 0

        while low <= high:
            mid = (high + low) // 2
            if lst[mid] < x:
                low = mid + 1
            elif lst[mid] > x:
                high = mid - 1
            else:
                return mid
        return -1

    # Check if the list is in ascending order and sort it if not
    if not check_order(n):
        n = bubble_sort(n)

    # Perform binary search to find 'x'
    result = binary_search(n, x)

    # Return the result
    if result != -1:
        return "x exists in the list"
    else:
        return "x does not exist in the list"