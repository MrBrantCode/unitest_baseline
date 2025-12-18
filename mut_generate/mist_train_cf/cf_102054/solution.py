"""
QUESTION:
Create a function "percentage" that takes two integer parameters "amount" and "total" within the range of -100 to 100 (inclusive) and returns the calculated percentage as a string. The function should perform the following checks and return the corresponding error messages:
- If the inputs are not integers, return "Error: The amount and total should be integers."
- If the inputs are out of range, return "Error: The amount and total should be within the range of -100 to 100 (inclusive)."
- If the amount is 0, return "0%".
- If the total is 0, return "Error: Division by zero is not allowed."
- If the amount is negative, return "Error: Amount cannot be negative."
- If the total is negative, return "Error: Total cannot be negative."
- If the amount is greater than the total, return "Error: Amount cannot be greater than the total."
Otherwise, return the calculated percentage as a string in the format "X%" where X is the calculated percentage.
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