"""
QUESTION:
Write a Python function `calculate_average_sweetness` that takes a dictionary `fruits` as input, where each key is a fruit and its corresponding value is another dictionary containing 'sweetness' and 'origin'. The function should first sort the fruits by their sweetness in descending order and then group them by their origin countries. Finally, it should calculate the average sweetness of fruits in each country and return the result as a dictionary where keys are country names and values are average sweetness. The input dictionary `fruits` is not empty and all fruits have non-negative sweetness values.
"""

def calculate_average_sweetness(fruits):
    """
    This function calculates the average sweetness of fruits in each country.

    Args:
    fruits (dict): A dictionary containing fruits as keys and their properties (sweetness and origin) as values.

    Returns:
    dict: A dictionary where keys are country names and values are average sweetness.
    """
    
    # Sort the fruits by sweetness in descending order
    sorted_fruits = sorted(fruits.items(), key=lambda x: x[1]["sweetness"], reverse=True)
    
    # Group the fruits by their origin countries
    grouped_fruits = {}
    for fruit, data in sorted_fruits:
        origin = data["origin"]
        if origin not in grouped_fruits:
            grouped_fruits[origin] = []
        grouped_fruits[origin].append((fruit, data["sweetness"]))
    
    # Calculate the average sweetness of fruits in each country
    average_sweetness = {}
    for country, fruits in grouped_fruits.items():
        total_sweetness = 0
        num_fruits = len(fruits)
        for fruit, sweetness in fruits:
            total_sweetness += sweetness
        average_sweetness[country] = total_sweetness / num_fruits
    
    return average_sweetness