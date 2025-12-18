"""
QUESTION:
Implement a function named `bubble_sort` that takes a list of tuples as input, where each tuple contains a name and an age. The function should sort the list in descending order based on the age using the bubble sort algorithm and return the sorted list. The function should not take any additional parameters.
"""

def bubble_sort(data):
    """
    Sorts a list of tuples in descending order based on the age using the bubble sort algorithm.

    Args:
        data (list): A list of tuples, where each tuple contains a name and an age.

    Returns:
        list: The sorted list of tuples.
    """

    # Initialize 'swapped' variable
    swapped = True

    # Create a while loop
    while swapped:
        # Set 'swapped' to False
        swapped = False
        # Iterate through the list
        for i in range(len(data) - 1):
            # Compare ages
            if data[i][1] < data[i+1][1]:
                # Swap positions
                data[i], data[i+1] = data[i+1], data[i]
                # Set 'swapped' to True
                swapped = True
        # Check if 'swapped' is False
        if not swapped:
            break

    # Return the sorted list
    return data