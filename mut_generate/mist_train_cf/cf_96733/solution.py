"""
QUESTION:
Write a function `find_max_min` that calculates the maximum and minimum values in the "seats" column for a given table with n rows. The table is a list of lists where each inner list contains a job name and the number of seats. The function should return a tuple containing the maximum and minimum values of the seats column.

Constraints:
- The number of rows in the table is in the range [1, 10^5].
- The number of seats for each job is in the range [1, 10^9] or can be negative.
"""

def find_max_min(table):
    max_seat = float('-inf')  # Initialize max_seat with negative infinity
    min_seat = float('inf')  # Initialize min_seat with positive infinity

    for row in table:
        seat = row[1]
        if seat > max_seat:
            max_seat = seat
        if seat < min_seat:
            min_seat = seat
    
    return max_seat, min_seat