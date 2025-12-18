"""
QUESTION:
Create a function `make_caipirinha(sweetness_level)` that takes a JSON string `sweetness_level` as input, where the JSON string contains a "sweetness_level" key with a value between 1 and 10. The function should adjust the amount of sugar in the caipirinha recipe based on the provided sweetness level. The amount of sugar should be calculated by dividing the sweetness level by 10 and multiplying it by 2. The function should then output the caipirinha recipe with the adjusted amount of sugar.
"""

import json
def make_caipirinha(sweetness_level):
    sweetness_data = json.loads(sweetness_level)
    sweetness_level = sweetness_data["sweetness_level"]
    sugar = (sweetness_level / 10) * 2
    return "To make a caipirinha with a sweetness level of " + str(sweetness_level) + "\nYou will need:\n- 2 oz cachaça\n- 1 lime, cut into wedges\n- " + str(sugar) + "oz sugar\n- ice\nDirections:\n1. Place the lime wedges and sugar in a glass.\n2. Muddle the lime and sugar together.\n3. Fill the glass with ice.\n4. Add the cachaça.\n5. Stir well and enjoy!"