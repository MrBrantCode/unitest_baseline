"""
QUESTION:
Write a function `compound_interest` that calculates the compound interest with monthly contributions. The function should accept five parameters: the initial principal, the annual interest rate as a percentage, time in years, the number of contributions per year, and the amount contributed each period. The function should return the total amount after the given period, considering the interest rate is compounded at the frequency of contributions.
"""

def compound_interest(principal, rate, time, contributions_per_year, contribution_amount):
    rate_per_time = rate / (contributions_per_year * 100)

    total_amount = principal
    for i in range(int(time*contributions_per_year)):
        total_amount = (total_amount + contribution_amount) * (1 + rate_per_time)
    
    return total_amount