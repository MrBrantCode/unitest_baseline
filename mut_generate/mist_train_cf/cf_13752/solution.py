"""
QUESTION:
Write a function named `sum_even_values` that takes a dictionary as input and returns the sum of all even values in the dictionary. If there are no even numbers in the dictionary, the function should return 0.
"""

def sum_even_values(dictionary):
    # Initialize a variable to store the sum
    total_sum = 0

    # Iterate through the values of the dictionary
    for value in dictionary.values():
        # Check if the value is an even number
        if value % 2 == 0:
            # Add the even number to the total sum
            total_sum += value

    # Return the total sum if there are even numbers, otherwise return 0
    return total_sum if total_sum != 0 else 0