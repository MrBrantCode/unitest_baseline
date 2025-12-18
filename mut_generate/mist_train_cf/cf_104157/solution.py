"""
QUESTION:
Write a function `transform_data` that takes a list of dictionaries as input where each dictionary represents a person with 'name', 'age', and 'email' keys. The function should return a new list of dictionaries containing only the 'name' and 'age' of each person, sorted by age in ascending order. If there are duplicate entries, they should be removed from the output list. If the input list is empty, the function should return an empty list.
"""

def transform_data(data):
    # Sort the input list by age in ascending order and remove duplicates
    seen = set()
    sorted_data = []
    for person in sorted(data, key=lambda x: x['age']):
        key = (person['name'], person['age'])
        if key not in seen:
            seen.add(key)
            sorted_data.append(person)
    
    # Create a new list of dictionaries with only name and age
    transformed_data = [{'name': person['name'], 'age': person['age']} for person in sorted_data]
    
    return transformed_data