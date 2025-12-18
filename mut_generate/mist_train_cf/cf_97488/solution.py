"""
QUESTION:
Implement a function `bubble_sort` that takes a list of numbers as input, sorts the list in ascending order without using any built-in sorting functions or methods, and returns the sorted list. The function should have a time complexity of O(n^2) and space complexity of O(1).
"""

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True
        if not swapped:
            break
    return numbers