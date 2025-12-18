"""
QUESTION:
Write a function `classify_fruit` that takes a fruit name and a JSON data structure containing fruit classifications as input and returns a string describing the fruit's type and color. The JSON data structure should map fruit names to objects containing "type" and "color" properties. The function should be adaptable to changes in the classification criteria by allowing the JSON data structure to be modified.
"""

def classify_fruit(fruit_name, fruits):
    """
    This function classifies a fruit based on its type and color.

    Args:
    fruit_name (str): The name of the fruit to classify.
    fruits (dict): A dictionary containing fruit classifications.

    Returns:
    str: A string describing the fruit's type and color.
    """
    fruit_info = fruits.get(fruit_name)
    if fruit_info:
        return f"{fruit_name} is a {fruit_info['color']} {fruit_info['type']} fruit."
    else:
        return f"Classification for {fruit_name} not found."