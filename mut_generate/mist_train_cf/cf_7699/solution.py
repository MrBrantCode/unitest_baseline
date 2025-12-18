"""
QUESTION:
Create a function named `calculate_total_amount` that calculates the total amount of money after a specified number of years. The function should take five parameters: `initial_amount`, `rate_of_interest`, `years`, `yearly_deposit`, and `max_deposit`. The `rate_of_interest` is a percentage value that should be converted to a decimal for calculations. The function should account for compound interest, which is calculated annually, and limit the yearly deposit to the maximum deposit amount. The yearly deposit is added to the initial amount at the beginning of each year. The function should return the total amount of money after the specified number of years, rounded to 2 decimal places.
"""

def calculate_total_amount(initial_amount: float, rate_of_interest: float, years: int, yearly_deposit: float, max_deposit: float) -> float:
    total_amount = initial_amount
    interest_rate = rate_of_interest / 100

    for _ in range(years):
        if yearly_deposit > max_deposit:
            yearly_deposit = max_deposit
        total_amount += yearly_deposit
        total_amount *= (1 + interest_rate)

    return round(total_amount, 2)