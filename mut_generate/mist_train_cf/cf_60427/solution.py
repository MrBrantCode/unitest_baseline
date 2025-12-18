"""
QUESTION:
Implement a function named reverse_dict that takes a dictionary as input and reverses its contents, including any nested dictionaries, while updating the original dictionary. The function should handle edge cases such as uneven numbers of nested dictionaries and empty dictionaries. Assume that keys and values are strings and that keys maintain uniqueness when reversed.
"""

def reverse_dict(dictionary):
    for key in list(dictionary.keys()):
        if isinstance(dictionary[key], dict):  # Check if value is a dictionary
            reverse_dict(dictionary[key])  # Recursive call for sub-dictionary
        else:
            dictionary[key[::-1]] = dictionary[key][::-1] if isinstance(dictionary[key], str) else dictionary[key]
            if key != key[::-1]:
                del dictionary[key]  # Delete old key only if it differs from reversed key
    return dictionary