"""
QUESTION:
Write a function `calculate_matches` that takes three parameters: `min_match`, `factor`, and `num_shapes`, representing the minimum number of matches required for the first shape, the factor by which the number of matches needed for each subsequent shape is multiplied, and the number of shapes to be formed, respectively. The function should return the total number of matches required to form the given number of shapes. The number of matches required for each subsequent shape is calculated by multiplying the number of matches needed for the previous shape by the factor.
"""

def calculate_matches(min_match, factor, num_shapes):
    total_matches = 0
    matches = min_match
    for _ in range(num_shapes):
        total_matches += matches
        matches *= factor
    return total_matches