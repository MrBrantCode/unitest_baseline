"""
QUESTION:
Create a function `generate_card_image_dict(cards, printings)` that takes two lists as input: `cards` and `printings`. 

The `cards` list contains dictionaries with the keys 'name', 'mana_cost', and 'type_line'. The `printings` list contains dictionaries with the keys 'card', 'image_url', and 'magic_set', where 'card' is a dictionary with a 'name' key.

Return a dictionary where the keys are the card names and the values are lists of image URLs for each printing of the card. If a card has no associated printings, its value should be an empty list.
"""

def generate_card_image_dict(cards, printings):
    card_image_dict = {card['name']: [] for card in cards}
    
    for printing in printings:
        card_name = printing['card']['name']
        if card_name in card_image_dict:
            card_image_dict[card_name].append(printing['image_url'])
    
    return card_image_dict