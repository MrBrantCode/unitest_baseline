"""
QUESTION:
Create a function named `correct_dict` that takes a dictionary as input. The dictionary maps fruits to their quantities, but some quantities may be strings instead of integers due to an error. The function should iterate over the dictionary, convert string quantities to integers where possible, and set them to 0 if the conversion is not possible. The function should return the corrected dictionary. The input dictionary may contain a mix of string and integer values.
"""

def correct_dict(fruit_dict):
    for key in fruit_dict:
        try:
            fruit_dict[key] = int(fruit_dict[key])
        except ValueError:
            fruit_dict[key] = 0
    return fruit_dict