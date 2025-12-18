"""
QUESTION:
Create a function "percentage" that calculates the percentage of the given amount relative to the total. The function should take two parameters: amount and total, both of which should be integers within the range of -100 to 100 (inclusive).

The function should return the calculated percentage as a string followed by "%". If the amount is equal to 0, the function should return "0%". However, it should handle the following error cases:

- If the total is equal to 0, return "Error: Division by zero is not allowed."
- If the amount is negative, return "Error: Amount cannot be negative."
- If the total is negative, return "Error: Total cannot be negative."
- If the amount is greater than the total, return "Error: Amount cannot be greater than the total."
- If either amount or total is not an integer, return "Error: The amount and total should be integers."
- If either amount or total is outside the range of -100 to 100 (inclusive), return "Error: The amount and total should be within the range of -100 to 100 (inclusive)."
"""

def percentage(amount, total):
    if not isinstance(amount, int) or not isinstance(total, int):
        return "Error: The amount and total should be integers."
    if amount < -100 or amount > 100 or total < -100 or total > 100:
        return "Error: The amount and total should be within the range of -100 to 100 (inclusive)."
    if amount == 0:
        return "0%"
    if total == 0:
        return "Error: Division by zero is not allowed."
    if amount < 0:
        return "Error: Amount cannot be negative."
    if total < 0:
        return "Error: Total cannot be negative."
    if amount > total:
        return "Error: Amount cannot be greater than the total."
    
    percentage = (amount / total) * 100
    return str(percentage) + "%"