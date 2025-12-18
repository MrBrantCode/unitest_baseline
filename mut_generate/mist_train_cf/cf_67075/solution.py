"""
QUESTION:
Create a function named `process_dict` that takes a dictionary as input. The dictionary may have existing key-value pairs. The function should enrich the dictionary with three additional key-value pairs: one integer value, one dictionary with at least two key-value pairs, and one function that takes an input and uses it within an operation. Then, the function should iterate over the dictionary. For each key-value pair: if the value is a dictionary, print the key and all the key-value pairs of this nested dictionary; if the value is an integer, increase it by 20%; if it's a function, call it with a suitable input. The function should also return the modified dictionary.
"""

def process_dict(input_dict):
    # Enrich the dictionary with three additional key-value pairs
    input_dict["grade"] = 90
    input_dict["hobbies"] = {"soccer": True, "reading": False}
    input_dict["calc_double"] = lambda x: x*2

    # Process the dictionary
    for key, value in input_dict.items():
        if isinstance(value, dict): 
            print(key + ":")
            for subkey, subvalue in value.items():
                print(subkey, subvalue)
        elif isinstance(value, int): 
            input_dict[key] = int(value*1.2) 
        elif callable(value): 
            print("Result of function '{}' with value 5 is: {}".format(key, value(5)))

    # Return the modified dictionary
    return input_dict