"""
QUESTION:
Calculate the compound interest using the formula A = P(1 + r/n)^(nt), where A is the amount of money accumulated after n years, including interest, P is the principal amount, r is the annual interest rate (in decimal), n is the number of times that interest is compounded per year, and t is the time the money is invested for in years. 

The function should be named `calculate_compound_interest` and should take four parameters: `principal`, `rate`, `time`, and `frequency`. The function should return the compound interest.
"""

def calculate_compound_interest(principal, rate, time, frequency):
    return principal * (1 + (rate / frequency)) ** (time * frequency) - principal