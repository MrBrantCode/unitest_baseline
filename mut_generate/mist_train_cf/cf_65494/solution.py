"""
QUESTION:
Write a function named `sum_numeric_values` that takes a dictionary as input and returns the sum of its numeric values. Use a loop that behaves like a do-while loop to traverse the dictionary entries.
"""

def sum_numeric_values(input_dict):
    """
    This function calculates the sum of numeric values in a dictionary.

    Args:
        input_dict (dict): A dictionary that may contain numeric values.

    Returns:
        int or float: The sum of numeric values in the dictionary.
    """

    # Initialize the sum to zero
    total = 0

    # Use a for loop to iterate over dictionary entries
    for key in input_dict:
        # Check if the value is numeric (either int or float)
        if isinstance(input_dict[key], (int, float)):
            # Add the numeric value to the total sum
            total += input_dict[key]

    # Return the total sum of numeric values
    return total


def sum_numeric_values_do_while(input_dict):
    """
    This function calculates the sum of numeric values in a dictionary using a do-while loop.

    Args:
        input_dict (dict): A dictionary that may contain numeric values.

    Returns:
        int or float: The sum of numeric values in the dictionary.
    """

    # Initialize the sum to zero
    total = 0

    # Create an iterator for dictionary keys
    subjects = iter(input_dict)

    # Emulate a do-while loop
    while True:
        try:
            # Get the next key from the dictionary
            subject = next(subjects)

            # Check if the value is numeric (either int or float)
            if isinstance(input_dict[subject], (int, float)):
                # Add the numeric value to the total sum
                total += input_dict[subject]
        except StopIteration:
            # Break the loop if there are no more keys
            break

    # Return the total sum of numeric values
    return total