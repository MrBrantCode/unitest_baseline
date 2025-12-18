"""
QUESTION:
Write a function named `sort_fruits_veggies` that takes a list of mixed fruits and vegetables as input. The function should return a list with all fruits first, sorted alphabetically in a case-insensitive manner, followed by all vegetables also sorted alphabetically in a case-insensitive manner. The classification of fruits and vegetables is based on two predefined lists: `fruits` and `vegetables`.
"""

def sort_fruits_veggies(mixed):
    fruits = ["Grapefruit", "Apricot", "Fig", "Apple", "Banana", "Mango", "Orange"]
    vegetables = ["Carrot", "Eggplant", "Broccoli", "Leek", "Zucchini", "Onion", "Tomato"]

    fruit_list = [item for item in mixed if item.lower() in [f.lower() for f in fruits]]
    veggie_list = [item for item in mixed if item.lower() in [v.lower() for v in vegetables]]
    
    fruit_list.sort(key=str.lower)
    veggie_list.sort(key=str.lower)
    
    return fruit_list + veggie_list