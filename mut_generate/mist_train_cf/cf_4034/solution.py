"""
QUESTION:
Create a function `add_item` that adds a new item to the end of a given list of fruits if it meets the following conditions: the item is a fruit, its name starts with a consonant, and it contains at least 3 different vowels in its name. The function should print an error message stating the reason why the item cannot be added to the list if any condition is not met. Assume a predefined list of fruits is ["apple", "orange", "cherry"].
"""

def add_item(list_of_items, item):
    """
    Adds a new item to the end of a given list of fruits if it meets the conditions:
    the item is a fruit, its name starts with a consonant, and it contains at least 3 different vowels in its name.

    Args:
        list_of_items (list): A list of fruits.
        item (str): The new item to be added.

    Returns:
        list: The updated list of fruits.
    """

    # Predefined list of fruits
    fruits = ["apple", "orange", "cherry"]

    # Check if the item is a fruit
    if item not in fruits:
        print(f"Item '{item}' does not meet the conditions to be added to the list.")
        print("Reason: The item is not a fruit.")
    # Check if the name starts with a consonant
    elif item[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        print(f"Item '{item}' does not meet the conditions to be added to the list.")
        print("Reason: The name does not start with a consonant.")
    # Check if the name contains at least 3 different vowels
    elif len(set([v for v in item.lower() if v in ['a', 'e', 'i', 'o', 'u']])) < 3:
        print(f"Item '{item}' does not meet the conditions to be added to the list.")
        print("Reason: The name does not contain at least 3 different vowels.")
    else:
        list_of_items.append(item)
        print(f"Item '{item}' has been added to the list.")
        return list_of_items

    return list_of_items