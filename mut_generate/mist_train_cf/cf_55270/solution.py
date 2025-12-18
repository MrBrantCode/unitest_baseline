"""
QUESTION:
Write a function named `parse_kv_pairs` that takes a string `kv_string` as input and returns a dictionary. The input string contains lines of key-value pairs separated by equals signs, and the function should parse the string into a dictionary where keys are the keys from the input string and values are the corresponding values. 

If a key appears multiple times in the input string, the function should store the corresponding values in a list. The function should also handle edge cases such as keys or values containing equals signs, or lines without an equals sign. In the latter case, the function should skip the line and print a warning message.
"""

def parse_kv_pairs(kv_string):
    kv_dict = {}
    entries = kv_string.split('\n')
    for entry in entries:
        kv = entry.split('=', 1) 
        if len(kv) == 2:
            key, value = kv[0], kv[1]
            if key in kv_dict:
                if isinstance(kv_dict[key], list):
                    kv_dict[key].append(value)
                else:
                    kv_dict[key] = [kv_dict[key], value] 
            else:
                kv_dict[key] = value
        else:
            print(f"Skipping invalid entry: '{entry}'")
    return kv_dict