"""
QUESTION:
Write a function called `calculate_difference` that takes four parameters: `samantha_cards`, `perry_cards`, and `cards_transferred`. The function should calculate and return the difference in the number of baseball cards between Samantha and Perry after Samantha gives Perry a certain number of cards. The initial number of cards Samantha and Perry have are `samantha_cards` and `perry_cards`, respectively. The number of cards Samantha gives to Perry is `cards_transferred`.
"""

def calculate_difference(samantha_cards, perry_cards, cards_transferred):
    samantha_end = samantha_cards - cards_transferred
    perry_end = perry_cards + cards_transferred
    difference = samantha_end - perry_end
    return difference