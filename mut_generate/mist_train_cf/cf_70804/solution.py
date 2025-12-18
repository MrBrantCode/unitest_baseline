"""
QUESTION:
Create two functions, `calculate_simple_interest` and `calculate_compounded_interest`, to calculate simple and compounded interest respectively. The `calculate_simple_interest` function should take three parameters: `principal`, `rate`, and `time`, and return the calculated simple interest. The `calculate_compounded_interest` function should take four parameters: `principal`, `rate`, `time`, and `n`, where `n` is the number of times the interest is compounded per year, and return the calculated compounded interest. Assume that the interest rate is an annual rate.
"""

def calculate_simple_interest(principal, rate, time):
    """Calculate simple interest."""
    return (principal * rate * time) / 100

def calculate_compounded_interest(principal, rate, time, n):
    """Calculate compounded interest."""
    amount = principal * (pow((1 + rate / (100*n)), (n*time)))
    return amount - principal