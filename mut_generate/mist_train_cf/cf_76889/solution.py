"""
QUESTION:
Create a function called `calculate_interest` that calculates the total amount after adding the interest to the principal amount. The function should take three parameters: the principal amount, the rate of interest (in decimal), and the time period for which the interest is calculated.
"""

def calculate_interest(principal, rate_of_interest, time_period):
    total = principal + (principal * rate_of_interest * time_period)
    return total