"""
QUESTION:
Create a function named `get_fruit_classification` that takes a fruit name and a dictionary of fruits with their respective types and colors as input. The function should return a string describing the fruit's classification based on its type and color. 

The dictionary of fruits should have the fruit name as the key and a dictionary containing the fruit's type and color as the value. The fruit type can be either 'citrus' or 'non-citrus' and the fruit color can be 'red', 'green', or 'yellow'.
"""

def get_fruit_classification(fruit_name, fruits):
    """
    This function returns a string describing the fruit's classification based on its type and color.

    Parameters:
    fruit_name (str): The name of the fruit.
    fruits (dict): A dictionary of fruits with their respective types and colors.

    Returns:
    str: A string describing the fruit's classification.
    """
    fruit_type = fruits[fruit_name]["type"]
    fruit_color = fruits[fruit_name]["color"]
    return f"{fruit_name} is a {fruit_color} {fruit_type} fruit."