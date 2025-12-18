"""
QUESTION:
Implement a function `polynomial_operations(poly1, poly2)` that takes two polynomials as input, each represented as a list of coefficients where the index of the coefficient corresponds to the power of the variable, and returns a tuple of two lists: the result of adding the two polynomials and the result of multiplying the two polynomials. The returned lists should represent the coefficients of the resulting polynomials.
"""

def add_and_multiply_polynomials(poly1, poly2):
    add_result = []
    mul_result = [0] * (len(poly1) + len(poly2) - 1)

    for i in range(max(len(poly1), len(poly2))):
        coeff1 = poly1[i] if i < len(poly1) else 0
        coeff2 = poly2[i] if i < len(poly2) else 0
        add_result.append(coeff1 + coeff2)

    for i in range(len(poly1)):
        for j in range(len(poly2)):
            mul_result[i + j] += poly1[i] * poly2[j]

    return add_result, mul_result