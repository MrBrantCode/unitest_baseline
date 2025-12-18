"""
QUESTION:
Write a function `advanced_sort` that takes a list of integers `numbers` as input. The function should determine if it's possible to sort the list into non-decreasing order by performing the following operations: 

1. Reverse any sublist any number of times.
2. Remove one element from the list.
3. Swap any two elements once.

The function should return `True` if the list can be sorted, `False` otherwise. If the list is empty, the function should return `True`. The function should also return the sequence of operations taken to sort the list.
"""

def advanced_sort(numbers):
    """
    Given a list 'numbers' with N integers from 1 to 10^6 in random order, determine if it's possible 
    to sort into non-decreasing order by the following operations:
    1. Reverse any sublist any number of times.
    2. Remove one element from the list.
    3. Swap any two elements once.

    If possible, return 'True', if not, 'False'. If the list is empty, return 'True'.
    Also, provide the sequence of operations taken to sort the list.
    """
    N = len(numbers)
    # If list is empty, return True
    if N == 0:
        return True, []

    # If list is already sorted, return True
    if numbers == sorted(numbers):
        return True, []

    # Else perform operations
    i = 0
    operations = []
    while i < N - 1:
        if numbers[i] < numbers[i + 1]:
            numbers.pop(i)
            operations.append('Remove ' + str(i))
            N -= 1
        else:
            i += 1

    if numbers == sorted(numbers):
        return True, operations

    # If after all operations, list is not sorted
    return False, []