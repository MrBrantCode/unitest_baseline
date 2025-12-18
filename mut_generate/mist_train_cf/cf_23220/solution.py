"""
QUESTION:
Implement a function `bubble_sort(numbers)` that sorts a list of numbers in ascending order using the bubble sort algorithm. The function should not use any built-in sorting functions or methods, should have a time complexity of O(n^2), and should have a space complexity of O(1).
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