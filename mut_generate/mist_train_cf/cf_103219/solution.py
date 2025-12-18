"""
QUESTION:
Write a function named `sort_dictionary` that takes a dictionary as input and returns a new dictionary with the same key-value pairs sorted in reverse alphabetical order by key. The input dictionary contains only strings as keys and values.
"""

def sort_dictionary(dictionary):
    # Step 1: Get the list of keys from the dictionary
    keys = dictionary.keys()
    
    # Step 2: Sort the list of keys in reverse order
    sorted_keys = sorted(keys, reverse=True)
    
    # Step 3: Create an empty dictionary
    sorted_dict = {}
    
    # Step 4: Iterate over the sorted keys
    for key in sorted_keys:
        # Step 5: Retrieve the value from the original dictionary
        value = dictionary[key]
        
        # Step 6: Add the key-value pair to the new dictionary
        sorted_dict[key] = value
    
    # Step 7: Return the new sorted dictionary
    return sorted_dict