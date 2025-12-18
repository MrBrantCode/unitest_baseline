"""
QUESTION:
Write a function compound_interest that calculates compound interest. The function should take four parameters: principle (initial amount of money), rate (annual interest rate), time (time the money is invested for), and n (number of times interest is compounded per year). n should default to 1 if not supplied. The function should return the calculated compound interest.
"""

def compound_interest(principle, rate=5, time=5, n=1):
   ci = principle * (pow((1 + rate / (n*100)), n*time)) - principle
   return ci