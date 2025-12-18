"""
QUESTION:
Write a function named `sum_greater_than_10_not_divisible_by_3` that takes an array of numbers as input and returns the sum of all numbers in the array that are greater than 10 and not divisible by 3.
"""

def sum_greater_than_10_not_divisible_by_3(numbers):
    # Initialize sum variable
    total = 0
    
    # Iterate through each number in the array
    for number in numbers:
        # Check if the number is greater than 10 and not divisible by 3
        if number > 10 and number % 3 != 0:
            # Add the number to the sum
            total += number
    
    # Return the sum
    return total