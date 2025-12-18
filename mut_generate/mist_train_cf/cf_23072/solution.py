"""
QUESTION:
Write a function named `calculate_statistics` that takes a list of at least 10 non-negative numbers as input. The function should calculate the sum and average of the numbers, find the maximum and minimum values in the list, and print these statistics. If the list is empty or contains only one number, the function should print an error message instead.
"""

def calculate_statistics(numbers):
    if len(numbers) < 10:
        print("Error: The list should contain at least 10 non-negative numbers.")
        return
    
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    print("Sum:", total)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)