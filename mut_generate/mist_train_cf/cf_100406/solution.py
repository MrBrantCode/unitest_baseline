"""
QUESTION:
Create a function named `generate_walks` that takes two lists of strings, `animals` and `walks`, as input. The function should return a list of strings where each string is a combination of an animal name from the `animals` list and a type of walk from the `walks` list, separated by a hyphen. The returned list should be in alphabetical order and contain no duplicates.
"""

def generate_walks(animals, walks):
    """
    Generate a list of strings where each string is a combination of an animal name 
    from the animals list and a type of walk from the walks list, separated by a hyphen.
    
    Args:
        animals (list): A list of animal names
        walks (list): A list of walk types
        
    Returns:
        list: A list of strings, each representing an animal-walk combination
    """
    return sorted(list(set(f"{animal}-{walk}" for animal in animals for walk in walks)))