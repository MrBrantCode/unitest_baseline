"""
QUESTION:
Implement the function `filter_animals` that takes a list of animal names as input and returns a new list containing only the names of animals that meet the following conditions: 
- the name contains the letter 'o'
- the name does not contain the letter 'a'
- the name does not end in the letter 'e'
"""

def filter_animals(animals):
    """Filter animal names containing 'o', excluding 'a' and not ending in 'e'"""
    return [animal for animal in animals if 'o' in animal and 'a' not in animal and not animal.endswith('e')]