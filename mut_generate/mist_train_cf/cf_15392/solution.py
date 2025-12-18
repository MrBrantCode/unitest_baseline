"""
QUESTION:
Create a function `checkout_dictionary` that takes a dictionary as input and returns a string representation of the dictionary. The output string should have the following properties: 
- keys are sorted in ascending order
- values are in all uppercase letters and truncated to a maximum length of 50 characters
- each key-value pair is separated by a comma
- the dictionary should not contain any duplicate keys
- the key-value pairs are sorted alphabetically in the format "key1:VALUE1, key2:VALUE2, ...".
"""

def checkout_dictionary(dictionary):
    sorted_dict = {}
    
    # Sort the dictionary by keys
    for key in sorted(dictionary.keys()):
        # Convert the value to uppercase and limit the length to 50 characters
        value = dictionary[key].upper()[:50]
        sorted_dict[key] = value
    
    # Convert the sorted dictionary to a string
    result = ""
    for key, value in sorted(sorted_dict.items()):
        result += f"{key}:{value}, "
    
    # Remove the trailing comma and space
    result = result.rstrip(", ")
    
    return result