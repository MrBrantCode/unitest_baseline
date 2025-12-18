"""
QUESTION:
Create a function called "square_dict_values" that takes a dictionary as input and returns a new dictionary with the values squared. The function should include the following properties: 

- It should only include key-value pairs from the input dictionary where both the key and value are integers and the value is positive.
- It should handle cases where the input dictionary is empty, in which case it should return an empty dictionary.
- It should ignore non-integer keys and negative values, excluding them from the output dictionary.
"""

def square_dict_values(input_dict):
    new_dict = {}
    
    for key, value in input_dict.items():
        if isinstance(key, int) and isinstance(value, int) and value > 0:
            squared_value = value ** 2
            new_dict[key] = squared_value
    
    return new_dict