"""
QUESTION:
Write a function `extract_fruit_classification` that takes a fruit name and a JSON object of fruit classifications as input. The JSON object contains the fruit name as the key and another JSON object with "type" and "color" as values. The function should return a string that includes the fruit name and its classification, e.g., "Apricot is a yellow non-citrus fruit." The function should be adaptable to changes in the criteria for classification by simply updating the JSON data structure.
"""

import json

def extract_fruit_classification(fruit_name, fruit_classifications):
    """
    Extract the classification of a fruit based on its type and color from a JSON data structure.
    
    Args:
        fruit_name (str): The name of the fruit to extract the classification for.
        fruit_classifications (dict): A dictionary containing fruit names as keys and dictionaries with "type" and "color" as values.
    
    Returns:
        str: A string that includes the fruit name and its classification.
    """
    if fruit_name in fruit_classifications:
        fruit_type = fruit_classifications[fruit_name]["type"]
        fruit_color = fruit_classifications[fruit_name]["color"]
        return f"{fruit_name} is a {fruit_color} {fruit_type} fruit."
    else:
        return f"Classification not found for {fruit_name}"