"""
QUESTION:
Create a function `filterFruitsByColor` that takes two lists, `fruits` and `colors`, as input. The function should return a list of dictionaries, where each dictionary contains a key-value pair representing a fruit and its corresponding color, but only if the color starts with a vowel. The key in each dictionary should be the fruit name and the value should be its corresponding color.
"""

def filterFruitsByColor(fruits, colors):
    """
    This function filters fruits by their corresponding colors and returns a list of dictionaries.
    Each dictionary contains a key-value pair representing a fruit and its color, 
    but only if the color starts with a vowel.

    Args:
        fruits (list): A list of fruit names.
        colors (list): A list of colors corresponding to the fruits.

    Returns:
        list: A list of dictionaries, where each dictionary contains a fruit-color pair.
    """
    vowels = 'aeiou'
    return [{fruit: color} for fruit, color in zip(fruits, colors) if color[0].lower() in vowels]