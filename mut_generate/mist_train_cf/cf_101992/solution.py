"""
QUESTION:
Create a function called `bubble_sort` that takes a list of integers as input and returns the sorted list in ascending order using the bubble sort algorithm. The function should not use any built-in sorting functions or libraries and should have a time complexity of O(n^2), where n is the length of the input list. The input list should contain at least 3 elements.
"""

def bubble_sort(numbers):
    n = len(numbers)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True
    return numbers