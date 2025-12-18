"""
QUESTION:
Implement the function `bubble_sort` that sorts a list of numbers in ascending order using the bubble sort algorithm. The function should not use any built-in sorting functions or methods. The input list will contain only numbers, and the function should return the sorted list.
"""

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        swapped = False
        for j in range(n-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True
        if not swapped:
            break
    return numbers