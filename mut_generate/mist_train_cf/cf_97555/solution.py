"""
QUESTION:
Create a function named `make_caipirinha(sweetness_level)` that takes a JSON string as input representing the desired sweetness level, with the JSON format being `{"sweetness_level": x}` where `x` is a value between 1 and 10. The function should calculate the amount of sugar based on the sweetness level and output the recipe with the adjusted amount of sugar. The amount of sugar should be calculated as `(sweetness_level / 10) * 2` and the output recipe should include the adjusted amount of sugar.
"""

import json

def make_caipirinha(sweetness_level):
    # Load the sweetness level from the JSON data
    sweetness_data = json.loads(sweetness_level)
    sweetness_level = sweetness_data["sweetness_level"]
 
    # Calculate the amount of sugar based on the sweetness level
    sugar = (sweetness_level / 10) * 2
 
    # Return the recipe with the adjusted amount of sugar
    return f"To make a caipirinha with a sweetness level of {sweetness_level}\nYou will need:\n- 2 oz cachaça\n- 1 lime, cut into wedges\n- {sugar}oz sugar\n- ice\nDirections:\n1. Place the lime wedges and sugar in a glass.\n2. Muddle the lime and sugar together.\n3. Fill the glass with ice.\n4. Add the cachaça.\n5. Stir well and enjoy!"