"""
QUESTION:
Create a function named `create_nested_dict` that stores the given data in a nested dictionary structure. The dictionary should have a key named 'name' and its corresponding value should be another dictionary with keys 'first_name', 'last_name', 'age', and 'address'. The 'address' key should have a value that is also a dictionary with keys 'street', 'city', and 'state'.
"""

def create_nested_dict(first_name, last_name, age, street, city, state):
    """
    Creates a nested dictionary structure to store personal data.
    
    Args:
    first_name (str): The first name of the person.
    last_name (str): The last name of the person.
    age (int): The age of the person.
    street (str): The street address of the person.
    city (str): The city of the person's address.
    state (str): The state of the person's address.
    
    Returns:
    dict: A nested dictionary containing the person's data.
    """
    return {
        'name': {
            'first_name': first_name,
            'last_name': last_name,
            'age': age,
            'address': {
                'street': street,
                'city': city,
                'state': state
            }
        }
    }