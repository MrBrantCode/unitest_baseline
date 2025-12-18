"""
QUESTION:
Write a function `calculate_digit_sum(x, y, z)` that takes three integers as input, calculates their product, and returns the sum of the digits of the product. The function should handle negative integers, zero inputs, large input integers (up to 10^9), and non-numeric input, returning an error message for the latter two cases. If any input integer is zero, the function should return 0.
"""

def calculate_digit_sum(x, y, z):
    # Check if any input integers are zero
    if x == 0 or y == 0 or z == 0:
        return 0

    # Check for non-numeric input
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return "Invalid input: non-numeric value"

    # Check for large input integers
    if abs(x) > 10**9 or abs(y) > 10**9 or abs(z) > 10**9:
        return "Invalid input: large input integers"

    # Calculate the product
    product = x * y * z

    # Convert the product to a string to iterate through the digits
    product_str = str(product)

    # Initialize the sum of digits
    digit_sum = 0

    # Iterate through each digit and add it to the sum
    for digit in product_str:
        if digit.isdigit():
            digit_sum += int(digit)

    return digit_sum