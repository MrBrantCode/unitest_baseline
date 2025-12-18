"""
QUESTION:
Create a function named `generate_walks` that takes two lists, `animals` and `walks`, as input and returns a list of unique words in alphabetical order, where each word is a combination of an animal name and a type of walk, separated by a hyphen. The function should not take any other input and should not have any side effects.
"""

def generate_walks(animals, walks):
    """
    Generate a list of unique words in alphabetical order, where each word is a combination of an animal name and a type of walk, separated by a hyphen.

    Args:
        animals (list): A list of animal names.
        walks (list): A list of types of walks.

    Returns:
        list: A list of unique words in alphabetical order.
    """
    words = [animal + "-" + walk for animal in animals for walk in walks]
    return sorted(words)