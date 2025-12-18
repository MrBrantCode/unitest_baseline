"""
QUESTION:
Implement a function `filter_animals` that takes a list of animal names as input and returns a filtered list containing only the names that meet the following conditions:

- The name contains the letter 'o'.
- The name does not contain the letter 'a'.
- The name does not end with the letter 'e'.

The function should be able to handle a list of any size.
"""

def filter_animals(animals):
    """
    Filters a list of animal names based on the following conditions:
    - The name contains the letter 'o'.
    - The name does not contain the letter 'a'.
    - The name does not end with the letter 'e'.

    Args:
        animals (list): A list of animal names.

    Returns:
        list: A filtered list of animal names meeting the specified conditions.
    """
    return [animal for animal in animals if 'o' in animal and 'a' not in animal and not animal.endswith('e')]