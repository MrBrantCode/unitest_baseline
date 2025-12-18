"""
QUESTION:
Create a function named `calculate_total_amount` that takes three parameters: `initial_amount`, `rate_of_interest`, and `years`, and returns the total amount of money after the specified number of years, rounded to 2 decimal places. The rate of interest should be divided by 100 to get the actual decimal value, and compound interest should be calculated annually.
"""

def calculate_total_amount(initial_amount: float, rate_of_interest: float, years: int) -> float:
    # Convert the rate of interest from percentage to decimal
    rate_of_interest = rate_of_interest / 100

    # Calculate the total amount using the formula for compound interest
    total_amount = initial_amount * (1 + rate_of_interest) ** years

    # Round the total amount to 2 decimal places
    total_amount = round(total_amount, 2)

    return total_amount