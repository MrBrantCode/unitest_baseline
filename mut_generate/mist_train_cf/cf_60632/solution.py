"""
QUESTION:
Create a function named `fix_python_dict` that takes a dictionary `d` as input. The function should iterate through the dictionary's key-value pairs, convert non-string keys to strings, and convert non-integer values to integers if possible. If a value cannot be converted to an integer, it should be converted to a string. The function should also identify and print any duplicate keys found. The function should return a new dictionary with the corrected key-value pairs, without modifying the original dictionary.
"""

def fix_python_dict(d):
    new_d = {}
    for k, v in d.items():
        str_key = str(k)  # Convert key to string

        if isinstance(v, int):  # Check if value is already an integer
            new_val = v
        else:
            try:
                new_val = int(v)  # Try to convert value to integer
            except ValueError:
                new_val = str(v)  # Convert to string if not possible 

        if str_key in new_d:  # Check for duplicate keys
            print(f"Duplicate key found: {str_key}")
        else:
            new_d[str_key] = new_val  # Update the new dictionary
            
    return new_d