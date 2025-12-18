"""
QUESTION:
Create a function `multiply(poly1, poly2)` to find the product of two polynomials represented as lists, where each element in the list corresponds to a coefficient of the polynomial in descending order of powers. The function should return a new list representing the coefficients of the resulting polynomial. The input lists `poly1` and `poly2` may have varying lengths.
"""

def multiply(poly1, poly2):
    m = len(poly1)
    n = len(poly2)
    product = [0] * (m + n - 1)
    
    for i in range(m):
        for j in range(n):
            product[i + j] += poly1[i] * poly2[j]
    
    return product