"""
QUESTION:
Create a function named `classify_fruit` that takes a fruit name and a dictionary of fruit classifications as input. The dictionary should be in the format where each key is a fruit name and each value is another dictionary containing the keys 'type' (either 'citrus' or 'non-citrus') and 'color' (either 'red', 'green', or 'yellow'). The function should return a string describing the fruit's classification in the format "Fruit name is a {color} {type} fruit."
"""

def classify_fruit(fruit_name, fruit_classifications):
    """
    Classify a fruit based on its type and color.

    Args:
        fruit_name (str): The name of the fruit to classify.
        fruit_classifications (dict): A dictionary containing fruit classifications.

    Returns:
        str: A string describing the fruit's classification.
    """
    fruit_type = fruit_classifications.get(fruit_name, {}).get('type', '')
    fruit_color = fruit_classifications.get(fruit_name, {}).get('color', '')
    return f"{fruit_name} is a {fruit_color} {fruit_type} fruit."