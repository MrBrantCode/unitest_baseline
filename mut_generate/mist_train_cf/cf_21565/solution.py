"""
QUESTION:
Implement a class named `SmallestElement` that takes a list of integers as input. The class should have three methods: `find_using_linear_search`, `find_using_selection_sort`, and `is_sorted`. 

`find_using_linear_search` should return the smallest element in the list using a linear search algorithm with a time complexity of O(n). 

`find_using_selection_sort` should return the smallest element in the list using a selection sort algorithm with a time complexity of O(n^2). 

`is_sorted` should return `True` if the list is sorted in non-decreasing order, and `False` otherwise. 

Both `find_using_linear_search` and `find_using_selection_sort` should handle empty lists by returning an error message, and they should handle lists with duplicate smallest elements by returning the first occurrence. The class should also handle lists with negative numbers.
"""

def find_smallest_using_linear_search(numbers):
    if len(numbers) == 0:
        return "Error: Empty list"
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

def find_smallest_using_selection_sort(numbers):
    if len(numbers) == 0:
        return "Error: Empty list"
    for i in range(len(numbers)):
        smallest = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[smallest]:
                smallest = j
        numbers[i], numbers[smallest] = numbers[smallest], numbers[i]
    return numbers[0]

def is_sorted(numbers):
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            return False
    return True