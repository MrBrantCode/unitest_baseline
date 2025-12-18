"""
QUESTION:
Create a function `calculate_net_earnings` that takes two arguments: `gross_earnings` and `deductions`. The function should validate the inputs to ensure they are positive numbers. It should then calculate the net earnings by applying a tax rate based on the gross earnings after deductions, where the tax rates are 0% for earnings below $10,000, 10% for earnings between $10,000 and $20,000, 15% for earnings between $20,000 and $30,000, and 25% for earnings above $30,000. The function should return the net earnings, rounded to two decimal places.
"""

def calculate_net_earnings(gross_earnings, deductions):
    # Validate inputs
    try:
        gross_earnings = float(gross_earnings)
        deductions = float(deductions)

        if gross_earnings < 0 or deductions < 0:
            return "Error: All inputs must be positive numbers"

    except ValueError:
        return "Error: All inputs must be numbers"

    # Calculate earnings after deductions
    earnings_after_deductions = gross_earnings - deductions

    # Calculate tax based on earnings after deductions
    if earnings_after_deductions < 10000:
        tax = 0
    elif earnings_after_deductions < 20000:
        tax = earnings_after_deductions * 0.1
    elif earnings_after_deductions < 30000:
        tax = earnings_after_deductions * 0.15
    else:
        tax = earnings_after_deductions * 0.25

    # Calculate and return net earnings, rounded off
    net_earnings = earnings_after_deductions - tax
    return round(net_earnings, 2)