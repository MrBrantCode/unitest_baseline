"""
QUESTION:
Create a function `group_pets` that takes a list of strings as input, where each string contains the owner's name, the number of pets, and the type of pet. The function should return a dictionary where the keys are the owner's names and the values are sub-dictionaries containing the type and number of pet animals owned. The function should be able to handle cases where an owner has multiple types of pets and cases where an owner has multiple pets of the same type.
"""

def group_pets(pets):
    pets_dict = {}
    for pet in pets:
        owner, number, type = pet.split()
        number = int(number)
        if owner in pets_dict:
            if type in pets_dict[owner]:
                pets_dict[owner][type] += number
            else:
                pets_dict[owner][type] = number
        else:
            pets_dict[owner] = {type: number}
    return pets_dict