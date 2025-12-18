"""
QUESTION:
Create a function called `checkout_dictionary` that takes a dictionary as input and returns a string representation of the dictionary. The requirements are: 
- The keys in the dictionary must be sorted in ascending order.
- The values must be converted to all uppercase letters and truncated to a maximum length of 50 characters.
- Each key-value pair must be separated by a comma in the output string.
- The dictionary should not contain any duplicate keys.
- The output string must be in the format "key1:VALUE1, key2:VALUE2, ...".
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