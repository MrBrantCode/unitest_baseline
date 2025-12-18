"""
QUESTION:
Create a function named `filter_animals` that takes a list of animal names as input and returns a filtered list containing only the names that include the letter 'o', exclude the letter 'a', and do not end with the letter 'e'. The function should be able to handle lists of varying sizes.
"""

def filter_animals(animals):
    return [animal for animal in animals if 'o' in animal and 'a' not in animal and not animal.endswith('e')]