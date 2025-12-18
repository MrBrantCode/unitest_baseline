"""
QUESTION:
Write a function `calculate_sum_of_digits(x, y, z)` that takes three numbers as input, calculates their product, and then calculates the sum of the digits of the product. The function should handle negative numbers, zero, large input numbers up to 10^9, and floating-point input numbers. If any of the input numbers are non-numeric or empty, the function should return an error message.
"""

def calculate_sum_of_digits(x, y, z):
    # Check for empty values
    if x == "" or y == "" or z == "":
        return "Invalid input: empty value"
    
    # Check for non-numeric values
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)) or not isinstance(z, (int, float)):
        return "Invalid input: non-numeric value"
    
    # Calculate the product
    product = x * y * z
    
    # Check for zero
    if product == 0:
        return 0
    
    # Convert the product to a string
    product_str = str(product)
    
    # Calculate the sum of the digits
    sum_of_digits = sum(int(digit) for digit in product_str if digit.isdigit())
    
    return sum_of_digits