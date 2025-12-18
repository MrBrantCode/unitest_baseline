"""
QUESTION:
Create a function named `calculate_compound_interest(principal, rate, time, n)` that calculates the final amount after a given period of time with compound interest. The function should take four parameters: `principal` (initial deposit amount), `rate` (annual interest rate in percentage), `time` (duration of time in years), and `n` (number of times interest applied per time period). Implement a program that allows the user to input different initial deposit amounts, interest rates, compound frequencies, and duration of time in years for two banks, then determines which bank offers a better return. The program should include error checking to ensure valid inputs (i.e., principal, rate, time, and n should be greater than 0).
"""

def calculate_compound_interest(principal, rate, time, n):
    # convert rate from percentage to a decimal
    rate = rate / 100
              
    # calculate compound interest using the formula
    A = principal * (1 + rate/n)**(time*n)
              
    return round(A, 2)