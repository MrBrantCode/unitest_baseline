"""
QUESTION:
Implement a function called `quick_sort` that takes a list of integers as input and returns the sorted list using the Quick Sort technique. The function should use recursion to sort the list. The input list can contain any number of integers, but the function should be able to handle lists with one or zero elements without requiring additional sorting.
"""

def quick_sort(list):
    # If the incoming list has less than or equal to one element, there's no need to sort
    if len(list) <= 1:
        return list
    
    # Select the pivot. Might be more efficient to choose a random element
    # In this case, we choose the last element of the list.
    pivot = list[len(list) - 1]

    # Elements less than pivot go in the left list, elements greater go in the right
    left = []
    right = []
    
    for i in range(0, len(list) - 1):
        if list[i] < pivot:
            left.append(list[i])
        else:
            right.append(list[i])

    # Use recursion to sort the left and the right lists
    return quick_sort(left) + [pivot] + quick_sort(right)