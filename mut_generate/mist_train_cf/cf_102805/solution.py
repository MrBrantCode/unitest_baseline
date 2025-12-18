"""
QUESTION:
Create a function "percentage" that calculates the percentage by dividing the amount by the total and multiplying by 100. The function should handle the following cases:
- If the amount is equal to 0, return 0 as the percentage.
- If the total is equal to 0, return "Error: Division by zero is not allowed."
- If the amount is negative, return "Error: Amount cannot be negative."
- If the total is negative, return "Error: Total cannot be negative."
- If the amount is greater than the total, return "Error: Amount cannot be greater than the total."

The function should take two parameters: amount and total, both integers.
"""

def percentage(amount, total):
    if amount == 0:
        return '0%'
    elif total == 0:
        return 'Error: Division by zero is not allowed.'
    elif amount < 0:
        return 'Error: Amount cannot be negative.'
    elif total < 0:
        return 'Error: Total cannot be negative.'
    elif amount > total:
        return 'Error: Amount cannot be greater than the total.'
    else:
        percentage = (amount / total) * 100
        return str(int(percentage)) + '%'