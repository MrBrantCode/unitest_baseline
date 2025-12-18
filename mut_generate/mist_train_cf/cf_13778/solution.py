"""
QUESTION:
Implement the `bubble_sort` function to sort a list of numbers in ascending order without using any built-in sorting functions or libraries. The function should take a list of numbers as an argument and return the sorted list.
"""

def entrance(numbers):
    n = len(numbers)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers