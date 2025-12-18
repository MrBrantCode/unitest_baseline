"""
QUESTION:
Implement a function called `quicksort` that sorts a list of integers in descending order using the Quick Sort algorithm. The function should handle lists containing duplicate elements and return the sorted list.
"""

def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[-1]
    greater = []
    equal = []
    smaller = []
    for element in lst:
        if element > pivot:
            greater.append(element)
        elif element < pivot:
            smaller.append(element)
        else:
            equal.append(element)
    sorted_greater = quicksort(greater)
    sorted_smaller = quicksort(smaller)
    return sorted_greater + equal + sorted_smaller