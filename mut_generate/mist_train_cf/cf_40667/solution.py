"""
QUESTION:
Create a function `sortFractions(fractions)` where `fractions` is a list of strings representing valid fractions in the format "numerator/denominator". The function should return a list of strings representing the sorted fractions in ascending order based on their decimal values.
"""

def entrance(fractions):
    def fraction_key(fraction):
        numerator, denominator = map(int, fraction.split('/'))
        return numerator / denominator  

    sorted_fractions = sorted(fractions, key=fraction_key)
    return sorted_fractions