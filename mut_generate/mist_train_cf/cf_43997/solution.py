"""
QUESTION:
Develop a function called `calculate_compound_interest` that takes four parameters: `principal`, `rate`, `time`, and `compounding_frequency`. The function should calculate the compound interest based on the given formula: A = P (1 + r/n)^(nt), where A is the amount of money accumulated after n years, P is the principal amount, r is the annual interest rate (in decimal), n is the number of times that interest is compounded per year, and t is the time the money is invested or borrowed for, in years. The function should return the compound interest. 

Note: The `rate` is given in percentage and should be converted to decimal before calculation.
"""

def calculate_compound_interest(principal, rate, time, compounding_frequency):
    # Convert rate from percentage to a proportion
    rate = rate / 100
    
    # Calculate compound interest
    amount = principal * (1 + rate/compounding_frequency) ** (compounding_frequency * time)
    compound_interest = amount - principal
    
    return compound_interest