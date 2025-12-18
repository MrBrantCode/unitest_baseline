"""
QUESTION:
Write a function `advanced_sort(numbers)` that determines if a list of integers can be sorted in non-decreasing order using a maximum of three operations: reversing any sublist, removing one element, and swapping two elements once. If possible, return `True` along with the sequence of operations performed. If not possible, return `False` with an empty list of operations. If the input list is empty, return `True` with an empty list of operations.
"""

def advanced_sort(numbers):
    """
    Given a list 'numbers' with N integers from 1 to 10^6 in random order. Determine if it's possible 
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
        if numbers[i] > numbers[i + 1]:
            numbers.pop(i)
            operations.append('Remove ' + str(i))
            N -= 1
        else:
            i += 1

        if numbers == sorted(numbers):
            return True, operations

    # If after all operations, list is not sorted
    return False, []