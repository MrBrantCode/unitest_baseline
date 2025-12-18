"""
QUESTION:
Write a function `calculate_grains(N)` that calculates the minimum and maximum amounts of each grain type (wheat, barley, millet, oats) that can be used in a mixture of N kg, given their respective weights (3 kg, 2 kg, 4 kg, 1 kg). The function should return two dictionaries: one for the minimum amounts and one for the maximum amounts of each grain type. The amounts should be integers, omitting any fractions.
"""

def calculate_grains(N):
    """
    Calculate the minimum and maximum amounts of each grain type 
    (wheat, barley, millet, oats) that can be used in a mixture of N kg, 
    given their respective weights (3 kg, 2 kg, 4 kg, 1 kg).

    Args:
        N (int): Total weight of the mixture in kg.

    Returns:
        tuple: Two dictionaries, one for the minimum amounts and one for the maximum amounts of each grain type.
    """

    grain_types = ['wheat', 'barley', 'millet', 'oats']
    weights = [3, 2, 4, 1]
    grain_dict = dict(zip(grain_types, weights))

    min_amounts = {}
    max_amounts = {}

    for grain in grain_dict:
        min_amounts[grain] = N // sum(weights)
        max_amounts[grain] = N // grain_dict[grain]

    return min_amounts, max_amounts