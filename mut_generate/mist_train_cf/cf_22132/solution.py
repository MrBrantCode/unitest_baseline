"""
QUESTION:
Write a function `findOldestPerson` that takes a list of dictionaries as input, where each dictionary contains information about a person with keys 'name' and optionally 'age'. The function should return the name and age of the oldest person, where the age is rounded to the nearest integer. The input list should not contain any duplicate names, and the function should handle cases where the 'age' key is missing or has a negative value. The function should also ensure that the names are displayed in alphabetical order.
"""

def findOldestPerson(people):
    """
    Find the oldest person in a list of dictionaries.
    
    Args:
    people (list): A list of dictionaries, each containing 'name' and optionally 'age' keys.
    
    Returns:
    tuple: A tuple containing the name and age of the oldest person, or None if no valid age is found.
    """
    # Remove duplicates
    people = [dict(t) for t in {tuple(d.items()) for d in people}]
    
    # Sort by name
    people.sort(key=lambda x: x['name'])
    
    # Find the oldest person
    oldest_person = None
    for person in people:
        if 'age' in person and person['age'] > 0:
            if oldest_person is None or person['age'] > oldest_person['age']:
                oldest_person = person
                
    # Return the name and age of the oldest person
    if oldest_person:
        return oldest_person['name'], round(oldest_person['age'])
    else:
        return None