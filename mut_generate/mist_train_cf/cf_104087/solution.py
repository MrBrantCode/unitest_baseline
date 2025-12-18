"""
QUESTION:
Create a function named `calculate_average` that takes a list of integers as input. The function should calculate the average of the numbers in the list, excluding any numbers that are divisible by 3. The average is calculated as the sum of all non-excluded numbers divided by the total count of non-excluded numbers.
"""

def calculate_average(numbers):
    # Filter out numbers divisible by 3
    filtered_numbers = [num for num in numbers if num % 3 != 0]

    # Calculate the average
    average = sum(filtered_numbers) / len(filtered_numbers)

    return average