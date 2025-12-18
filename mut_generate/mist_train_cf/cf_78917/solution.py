"""
QUESTION:
Create a function called `generate_haiku` that takes a character's name and a list of traits as input, and returns a list of 10 haikus where each haiku reveals one trait of the character. The haiku structure should be a three-line poem with the first line containing the character's name and the trait, the second line being "Paths of life he does tread," and the third line being "A soul story spreads."
"""

def generate_haiku(name, traits):
    """
    Generates a list of haikus where each haiku reveals one trait of the character.
    
    Args:
    name (str): The character's name.
    traits (list): A list of traits of the character.
    
    Returns:
    list: A list of haikus.
    """
    haikus = []
    for trait in traits:
        haiku = f'{name}, {trait},\nPaths of life he does tread,\nA soul story spreads.'
        haikus.append(haiku)
    return haikus