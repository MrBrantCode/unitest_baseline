"""
QUESTION:
Collect Unique Values from a List of Dictionaries

Define a function `collect_unique_values` that takes a list of dictionaries as input. The function should return a list of unique keys (strings) from the dictionaries, where each key is at least 3 characters long. The returned keys should be sorted in descending order based on their corresponding "price" values (numbers) and in ascending order based on the keys themselves in case of a price tie. If a dictionary is missing a "key" or "price" field, or if the "key" is not a string with at least 3 characters, or if the "price" is not a number, the function should skip that dictionary. If the input list is empty, the function should return an empty list.
"""

def collect_unique_values(lst):
    # Check if the list is empty
    if not lst:
        return []
    
    # Initialize a dictionary to store unique values based on the "key" field
    unique_values = {}
    
    # Iterate over each dictionary in the list
    for d in lst:
        # Check if the dictionary has a "key" field and its value is a string with at least 3 characters
        if "key" in d and isinstance(d["key"], str) and len(d["key"]) >= 3:
            # Check if the dictionary has a "price" field and its value is a number
            if "price" in d and isinstance(d["price"], (int, float)):
                key = d["key"]
                price = d["price"]
                
                # If the key is not already in the unique_values dictionary, add it with its price as the value
                if key not in unique_values:
                    unique_values[key] = price
                # If the key is already in the unique_values dictionary, compare the prices and names
                else:
                    # If the price is greater, update the value with the new price
                    if price > unique_values[key]:
                        unique_values[key] = price
                    # If the price is the same, compare the names in ascending order
                    elif price == unique_values[key]:
                        if key < min(unique_values, key=unique_values.get):
                            unique_values[key] = price
            else:
                # If the "price" field is missing or invalid, skip this dictionary
                continue
        else:
            # If the "key" field is missing or invalid, skip this dictionary
            continue
    
    # Sort the unique values in descending order based on the "price" field and ascending order based on the names
    sorted_values = sorted(unique_values.items(), key=lambda x: (-x[1], x[0]))
    
    # Extract the keys from the sorted values
    result = [value[0] for value in sorted_values]
    return result