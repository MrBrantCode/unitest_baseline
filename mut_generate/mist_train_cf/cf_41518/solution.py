"""
QUESTION:
Implement a class `AtmosphericInnerProductCalculator` with a method `compute_inner_product(field1, field2, domain)` that calculates the atmospheric inner product for the given atmospheric fields `field1` and `field2` over a specified `domain`. The atmospheric fields are represented as 2D arrays of numerical values, and the `domain` is a tuple of the form `(x_min, x_max, y_min, y_max)` representing the minimum and maximum bounds of the domain in the x and y directions.
"""

def compute_inner_product(field1, field2, domain):
    x_min, x_max, y_min, y_max = domain
    inner_product = 0
    for i in range(len(field1)):
        for j in range(len(field1[0])):
            if x_min <= i < x_max and y_min <= j < y_max:
                inner_product += field1[i][j] * field2[i][j]
    return inner_product