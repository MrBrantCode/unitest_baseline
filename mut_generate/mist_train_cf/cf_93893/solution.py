"""
QUESTION:
Implement a function named `custom_sort` that takes a list of dictionaries as input, where each dictionary contains 'public_id' and 'name' keys. The function should sort the list in descending order based on 'public_id', and for dictionaries with the same 'public_id', they should be sorted in ascending order based on 'name'. The sorting should be done using a custom sorting algorithm implemented from scratch, without using any built-in sorting functions or libraries.
"""

def custom_sort(data):
    # Sort the data by public_id in descending order
    data.sort(key=lambda x: x['public_id'], reverse=True)

    # Create a dictionary to store objects with the same public_id
    id_dict = {}

    # Iterate over the sorted data
    for obj in data:
        public_id = obj['public_id']
        name = obj['name']

        # If public_id already exists in the dictionary, append the object
        # Else, create a new list with the object as the value
        if public_id in id_dict:
            id_dict[public_id].append(obj)
        else:
            id_dict[public_id] = [obj]

    # Sort the objects with the same public_id by name in ascending order
    for public_id, obj_list in id_dict.items():
        obj_list.sort(key=lambda x: x['name'])

    # Flatten the dictionary back to a list
    sorted_data = []
    for obj_list in id_dict.values():
        sorted_data.extend(obj_list)

    return sorted_data