"""
QUESTION:
Create a function named `calculate_total` that takes four numerical parameters: `num1`, `num2`, `num3`, and `increase`. The function should calculate the sum of `num1`, `num2`, and `num3`, then increase the result by the value of `increase` and return the final total.
"""

def calculate_total(num1, num2, num3, increase):
    """Calculate the combined total of three numbers and increase the result."""
    total = num1 + num2 + num3
    return total + increase