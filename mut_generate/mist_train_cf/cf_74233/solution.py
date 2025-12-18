"""
QUESTION:
Implement a function `quick_sort(array)` to sort an unsorted array of integers in ascending order without using built-in sort methods. The array may contain elements that are randomly distributed within a range and may be of any size.
"""

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less_than_pivot = [element for element in array[1:] if element <= pivot]
        greater_than_pivot = [element for element in array[1:] if element > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)