"""
QUESTION:
Create a function named `retrieve_value` that takes a dictionary with at least 5 key-value pairs, a starting letter (case-insensitive), and a minimum value as input. The function should return the first key-value pair where the key starts with the given letter and the value is greater than the specified minimum value. If no matching pair is found, the function should return `(None, None)`.
"""

def retrieve_value(dictionary, starting_letter, minimum_value):
    starting_letter = starting_letter.lower()  
    minimum_value = max(minimum_value, 0)  

    for key, value in dictionary.items():
        if isinstance(value, (int, float)) and value > minimum_value:
            if key[0].lower() == starting_letter:
                return key, value

    return None, None  