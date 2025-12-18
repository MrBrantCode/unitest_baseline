"""
QUESTION:
Create a data object with the following structure: it should have 'category' and 'identification' as nested dictionaries and 'age' at the top level. The 'category' dictionary should have a 'type' key with a dictionary value containing an 'animal' key, and the 'identification' dictionary should have a 'name' key with a dictionary value containing a 'pet' key.
"""

def create_data_object(animal, pet, age):
    """
    Creates a nested dictionary data object with 'category', 'identification', and 'age'.

    Args:
    animal (str): The type of animal.
    pet (str): The name of the pet.
    age (int): The age of the pet.

    Returns:
    dict: A nested dictionary data object.
    """
    return {
        'category': {
            'type': {
                'animal': animal
            }
        },
        'identification': {
            'name': {
                'pet': pet
            }
        },
        'age': age
    }