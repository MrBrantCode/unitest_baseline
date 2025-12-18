"""
QUESTION:
Create a function named `recommend_accessories` that takes three arguments: `color`, `size`, and `print_design`. The function should return a list of recommended accessories based on the given t-shirt characteristics. The function should use a dictionary that maps t-shirt characteristics to recommended accessories. The dictionary should have tuples of `color`, `size`, and `print_design` as keys and lists of accessories as values.
"""

def recommend_accessories(color, size, print_design):
    accessories = {
        ("Red", "Large", "Stripes"): ["Black Fedora", "Gold Watch", "Black Leather Belt"]
        # Add more t-shirt characteristics and accessories here
    }
    return accessories.get((color, size, print_design), [])