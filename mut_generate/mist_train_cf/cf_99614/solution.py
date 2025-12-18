"""
QUESTION:
Create a function named `generate_animal_walks` that takes two lists, `animals` and `walks`, as input and returns a sorted list of unique words in the structure "animal-walk". The input lists `animals` and `walks` contain strings representing animal names and types of walks respectively. The output list should be in alphabetical order.
"""

def generate_animal_walks(animals, walks):
    """
    Generate a sorted list of unique words in the structure "animal-walk".
    
    Args:
        animals (list): A list of strings representing animal names.
        walks (list): A list of strings representing types of walks.
    
    Returns:
        list: A sorted list of unique words in the structure "animal-walk".
    """
    words = [f"{animal}-{walk}" for animal in animals for walk in walks]
    return sorted(set(words))