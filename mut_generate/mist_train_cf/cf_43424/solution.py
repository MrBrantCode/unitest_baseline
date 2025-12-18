"""
QUESTION:
Implement a function `quick_sort` that takes a list of alphanumeric characters as input and returns a list of characters sorted in alphabetical order using the quicksort algorithm. The function should have a time complexity of O(n log n) on average. Additionally, implement a function `sort_string` that takes a string as input, converts it to a list of characters, sorts the list using the `quick_sort` function, and returns the sorted characters as a string.
"""

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less_than_pivot = [i for i in array[1:] if i <= pivot]
        greater_than_pivot = [i for i in array[1:] if i > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

def sort_string(input_string):
    return ''.join(quick_sort(list(input_string)))