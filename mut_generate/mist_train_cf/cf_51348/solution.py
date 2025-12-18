"""
QUESTION:
Implement a function `calculate_coefficients` that calculates the Pearson Correlation Coefficient (r), Coefficient of Determination (R-squared), and Adjusted R-squared between two numerical datasets using native Python libraries without any statistical modules or libraries. The function should take two lists of numerical values `x1` and `x2` as input, along with the number of data points `n`. The function should handle large datasets efficiently without excessive consumption of computational resources.

The function should check for the validity of the input datasets, ensuring they have the same length and contain at least 4 data points. It should return the calculated coefficients `r`, `r_squared`, and `adj_r_squared` or raise an exception if an error occurs during the calculation.
"""

def calculate_coefficients(x1, x2, n):
    def sum_of_square(xi):
        return sum([i**2 for i in xi])

    def square_of_sum(xi):
        return sum(xi)**2

    def sum_of_product(x1i, x2i):
        return sum([x1i[i]*x2i[i] for i in range(len(x1i))])

    # Pearson Correlation Coefficient (r)
    numerator = n * sum_of_product(x1, x2) - sum(x1) * sum(x2)
    denominator = ((n * sum_of_square(x1) - square_of_sum(x1)) * 
                   (n * sum_of_square(x2) - square_of_sum(x2)))**0.5
    r = numerator / denominator

    # Coefficient of Determination (R-Squared)
    r_squared = r**2

    # Adjusted R-Squared
    adj_r_squared = 1 - (1-r_squared)*(n-1)/(n-2-1)

    return r, r_squared, adj_r_squared