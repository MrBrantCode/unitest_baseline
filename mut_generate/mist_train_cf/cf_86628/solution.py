"""
QUESTION:
Create a function `retrieve_value` that takes a dictionary with at least 10 key-value pairs, a starting letter, and a minimum value as input, and returns the first value that starts with the given letter and is greater than the specified number along with its associated key. The function should be case-insensitive and handle negative minimum values.
"""

def retrieve_value(dictionary, starting_letter, minimum_value):
    # Convert the starting letter to lowercase
    starting_letter = starting_letter.lower()
    
    # Iterate through the dictionary
    for key, value in dictionary.items():
        # Check if the key starts with the given letter
        if key.lower().startswith(starting_letter):
            # Check if the value is greater than the minimum value
            if value > minimum_value:
                # Return the value and the associated key
                return value, key
    
    # If no value was found, return None
    return None