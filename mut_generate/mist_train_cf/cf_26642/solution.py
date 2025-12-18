"""
QUESTION:
Implement a function `count_traits(traits)` that takes a list of traits as input, where each trait is a string, and returns a dictionary containing the frequency of each trait. The function should ignore case sensitivity when counting the frequency of traits.
"""

def count_traits(traits):
    trait_frequency = {}
    for trait in traits:
        trait_lower = trait.lower()  # Convert trait to lowercase for case insensitivity
        if trait_lower in trait_frequency:
            trait_frequency[trait_lower] += 1
        else:
            trait_frequency[trait_lower] = 1
    return trait_frequency