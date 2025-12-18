"""
QUESTION:
Create a function `compound_interest` that calculates the compound interest based on the principal amount, variable interest rates, time period in years, and the number of times interest is applied per year. The interest rates are applied annually but can be computed on different time intervals (e.g., quarterly, monthly). The function should take four parameters: the principal amount, a list of interest rates for each year, the time period in years, and the number of times interest is applied per year. The function should return the total amount after the given time period with the compound interest applied.
"""

def compound_interest(principal, interest_rates, time, times_per_year):
    amount = principal
    for i in range(time):
        amount += amount * (interest_rates[i] / 100) / times_per_year
    return round(amount, 2)