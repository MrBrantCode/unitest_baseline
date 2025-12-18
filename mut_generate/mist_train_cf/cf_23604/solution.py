"""
QUESTION:
Create a function named `years_months_days` that takes an integer number of days as input and returns a tuple of three integers representing the equivalent number of years, months, and remaining days. Assume a non-leap year (365 days) and a month with 30 days for simplicity.
"""

def years_months_days(days):
    years = int(days // 365)
    months = int((days % 365) // 30)
    days = int((days % 365) % 30)
 
    return (years, months, days)