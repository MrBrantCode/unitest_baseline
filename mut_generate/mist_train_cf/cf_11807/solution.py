"""
QUESTION:
Write a function `calculate_compound_interest` that takes four parameters: `principal_amount`, `interest_rate`, `num_years`, and `compounded_per_year`, and returns the final amount after `num_years` years, considering compound interest. The function should use the formula A = P(1 + r/n)^(n*t), where A is the final amount, P is the principal amount, r is the rate of interest, n is the number of times interest is compounded per year, and t is the number of years. Assume all inputs will be valid and within a reasonable range.
"""

def calculate_compound_interest(principal_amount, interest_rate, num_years, compounded_per_year):
    A = principal_amount * (1 + interest_rate / compounded_per_year) ** (compounded_per_year * num_years)
    return A