"""
QUESTION:
Write a function named `calculate_seat_range` that calculates the maximum and minimum values in the "seats" column for a given table with n rows. The table is a list of lists, where each sublist contains a job name and the number of seats, a non-negative integer. The function should return a tuple containing the maximum and minimum seat values. The number of rows in the table is in the range [1, 10^5] and the number of seats for each job is in the range [0, 10^9].
"""

def calculate_seat_range(table):
    # Initialize the maximum and minimum values
    maximum = float('-inf')
    minimum = float('inf')

    # Iterate through each row in the table
    for row in table:
        # Get the number of seats for the current row
        seats = row[1]

        # Update the maximum and minimum values if necessary
        maximum = max(maximum, seats)
        minimum = min(minimum, seats)

    # Return the maximum and minimum values
    return maximum, minimum