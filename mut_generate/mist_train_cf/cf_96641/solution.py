"""
QUESTION:
Write a function named `sum_even_greater_than_10` that takes a dictionary as input, sums all the even values greater than 10, and returns the sum. If no such values exist in the dictionary, return -1.
"""

def sum_even_greater_than_10(dictionary):
    # Initialize the sum variable
    sum_val = 0

    # Iterate over the dictionary values
    for value in dictionary.values():
        # Check if the value is an even number and greater than 10
        if value % 2 == 0 and value > 10:
            # Add the value to the sum
            sum_val += value

    # Check if there are no even numbers greater than 10 in the dictionary
    if sum_val == 0:
        return -1

    # Return the sum
    return sum_val