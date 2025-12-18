"""
QUESTION:
Implement the `bubble_sort` and `quick_sort` functions in Python to sort a list of integers in ascending order. The `bubble_sort` function should use the bubble sort algorithm, which repeatedly swaps adjacent elements if they are in the wrong order, while the `quick_sort` function should use the quick sort algorithm, which selects a pivot element and partitions the other elements into two sub-arrays based on whether they are less than or greater than the pivot.
"""

def bubble_sort(lst):
    for passnum in range(len(lst) - 1, 0, -1):
        for i in range(passnum):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
    return lst

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        less_sublst = [i for i in lst[1:] if i <= pivot]
        greater_sublst = [i for i in lst[1:] if i > pivot]
        return quick_sort(less_sublst) + [pivot] + quick_sort(greater_sublst)