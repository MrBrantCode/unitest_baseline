"""
QUESTION:
Create a function `calculate_compound_interest` that calculates the compound interest using the formula A = P(1 + r/n)^(nt), where A is the total amount after compound interest, P is the principal, r is the rate of interest, n is the number of times the interest is compounded per time period, and t is the number of time periods. The function should accept the principal, rate of interest, number of times compounded, and time in years as parameters and return the total amount.
"""

def calculate_compound_interest(principal, rate_of_interest, number_of_times_compounded, time_in_years):
    total = principal * (1 + (rate_of_interest / number_of_times_compounded)) ** (number_of_times_compounded * time_in_years)
    return total