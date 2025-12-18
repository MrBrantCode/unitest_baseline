"""
QUESTION:
Write a function `filter_and_sort(numbers)` that takes a list of integers as input, filters out the numbers that are divisible by both 2 and 3, and returns the filtered numbers in descending order. You must implement the filtering and sorting logic from scratch using loops and conditional statements, without using any built-in Python functions or libraries, and without using additional data structures to store intermediate results. All operations must be performed in-place, modifying the original list directly.
"""

def filter_and_sort(numbers):
    # Iterate over the list in reverse order
    for i in range(len(numbers)-1, -1, -1):
        # Check if the number is divisible by both 2 and 3
        if numbers[i] % 2 == 0 and numbers[i] % 3 == 0:
            # Remove the number from the list
            numbers.pop(i)

    # Sort the list in descending order using bubble sort algorithm
    n = len(numbers)
    for i in range(n-1):
        for j in range(n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    
    return numbers