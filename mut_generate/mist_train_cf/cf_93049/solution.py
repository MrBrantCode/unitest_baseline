"""
QUESTION:
Write a function called `calculate_statistics` that takes a list of integers as input. The function should calculate the sum of all numbers in the list that are divisible by both 3 and 7, calculate their average, find the maximum and minimum values among those numbers, and count the occurrences of each unique number. The function should then return the average, maximum value, minimum value, and a dictionary of occurrences.
"""

def calculate_statistics(numbers):
    """
    Calculate statistics for numbers divisible by both 3 and 7 in a given list.

    Args:
        numbers (list): A list of integers.

    Returns:
        tuple: A tuple containing the average, maximum value, minimum value, and a dictionary of occurrences.
    """

    # Initialize variables
    sum_of_numbers = 0
    count = 0
    maximum = float('-inf')
    minimum = float('inf')
    occurrences = {}

    # Iterate through each number in the list
    for num in numbers:
        # Check if the number is divisible by both 3 and 7
        if num % 3 == 0 and num % 7 == 0:
            # Add the number to the sum
            sum_of_numbers += num
            # Increment the count variable
            count += 1
            # Update the maximum value
            maximum = max(maximum, num)
            # Update the minimum value
            minimum = min(minimum, num)
            # Increment the count of the unique number
            if num in occurrences:
                occurrences[num] += 1
            else:
                occurrences[num] = 1

    # Calculate the average
    average = sum_of_numbers / count if count > 0 else 0

    # Return the results
    return average, maximum, minimum, occurrences