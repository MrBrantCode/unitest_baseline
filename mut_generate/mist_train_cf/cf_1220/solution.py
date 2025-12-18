"""
QUESTION:
Transform a list of dictionaries representing people into a new list of dictionaries with only 'name', 'age', and 'address' keys, sorted by age in ascending order, and with no duplicates. The function should take a list of dictionaries as input where each dictionary contains 'name', 'age', 'email', and 'address' keys. If the input list is empty, the function should return an empty list. The function name should be `transform_data`.
"""

def transform_data(data):
    if len(data) == 0:
        return []
    
    # Sort the data list by age in ascending order
    sorted_data = sorted(data, key=lambda x: x['age'])
    
    # Create a new list of dictionaries with only 'name', 'age', and 'address' keys
    transformed_data = []
    seen = set()
    for person in sorted_data:
        name_age = (person['name'], person['age'], person['address'])
        if name_age not in seen:
            transformed_person = {
                'name': person['name'],
                'age': person['age'],
                'address': person['address']
            }
            transformed_data.append(transformed_person)
            seen.add(name_age)
    
    return transformed_data