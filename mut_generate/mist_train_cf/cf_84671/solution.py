"""
QUESTION:
Implement a function named `valid_key_value` that takes a dictionary and a key as input. The function should return `True` if the key exists in the dictionary, the key is a string, and its corresponding value is an integer. If the key or value is of the wrong data type, or if the key does not exist, the function should return `False` and print an error message indicating the specific issue.
"""

def valid_key_value(dictionary, key):
    if isinstance(key, str):   # Check if key is of string data type
        if key in dictionary:    # Check if key exists in the dictionary
            if isinstance(dictionary[key], int):   # Check if value is of integer data type
                return True
            else:
                print("The value is not of integer data type.")
                return False
        else:
            print("The key does not exist in the dictionary.")
            return False
    else:
        print("The key is not of string data type.")
        return False