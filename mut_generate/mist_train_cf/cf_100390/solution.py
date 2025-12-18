"""
QUESTION:
Create a function `recommend_accessories(color, size, print_design)` that takes in a t-shirt's color, size, and print design, and returns a list of recommended accessories based on these characteristics. The function should use a dictionary to map t-shirt characteristics to recommended accessories.
"""

def recommend_accessories(color, size, print_design):
    accessories = {
        ("Red", "Large", "Stripes"): ["Black Fedora", "Gold Watch", "Black Leather Belt"]
    }
    return accessories.get((color, size, print_design), [])