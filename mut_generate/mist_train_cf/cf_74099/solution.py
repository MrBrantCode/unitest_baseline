"""
QUESTION:
Implement a function `quick_sort(numbers)` that sorts a list of integers in ascending order using the Quicksort algorithm. The function should be able to handle lists of any length, including empty or single-element lists.
"""

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = numbers[0]
        less = [i for i in numbers[1:] if i <= pivot]
        greater = [i for i in numbers[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)