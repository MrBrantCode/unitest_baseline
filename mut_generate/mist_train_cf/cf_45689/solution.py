"""
QUESTION:
Create a function `dict_sum` that calculates the sum of all numeric values in a given dictionary. The function should handle cases where a key contains a non-numeric value by catching the TypeError and printing an error message indicating which key contains the non-numeric value. The function should also handle cases where a key is not found in the dictionary by catching the KeyError and printing an error message.
"""

def dict_sum(dic):
    total = 0
    for key in dic:
        try:
            total += dic[key]
        except KeyError:
            print(f"KeyError: '{key}' not found.")
        except TypeError:
            print(f"TypeError: '{key}' contains non-numeric value.")
    return total