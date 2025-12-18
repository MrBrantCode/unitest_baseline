"""
QUESTION:
Write a function named `calculate_sum_of_digits` that takes three numbers as input. The function should return the sum of the digits of the product of the three numbers, handling negative numbers, zeros, large input numbers up to 10^9, floating-point input numbers, non-numeric input, and empty input. If any input is empty, return "Invalid input: empty value". If any input is non-numeric, return "Invalid input: non-numeric value".
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