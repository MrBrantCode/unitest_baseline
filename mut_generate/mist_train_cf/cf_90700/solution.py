"""
QUESTION:
Create a function `bubble_sort(numbers)` that takes a list of numbers as input and returns the sorted list in ascending order. The function should implement the bubble sort algorithm. The input list can contain any number of elements and may not be sorted in any particular order. Implement the swap operation correctly to ensure the list is sorted in ascending order.
"""

def entrance(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers