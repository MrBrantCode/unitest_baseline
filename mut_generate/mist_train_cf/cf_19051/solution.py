"""
QUESTION:
Write a function compound_interest that calculates the total compound interest earned on a principal amount over a given time period with additional contributions at regular intervals and compounding interest at the specified frequency. The function should take five parameters: the principal amount, the annual interest rate as a decimal, the time period in years, the frequency of contributions (e.g. monthly=12, quarterly=4), and the amount contributed at each interval. The function should return the total compound interest earned over the given time period, taking into account both the initial principal amount and the additional contributions. Assume that the interest is compounded at the specified frequency and the contributions are made at the end of each interval.
"""

def compound_interest(principal, rate, time_period, contribution_frequency, contribution_amount):
    total_interest = 0
    
    # Calculate the interest for each contribution period
    for i in range(time_period * contribution_frequency):
        # Calculate the interest for the principal amount
        interest = principal * (rate / contribution_frequency)
        total_interest += interest
        
        # Add the contribution amount to the principal
        principal += contribution_amount
    
    return total_interest