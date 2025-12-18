"""
QUESTION:
Write a function `sum_of_squares(n)` that calculates the sum of the unique squares of numbers from 0 to n-1, where n is an integer up to 10^9. Ensure a time complexity of O(n) and a space complexity of O(1).
"""

def sum_of_squares(n):
    # Initialize the sum of squares to 0
    sum_of_squares = 0

    # Create an empty set to store the squares
    squares_set = set()

    # Iterate from 0 to n-1
    for i in range(n):
        # Calculate the square of the current number
        square = i**2

        # If the square is already in the set, skip it
        if square in squares_set:
            continue

        # Add the square to the set
        squares_set.add(square)

        # Add the square to the sum of squares
        sum_of_squares += square

    # Return the sum of squares
    return sum_of_squares