"""
QUESTION:
Create a function called `retrieve_value` that takes a dictionary with at least 5 key-value pairs, a starting letter, and a minimum value as input. The function should return the first key-value pair where the value is greater than the minimum value and the key starts with the given letter. The function should handle cases where the starting letter is uppercase and the minimum value is negative.
"""

def retrieve_value(dictionary, starting_letter, minimum_value):
    starting_letter = starting_letter.lower()  # Convert starting letter to lowercase
    minimum_value = max(minimum_value, 0)  # Ensure minimum value is non-negative

    for key, value in dictionary.items():
        if isinstance(value, (int, float)) and value > minimum_value:
            if key[0].lower() == starting_letter:
                return key, value

    return None, None  # Return None if no matching value is found