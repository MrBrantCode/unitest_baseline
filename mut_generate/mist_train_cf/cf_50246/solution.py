"""
QUESTION:
Write a function `look_up_and_reverse` that takes a dictionary `d` and a list of keys `keys` as input, and returns a new dictionary with the same keys from the input list and their corresponding values from the input dictionary, but with the values reversed. If a key is not found in the dictionary, print an error message. The function should handle invalid inputs and non-integer values. The values in the dictionary are assumed to be positive integers and the keys are strings.
"""

def look_up_and_reverse(d: dict, keys: list) -> dict:
    if not isinstance(d, dict) or not isinstance(keys, list):
        return "Error: Invalid inputs"
        
    reverse_dict = {}

    for key in keys:
        try:
            value = str(d[key])
            reverse_dict[key] = int(value[::-1])
        except KeyError:
            print(f"Key {key} not found in dictionary.")
        except ValueError:
            print(f"Value of key {key} is not a valid integer.")
            
    return reverse_dict