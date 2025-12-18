"""
QUESTION:
Implement a function named `bubble_sort_descending` to sort a list of unique integers in descending order. The list should contain 5 to 10 integers, each within the range of 1 to 100. The function should not use any built-in sorting functions and should return the sorted list.
"""

def bubble_sort_descending(numbers):
    n = len(numbers)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers