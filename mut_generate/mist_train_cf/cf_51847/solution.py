"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given non-negative integer. The function should return `None` and print an error message if the input is not an integer or is negative. The function should be able to handle large inputs without exceeding the maximum recursion depth.
"""

def factorial(num):
    # Check if the number is an integer
    if not isinstance(num, int):
        print("Error: The input is not an integer")
        return None
  
    # Check if the number is negative
    if num < 0:
        print("Error: Factorial is not defined for negative numbers")
        return None

    # Define the base case
    if num == 0 or num == 1:
        return 1

    # Initialize result
    result = 1

    # Calculate factorial iteratively to prevent recursion depth limit
    while num > 1:
        result *= num
        num -= 1

    # Return the factorial of the number
    return result