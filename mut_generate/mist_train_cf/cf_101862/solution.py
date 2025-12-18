"""
QUESTION:
Create a function called `add_item` to store a list of fruits and vegetables in a dictionary where the keys are the names of the items and the values are tuples containing their nutritional properties: whether it is a fruit or vegetable, its taste profile, its primary nutritional benefit, and its calorie content. The function should be able to add items to the dictionary. Provide a way to retrieve an item from the dictionary. The dictionary should be initialized with the following items: 
"apple" with ("fruit", "sweet", "high in fiber", "low in calories"), 
"broccoli" with ("vegetable", "bitter", "high in fiber", "low in calories"), 
"carrot" with ("vegetable", "sweet", "high in vitamin A", "low in calories"), 
"banana" with ("fruit", "sweet", "high in potassium", "moderate in calories"), 
and "spinach" with ("vegetable", "bitter", "high in iron", "low in calories").
"""

def add_item(fruits_and_veggies, name, item_type, taste, nutritional_benefit, calorie_content):
    """
    Adds an item to the dictionary of fruits and vegetables.

    Args:
        fruits_and_veggies (dict): The dictionary of fruits and vegetables.
        name (str): The name of the item.
        item_type (str): Whether the item is a fruit or vegetable.
        taste (str): The taste profile of the item.
        nutritional_benefit (str): The primary nutritional benefit of the item.
        calorie_content (str): The calorie content of the item.

    Returns:
        dict: The updated dictionary of fruits and vegetables.
    """
    fruits_and_veggies[name] = (item_type, taste, nutritional_benefit, calorie_content)
    return fruits_and_veggies

# Example usage:
fruits_and_veggies = {
    "apple": ("fruit", "sweet", "high in fiber", "low in calories"),
    "broccoli": ("vegetable", "bitter", "high in fiber", "low in calories"),
    "carrot": ("vegetable", "sweet", "high in vitamin A", "low in calories"),
    "banana": ("fruit", "sweet", "high in potassium", "moderate in calories"),
    "spinach": ("vegetable", "bitter", "high in iron", "low in calories")
}

fruits_and_veggies = add_item(fruits_and_veggies, "grape", "fruit", "sweet", "high in antioxidants", "moderate in calories")
print(fruits_and_veggies["grape"])  # Output: ("fruit", "sweet", "high in antioxidants", "moderate in calories")