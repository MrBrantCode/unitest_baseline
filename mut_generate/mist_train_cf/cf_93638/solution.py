"""
QUESTION:
Create a function called `bubble_sort` that sorts a given list of numbers in ascending order without using the built-in `sort()` function or any other sorting algorithm. The function should take a list of numbers as input, perform the necessary operations to sort the list in ascending order, and return the sorted list. The input list can contain duplicate numbers, and the list should be sorted in-place.
"""

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
    return numbers