"""
QUESTION:
Write a Python function `print_sorted_dict` that recursively prints all key-value pairs in a dictionary. The function should print key-value pairs in alphabetical order of the keys, excluding any pairs where the key starts with a vowel or the value is a string containing a digit. The function should not return any value, only print the key-value pairs. The input dictionary can contain any type of values, including strings, integers, and other types.
"""

def print_sorted_dict(dictionary):
    # Base case: if the dictionary is empty, return
    if len(dictionary) == 0:
        return
    
    # Sort the keys in alphabetical order
    sorted_keys = sorted(dictionary.keys())
    
    # Iterate over the sorted keys
    for key in sorted_keys:
        # Check if the key starts with a vowel
        if key[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            continue
        
        # Check if the value is a string that contains a digit
        if isinstance(dictionary[key], str) and any(char.isdigit() for char in dictionary[key]):
            continue
        
        # Print the key-value pair
        print(key, ":", dictionary[key])
        
        # Create a new dictionary that excludes the current key
        new_dict = {k: dictionary[k] for k in dictionary if k != key}
        
        # Recursive call with the new dictionary
        print_sorted_dict(new_dict)