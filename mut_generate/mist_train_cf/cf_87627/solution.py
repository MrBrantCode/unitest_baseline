"""
QUESTION:
Write a function named `absolute_difference(x, y)` that finds the absolute difference between two positive integers `x` and `y` (both less than or equal to 1000) without using any built-in functions or operators (e.g., `abs()` or `-`).
"""

def absolute_difference(x, y):
    # Swap values if x is less than y
    if x < y:
        x, y = y, x

    # Initialize variables
    difference = 0
    carry = 0

    # Calculate absolute difference digit by digit
    while x > 0 or y > 0:
        # Get the last digit of x and y
        digit_x = x % 10
        digit_y = y % 10

        # Calculate the difference and add the carry
        diff = digit_x - digit_y + carry

        # Adjust the difference and carry
        if diff < 0:
            diff += 10
            carry = -1
        else:
            carry = 0

        # Update the difference variable
        difference = difference * 10 + diff

        # Remove the last digit from x and y
        x //= 10
        y //= 10

    # Return the absolute value of the difference
    return difference