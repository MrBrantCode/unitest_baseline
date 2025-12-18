"""
QUESTION:
Write a function `calculate_departure_product(field_pos, my_ticket)` that calculates the product of the values in the "my ticket" for the fields that start with "departure".

The function takes two parameters:
- `field_pos` (dict): A dictionary where each key is a field name and the value is a list of possible positions for that field.
- `my_ticket` (list): A list representing your personal ticket information.

The function should return the product of the values in the "my ticket" for the fields that start with "departure".
"""

def calculate_departure_product(field_pos, my_ticket):
    product = 1
    for field, positions in field_pos.items():
        if field.startswith("departure"):
            product *= my_ticket[positions[0]]
    return product