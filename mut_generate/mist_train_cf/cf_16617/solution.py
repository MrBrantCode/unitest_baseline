"""
QUESTION:
Create a function named `compute_sum` that takes two strings representing decimal numbers as input. The function must convert the input strings to decimal numbers, check if they are within the range of -100 to 100, compute their sum using a recursive approach with a time complexity of O(n) where n is the number of digits in the input numbers, and return the sum as a string with a precision of 2 decimal places. The function should not use any additional data structures or recursion stack space, resulting in a space complexity of O(1).
"""

def compute_sum(num1, num2):
    # Convert strings to floats
    num1 = float(num1)
    num2 = float(num2)

    # Check if numbers are within range
    if num1 < -100 or num1 > 100 or num2 < -100 or num2 > 100:
        return "Numbers are not within range."

    # Compute sum using built-in addition
    result = num1 + num2

    # Format the result with 2 decimal places
    result = "{:.2f}".format(result)

    return result