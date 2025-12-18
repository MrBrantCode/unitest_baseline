"""
QUESTION:
Write a function `calculate_placeholder` that takes five parameters: `M`, `m`, `n` as integers, and `positive` and `min_inf` as booleans. The function should return the value of `place_holder` based on the following conditions: 
- If `min_inf` is `False`, calculate `place_holder` using the formula: `(M + (n - 1) * (M - m)) + positive`
- If `min_inf` is `True`, calculate `place_holder` using the formula: `(m + (n - 1) * (m - M)) - positive`
"""

def calculate_placeholder(M, m, n, positive, min_inf):
    if not min_inf:
        place_holder = (M + (n - 1) * (M - m)) + positive
    else:
        place_holder = (m + (n - 1) * (m - M)) - positive
    return place_holder