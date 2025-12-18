"""
QUESTION:
Create a function named `categorize_fruit` that takes a dictionary representing a fruit with 'color' and 'texture' as keys and returns the species of the fruit. The function should be able to categorize fruits into 'Mangifera indica' (Mango) and 'Malus domestica' (Apple) based on their color and texture. The function should return 'Unknown fruit' for any fruit that does not match the specified characteristics of Mango or Apple.
"""

def categorize_fruit(fruit):
    """Function that determines the type of fruit based on its traits."""
    if fruit["color"] == "yellow" and fruit["texture"] == "smooth":
        return "Mangifera indica" 
    elif fruit["color"] == "red" and fruit["texture"] == "smooth":
        return "Malus domestica" 
    else:
        return "Unknown fruit"