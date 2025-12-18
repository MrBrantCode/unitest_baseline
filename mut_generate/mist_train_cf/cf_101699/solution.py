"""
QUESTION:
Write a function `filter_animals` that takes a list of animal names as input and returns a new list containing only the names that meet the following conditions: 
- The name contains the letter 'o'.
- The name does not contain the letter 'a'.
- The name does not end with the letter 'e'.
"""

def filter_animals(animals):
    return [animal for animal in animals if 'o' in animal and 'a' not in animal and not animal.endswith('e')]