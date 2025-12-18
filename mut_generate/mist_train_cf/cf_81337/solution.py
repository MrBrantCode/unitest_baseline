"""
QUESTION:
Create a function `get_semantics(character)` that takes an alphabet character as input and returns its corresponding semantic meaning. The function should be case-insensitive and return "Semantics not found for this character" if the input character is not found. Use a dictionary to store the semantics of alphabet characters.
"""

def get_semantics(character):
    # Define a dictionary with alphabet semantics
    semantics_dict = {
        'a': 'First letter of the English alphabet',
        'b': 'Second letter of the English alphabet',
        # Add more alphabet semantics as needed
    }

    # Look up semantics in the dictionary
    character = character.lower()  # Ensure input is not case sensitive
    return semantics_dict.get(character, "Semantics not found for this character")