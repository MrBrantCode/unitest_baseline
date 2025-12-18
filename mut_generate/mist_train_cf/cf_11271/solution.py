"""
QUESTION:
Create a function `create_fruit_characteristics` that takes a list of fruit names as input and returns a dictionary where each key is a fruit name and its corresponding value is another dictionary containing the characteristics of that fruit, including 'color', 'taste', and 'size'. The function should be able to handle a list of fruit names, including but not limited to "Apple", "Orange", "Grapes", "Bananas", and "Watermelons".
"""

def create_fruit_characteristics(fruits):
    """
    This function takes a list of fruit names and returns a dictionary where each key is a fruit name 
    and its corresponding value is another dictionary containing the characteristics of that fruit.

    Args:
        fruits (list): A list of fruit names.

    Returns:
        dict: A dictionary containing fruit names as keys and their characteristics as values.
    """
    fruit_characteristics = {
        "Apple": {"color": "red", "taste": "sweet", "size": "medium"},
        "Orange": {"color": "orange", "taste": "tangy", "size": "medium"},
        "Grapes": {"color": "green/purple", "taste": "sweet", "size": "small"},
        "Bananas": {"color": "yellow", "taste": "sweet", "size": "long"},
        "Watermelons": {"color": "green", "taste": "refreshing", "size": "large"},
    }
    return {fruit: fruit_characteristics[fruit] for fruit in fruits if fruit in fruit_characteristics}