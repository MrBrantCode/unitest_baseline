"""
QUESTION:
Write a function called `print_ratings` to parse JSON data containing a list of items. The function should print the "rating" of every item in the list. If a nested object is present within an item, it should traverse through the nested object and print out the values of any "rating" keys found. The function should also print the path to the nested object in the format "path.to.nested.object". The function should handle cases with missing or invalid keys and display an error message for each invalid entry. The function should not exceed a maximum depth of 5 levels when traversing through nested objects.
"""

import json

def print_ratings(data, path="", depth=0):
    if depth > 5:
        print(f"{path}: Maximum depth exceeded")
        return
    
    if isinstance(data, list):
        for i, item in enumerate(data):
            print_ratings(item, path=path+f"[{i}]", depth=depth+1)
    elif isinstance(data, dict):
        if "rating" in data:
            rating = data["rating"]
            if isinstance(rating, (int, float)):
                print(f"{path}.rating: {rating}")
            else:
                print(f"{path}.rating: Invalid value")
        
        for key, value in data.items():
            if key != "rating":
                print_ratings(value, path=path+f".{key}", depth=depth+1)
    else:
        print(f"{path}: Invalid data")