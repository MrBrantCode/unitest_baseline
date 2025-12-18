"""
QUESTION:
Write a function named `calculate_sum` that takes in three parameters: `base_sum`, `interest_rates`, and `contributions`. The function should calculate the accumulated sum after 5 years, considering compound interest and annual contributions. The `interest_rates` and `contributions` parameters should be lists of 5 elements each, representing the interest rate and contribution for each year, respectively. The interest rates should be decimal fractions (e.g., 2% interest rate is 0.02). The function should return the accumulated sum after 5 years.
"""

def calculate_sum(base_sum, interest_rates, contributions):
    total = base_sum
    for i in range(5):
        total = (total + contributions[i]) * (1 + interest_rates[i])
    return total